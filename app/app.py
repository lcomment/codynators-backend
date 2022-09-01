from flask import Flask, request, url_for
from DB_handler import DBModule
import algorithm_1
import algorithm_2

app = Flask(__name__)
DB = DBModule()
storage = DB.firebase.storage()


@app.route("/")
def index():
    return "악보 데이터 변환용 서버"


# json 형식
# {
#     "username": "string",
#     "filename": "string",
# }

@app.route("/", methods=['POST'])
def post():
    params = request.get_json()
    #print(params['username'])
    #path_on_cloud = f"{params['username']}/{params['filename']}"
    path_on_cloud = f"{params['filename']}"

    if params['filename'] != '여행을떠나요':
        image = storage.child(path_on_cloud+".png").download(f"./source/{params['filename']}"+".png")

    if image is None:
        print('cant download')

    if params['filename'] == '여행을떠나요':
        path_local = f"{params['filename']}" + ".csv"  # 샘플
    elif params['filename'] == 'canthaveyou':
        algorithm_1.musicsheet_algorithm(params['filename'])
        path_local = f"{params['filename']}" + ".csv"  # 샘플
    elif params['filename'] == 'butter':
        algorithm_2.butter_algorithm(params['filename'])
        path_local = f"{params['filename']}" + ".csv"  # 샘플
    #path_local = f"{params['filename']}" + ".csv"  # 샘플
    storage.child(path_on_cloud).put(path_local)
    return url_for('index')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
