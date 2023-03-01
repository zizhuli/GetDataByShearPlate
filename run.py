from flask import Flask, request
import platform, time
import pyperclip

app = Flask(__name__)


# Unix 系统里，每行结尾只有“<换行>”，即“\n”；
# Windows系统里面，每行结尾是“<回车><换行>”，即“ \r\n”；
# Mac系统里，每行结尾是“<回车>”


@app.route('/', methods=["POST"])
def get_data():
    pyperclip.paste()

    text = request.form.get("name")  # 获取数据

    with open("传输内容.txt", mode="w", encoding="utf-8") as fw:
        # 判断判断当前系统是否为windows
        if platform.system().lower() == 'windows':
            text = str(text).replace("\r\n", "\n")

        fw.write(text)

    with open("传输内容.txt", mode="r", encoding="utf-8") as fr:
        pyperclip.copy(fr.read())

    time.sleep(1)

    return "submit successfully"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="2532", debug=True)
