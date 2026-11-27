from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

RESULTS_TABLE = [5, 1, 3, 2, 4]
RESULT_MESSAGES = {
    1: "今日は無理をせず、落ち着いて過ごすとよさそうです。",
    2: "身近な人との会話に小さな幸運がありそうです。",
    3: "これまでの努力が実を結ぶきっかけがありそうです。",
    4: "新しいことに挑戦するとよい流れに乗れそうです。",
    5: "思いがけない幸運に恵まれるかもしれません。",
}


@app.route("/uranai")
def uranai():
    return render_template("uranai_form.html")


@app.route("/uranai/play", methods=["POST"])
def uranai_play():
    name = request.form.get("name", "").strip()
    birthday = request.form.get("birthday", "").strip()

    try:
        birth_date = datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        uranai_rank = 1
        result_message = "入力不備で占えませんでした"
    else:
        if not name:
            uranai_rank = 1
            result_message = "入力不備で占えませんでした"
        else:
            today_int = int(datetime.now().strftime("%Y%m%d"))
            birth_int = int(birth_date.strftime("%Y%m%d"))
            diff = abs(today_int - birth_int)
            index = (diff * len(name)) % 5
            uranai_rank = RESULTS_TABLE[index]
            result_message = RESULT_MESSAGES[uranai_rank]

    return render_template(
        "uranai_play.html",
        name=name,
        birthday=birthday,
        uranai_rank=uranai_rank,
        result_message=result_message,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8889, debug=True)
