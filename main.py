from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ

app = Flask(__name__)

# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）
@app.route('/')
def index():
    return render_template('index.html')


# 2. じゃんけんアプリの入力フォーム
@app.route('/janken')
def janken():
    # じゃんけんの入力画面のテンプレートを呼び出し
    return render_template('janken_form.html')


# 3. じゃんけんデータ送信先とじゃんけん結果表示画面
@app.route('/janken/play', methods=["POST"])
def janken_play():
    name = request.form.get("name")
    if not name:
        name = "名無しさん"

    hand = request.form.get("hand", None)
    is_settai = request.form.get("is_settai")

    if is_settai:
        if hand is None:
            hand = "rock"
        cpu = {"rock": "scissor", "scissor": "paper", "paper": "rock"}.get(hand)
    else:
        # リストの中からランダムに選ぶ
        cpu = random.choice(["rock", "scissor", "paper"])

    is_win = False
    if hand == cpu:
        result_message = "あいこ"
    elif hand == "rock":
        if cpu == "scissor":
            result_message = "{}の勝ち".format(name)
            is_win = True
        else:
            result_message = "{}の負け".format(name)
    elif hand == "scissor":
        if cpu == "paper":
            result_message = "{}の勝ち".format(name)
            is_win = True
        else:
            result_message = "{}の負け".format(name)
    elif hand == "paper":
        if cpu == "rock":
            result_message = "{}の勝ち".format(name)
            is_win = True
        else:
            result_message = "{}の負け".format(name)
    else:
        result_message = "後出しはダメです。"

    # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
    return render_template('janken_play.html',
                           result_message=result_message,
                           is_win=is_win,
                           name=name,
                           hand=hand,
                           cpu=cpu)


if __name__ == '__main__':
    # portは適宜書き換えてください
    app.run(host="0.0.0.0", port=8888, debug=True)