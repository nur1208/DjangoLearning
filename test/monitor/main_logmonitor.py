import configparser
import os
import re
import subprocess
import sys
import time
from tkinter import *


from monitor import logMonitor
from utils import execSQL, getConfig


def main():
    # global db
    db = getConfig()
    data = execSQL(db, "SELECT VERSION()")
    print(time.strftime('[%H:%M:%S]') + " The version of database: %s " % data)
    time.sleep(1)
    data = execSQL(db, "show variables like '%general_log%';")[1]
    print(time.strftime('[%H:%M:%S]') + ' The status of log:' + data)
    if data == "OFF":
        try:
            print(time.strftime('[%H:%M:%S]') + ' Starting log mode...')
            time.sleep(1)
            try:
                # logPath = r'D:\\github\\MySQL_Monitor\\'
                logPath = os.getcwd()
                # print("path "+logPath) 
                global log
                logName = str(time.strftime('%Y_%m_%d')) + "_log.txt"
                log = logPath + "/" + logName
                log = log.replace("\\", "/")  # for windows not support to use \ in log file path
                # print(log)
                data = execSQL(db, "set global general_log_file='" + log + "';")
                # print(data)
            except:
                print("here error")
                pass

            data = execSQL(db, "set global general_log=on;")
            data = execSQL(db, "show variables like '%general_log%';")[1]
            # print(data)
            if data == "ON":
                print(time.strftime('[%H:%M:%S]') + ' Log is started. ✅')
                print(time.strftime('[%H:%M:%S]') + ' Log monitor running... ')
                log = str(execSQL(db, "show variables like 'general_log_file';")[-1])
                logMonitor(log, db)
                # db.close()

        except:
            print(time.strftime('[%H:%M:%S]') + ' Log starting failed. ❌')
            exit()
    else:
        print(time.strftime('[%H:%M:%S]') + ' Log monitor running...')
    log = str(execSQL(db, "show variables like 'general_log_file';")[-1])
    logMonitor(log, db)
    # db.close()


if __name__ == '__main__':
    main()