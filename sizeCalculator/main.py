import os
import pymysql
import time
import yaml


def get_dir_size(path, size=0):
    for root, dirs, files in os.walk(path):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


with open('config.yml', 'rb') as file:
    conf = yaml.safe_load(file)
with open('dbconfig.yml', 'rb') as dbFile:
    dbConf = yaml.safe_load(dbFile)
todayStr = time.strftime("%Y-%m-%d", time.localtime())
connect = pymysql.connect(host=dbConf['db']['host'],
                          user=dbConf['db']['user'],
                          password=dbConf['db']['password'],
                          db=dbConf['db']['schema'],
                          charset=dbConf['db']['charset'])
cur = connect.cursor()

indiFolderSize = get_dir_size(path=conf['folderPath']['indiFolder'])
groupFolderSize = get_dir_size(path=conf['folderPath']['groupFolder'])
exFolderSize = get_dir_size(path=conf['folderPath']['exFolder'])

try:
    sqlNew = "INSERT INTO folder_size ( `date`, `indiFolder`, `groupFolder`, `exFolder` ) VALUES ( '{0}', {1}, {2}, " \
             "{3} ) ON DUPLICATE KEY UPDATE `date` = '{0}', `indiFolder` = {1}, `groupFolder` = {2}, `exFolder` = {" \
             "3}"
    sqlStr = sqlNew.format(todayStr, indiFolderSize, groupFolderSize, exFolderSize)
    cur.execute(sqlStr)
except Exception as e:
    print("Error:", e)
else:
    connect.commit()
    print("Done")

cur.close()
connect.close()
