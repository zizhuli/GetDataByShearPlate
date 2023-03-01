import pyperclip
import platform
import time
from datetime import datetime
import traceback

print('run read_shear_plate.py')

text = ""

while True:
    try:

        new_text = pyperclip.paste()

        if text != new_text:
            text = new_text

            if platform.system().lower() == 'windows':
                new_text = str(new_text).replace("\r\n", "\n")

            with open("传输内容.txt", mode="w", encoding="utf-8") as fw:
                fw.write(new_text)

            print(datetime.now())

    except BaseException:
        print(traceback.print_exc())

    time.sleep(1)
