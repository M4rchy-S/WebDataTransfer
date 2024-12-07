from flask import Flask, render_template, redirect, url_for, current_app, send_from_directory
import os

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("main_page"))

@app.route("/data/<path:filename>", methods=["GET"])
def download(filename):
    downloads = os.path.join(current_app.root_path, "data")
    print("[DEBUG] " + downloads + "/" + filename)
    return send_from_directory(downloads, filename)


@app.route("/")
@app.route("/index.html")
def main_page():
    print("[DEBUG] " + os.path.join(current_app.root_path, "data"))
    file_names = os.listdir(os.path.join(current_app.root_path, "data"))
    return render_template("index.html", names=file_names)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")