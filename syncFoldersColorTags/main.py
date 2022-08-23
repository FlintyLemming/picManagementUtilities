import os
import subprocess

# 使用前需要用 brew 安装 tag
# https://github.com/jdberry/tag

referredFolder = input("来源文件夹路径：")
targetFolder = input("目标文件夹路径：")
referredFolderInfo = os.popen("cd \"" + referredFolder + "\" && tag")
for folder in referredFolderInfo.readlines():
    colorInfo = folder.split("\t")[len(folder.split("\t")) - 1]
    subprocess.call(['tag', '-s', colorInfo.split("\n")[0], targetFolder + "/" + folder.split(" ")[0]])
