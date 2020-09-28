import os
import time

path = '/Users/gabrielmaya/Documents'
cur_list = None

while True:
    new_list = os.listdir(path)

    if new_list != cur_list:
        cur_list = new_list

        with open("File.txt", "w") as f:
            f.write('\n'.join(cur_list))

    time.sleep(5)