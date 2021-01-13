# pip install schedule
# Schedule deletion of files >= 1 week old from directory

import schedule
import time
import os


def file_delete():
    path = r"/home/matt/Security_Cam"
    now = time.time()

    for filename in os.listdir(path):
        if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
            if os.path.isfile(os.path.join(path, filename)):
                os.remove(os.path.join(path, filename))


schedule.every().wednesday.at("10:38").do(file_delete)

while True:
    schedule.run_pending()
    time.sleep(1)
