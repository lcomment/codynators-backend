from flask import Flask, redirect, render_template, url_for
from DB_handler import DBModule

app = Flask(__name__)
DB = DBModule()
storage = DB.firebase.storage()

username = "현석"
filename = "샘플" + ".txt"


@app.route("/")
def index():
    path_on_cloud = f"{username}/{filename}"
    path_local = "sample.txt"
    storage.child(path_on_cloud).put(path_local)
    return "악보 데이터 변환용 서버"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
