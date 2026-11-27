from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/uranai")
def uranai():
    return render_template("uranai_form.html")


@app.route("/uranai/play", methods=["POST"])
def uranai_play():
    name = request.form.get("name", "")
    birthday = request.form.get("birthday", "")
    return render_template("uranai_play.html", name=name, birthday=birthday)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8889, debug=True)
