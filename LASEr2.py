#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import time
import requests
import threading
import argparse
import random
import json
import os
writing = []
email='null'
header={
		'Range': 'bytes=0-0',
        'user-agent': "okhttp/3.10.0"
		}

username="" # 账号sxceshi1
swdid="" # "b4:cd:27:30:3e:f2"

def getinfo(id):
    r=requests.post("https://cloud.linspirer.com:883/public-interface.php",data=json.dumps({"is_encrypt":False,"method":"com.linspirer.app.getappbyids","id":"1","!version":"1","jsonrpc":"2.0","params":{"swdid":swdid,"username":username,"token":"null","ids":[str(id)]},"client_version":"5.1.0","_elapsed":1}))
    data=json.loads(r.text)
    datab=data.get('data')
    if(data.get('code')!=0):
        print("account and swdid invaild!")
        return "ERROR","ERROR","ERROR","ERROR","ERROR","ERROR","ERROR"
    for item in datab:
        print(f"packagename:",item.get('packagename'))
        print(f"target api:",item.get('target_sdk_version'))
        print(f"name:",item.get('name'))
        print(f"versionname:",item.get('versionname'))
        print(f"versioncode:",item.get('versioncode'))
        print(f"md5sum:",item.get('md5sum'))
        print(f"sha1:",item.get('sha1'))
        packagename=item.get('packagename')
        targetapi=str(item.get('target_sdk_version'))
        name=str(item.get('name'))
        versionname=item.get('versionname')
        versioncode=str(item.get('versioncode'))
        md5sum=item.get('md5sum')
        #sha1=str(item.get('sha1'))
        if item.get('sha1')==None:
            sha1="no sha1"
        else :
            sha1=str(item.get('sha1'))
        return packagename,name,targetapi,versionname,versioncode,md5sum,sha1
    print("ERROR",r.text)
    return "ERROR","ERROR","ERROR","ERROR","ERROR","ERROR","ERROR"
class downloadThread (threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        try:
            download(self.id)
        except Exception:
            log(self.id, "ERROR")
            raise Exception
def download(id):
    url = "https://cloud.linspirer.com:883/download.php?email="+email+"&appid="+str(id)+"&swdid="+"4a"+"&version="+str(random.randint(1,9000000))
    realurl="Null"
    res = requests.head(url, stream=True,headers=header)
    try:
        url=res.headers['Location']
        print(str(id),",",url) 
        realurl=url
    except:
        print("id:",str(id),"null")
        return
    #code here

    #code end
    a,b,c,d,e,f,g=getinfo(id)
    output(str(id),realurl,a,b,c,d,e,f,g)

def log(id, message):
    print("["+datetime.datetime.now().strftime("%H:%M:%S")+"]" +
          "["+str(id)+"]:", message)

def output(id,link,package,name,targetapi,versionname,versioncode,md5sum,sha1):
    global writing
    writing.append([id,link,package,name,targetapi,versionname,versioncode,md5sum,sha1])
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Please run with at least 5 arguments.')

    parser.add_argument('begin_id', type=int, help='Start_id')
    parser.add_argument('end_id', type=int, help='End_id')
    parser.add_argument('threads', type=int, help='Threads Count')
    parser.add_argument('swdid', type=str, help='swdid(Emui10/HarmonyOS requires SN, and others use mac addresses)')
    parser.add_argument('username', type=str, help='linspirer login username')
    args = parser.parse_args()
    beg = args.begin_id
    end = args.end_id
    threads = args.threads
    now = beg-1
    swdid= args.swdid
    username=args.username
    while now < end:
        if threading.activeCount() <= threads:
            downloadThread(now+1).start()
            now = now+1
        if len(writing):
            f = open("./result.csv", "a",encoding="utf-8")            
            f.write(writing[0][0]+","+writing[0][1]+","+writing[0][2]+","+writing[0][3]+","+writing[0][4]+","+writing[0][5]+","+writing[0][6]+","+writing[0][7]+","+writing[0][8]+"\n")
            writing.pop(0)
            f.close()
    while threading.activeCount() >1:
        pass