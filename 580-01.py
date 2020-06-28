#python3
#ssh to the device and get the netflow data
#print as file

import time, datetime, paramiko

ip = "192.168.0.103"
username = "cisco"
password = "cisco"

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
time.sleep(.5)
output = remote_conn.recv(65535)
print ("conn= ", output)

remote_conn.send("terminal length 0\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

remote_conn.send("show flow monitor test3 cache format csv\n")
time.sleep(.5)
output = remote_conn.recv(65535)

print ("show result is =", output)
print (type(output))
print (str(output, 'utf-8'))
print (type(str(output, 'utf-8')))

result = str(output, 'utf-8')
print ("================================")
print (type(result))
print (result)

remote_conn.send("exit\n")
time.sleep(.5)
output = remote_conn.recv(65535)

now = str(datetime.datetime.now())
print (type(now))

f = open ("netflow-raw-data_"+ip+"_"+now+".txt", 'w')
f.write (result)
f.close()

'''
flow record test3
 match ipv4 protocol
 match ipv4 source address
 match transport source-port
 match interface input
!
!
flow monitor test3
 record test3
!
!
interface GigabitEthernet1/0/37
 ip flow monitor test3 input

import time, datetime, requests, json, paramiko
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from flask import Flask
from flask import request
from requests_toolbelt.multipart.encoder import MultipartEncoder
#pip install requests-toolbelt
import datetime
'''