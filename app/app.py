from flask import Flask, request, url_for
from DB_handler import DBModule

app = Flask(__name__)
DB = DBModule()
storage = DB.firebase.storage()

username = "현석"
filename = "샘플" + ".txt"


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
    print(params['username'])
    path_on_cloud = f"{params['username']}/{params['filename']}"
    #path_local = f"{params['filename']}" + ".csv"  # 샘플
    path_local = "여행을떠나요.csv"  # 샘플
    storage.child(path_on_cloud).put(path_local)
    return url_for('index')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
