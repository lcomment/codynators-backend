# we are going to use a micro web framework called Flask
# goal is to create a web app for our simple /predict API service
import pickle 
import os 
from flask import Flask, jsonify, request 

app = Flask(__name__)

# we need to add a route (2 actually)
# a route for the homepage
# a route is a path on a server to a function that handles the request
@app.route("/", methods=["GET"])
def index():
    # need to return content and a response code
    return "<h1>Welcome to my App!!</h1>", 200

# a route for /predict
@app.route("/predict", methods=["GET"])
def predict():
    # goals
    # 1. parse out the level, lang, tweets, phd args from the query string
    # use the request object to get the current requests query args
    level = request.args.get("level", "")
    lang = request.args.get("lang", "")
    tweets = request.args.get("tweets", "")
    phd = request.args.get("phd", "")
    print("level:", level, lang, tweets, phd)
    # 2. make a prediction using a decision tree
    prediction = predict_interviews_well([level, lang, tweets, phd])
    if prediction is not None:
        # 3. return prediction as a json response
        result = {"prediction": prediction}
        return jsonify(result), 200
    else:
        return "Error making prediction", 400


def predict_interviews_well(instance):
    # goals
    # 1. unpickle tree.p to get the header and interview_tree
    infile = open("tree.p", "rb")
    header, interview_tree = pickle.load(infile)
    print("header:", header)
    print("interview tree:", interview_tree)
    infile.close()

    # 2. write an algorithm to traverse the tree based on the instance until we hit a leaf node
    # then return the leaf node's class
    try:
        return tdidt_classifier(interview_tree, header, instance)
    except:
        return None
    # 3. if anything goes wrong, return None for the prediction

def tdidt_classifier(tree, header, instance):
    info_type = tree[0]
    if info_type == "Attribute":
        attribute = tree[1]
        attribute_index = header.index(attribute)
        test_value = instance[attribute_index]
        for i in range(2, len(tree)):
            value_list = tree[i]
            if value_list[1] == test_value:
                return tdidt_classifier(value_list[2], header, instance)
    else: # info_type == "Leaf" 
        leaf_label = tree[1]
        return leaf_label

if __name__ == "__main__":
    # deployment notes
    # two main categories of deployment
    # host your own server OR use a cloud provider (AWS, Azure, Heroku, DigitalOcean,...)
    # we are going to use Heroku (BaaS, backend as a service)
    # there are quite a few ways to deploy a Flask app to Heroku
    # 1. deploy the app directly on an ubuntu "stack" (e.g. Procfile and requirements.txt)
    # 2. deploy the app as a Docker container on a container "stack" (e.g. Dockerfile)
    # 2.A. build a Docker image locally and push the image to a container registry (e.g. Heroku's registry) 
    # 2.B. define a heroku.yml and push your source code to Heroku's git and
    # Heroku is going to build the Docker image (and register it)
    # 2.C. define main.yml and push your source code to Github and a Github Action builds
    # the image and pushes the image to the registry (e.g. Heroku's registry)
    port = os.environ.get("PORT", 5000) # Heroku will set the PORT environment variable for web traffic
    app.run(debug=False, host="0.0.0.0", port=port) # set debug=False before deployment!!