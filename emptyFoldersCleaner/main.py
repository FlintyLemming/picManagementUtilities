import os
dir_path = r'/Users/flintylemming/Downloads'
for root, dirs, files in os.walk(dir_path):
    if not os.listdir(root):
        os.rmdir(root)
        print(root)
