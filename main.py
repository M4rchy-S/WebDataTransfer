from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("main_page"))

@app.route("/")
@app.route("/index.html")
def main_page():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")