import requests  # lib used for making HTTP requests
import json  # lib used for working with JSON objects

# I created an API that is hosted as a Heroku app
# the API accepts 4 key value pairs
# level, lang, tweets, phd
# returns a prediction of whether the candidate interview well (True) or not (False)
#url = "http://127.0.0.1:5000/predict?level=Junior&lang=Java&tweets=yes&phd=yes"
url = "https://interview-app-gina.herokuapp.com/predict?level=Junior&lang=Java&tweets=yes&phd=no"


# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
response = requests.get(url)

# check the reponse's status code
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
print("status code:", response.status_code)

if response.status_code == 200:
    # success! grab the JSON object from the message body
    json_object = json.loads(response.text)
    print(json_object)
    prediction = json_object["prediction"]
    print(prediction)
