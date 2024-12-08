from flask import Flask, render_template, redirect, url_for, current_app, send_from_directory, request
import os
# from os import lsitdir, path, getcwd
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), "data")

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("main_page"))

@app.route("/data/<path:filename>", methods=["GET"])
def download(filename):
    downloads = os.path.join(current_app.root_path, "data")
    print("[DEBUG] " + downloads + "/" + filename)
    return send_from_directory(downloads, filename)


@app.route("/", methods=['POST', 'GET'])
@app.route("/index.html")
def main_page():
    if request.method == "POST":
        if 'files[]' not in request.files:
            print("[!] No file part")
            return redirect(url_for("main_page"))
        # file = request.files['files[]']
        files = request.files.getlist('files[]')
        for file in files:
            # filename = secure_filename(file.filename)
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for("main_page"))
        
    # print("[DEBUG] " + os.path.join(current_app.root_path, "data"))
    file_names = os.listdir(os.path.join(current_app.root_path, "data"))
    return render_template("index.html", names=file_names)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)