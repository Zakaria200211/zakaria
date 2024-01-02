import os
try:
 import requests
 import time
except:
 
 os.system('pip install requests')
 os.system('pip install time')

A = "\033[1;91m" #احمر
E = "\033[1;92m" #اخضر
H = "\033[1;93m" #اصفر

link= input(H+'ENTER URL : ')

data = {
"key": '878dba56e07899059e6c7eb936c2fe68',
"action": "add",
"service": "1548",
"link": link,
"quantity": "2000"}

while True:
 url = "https://smmxpepo.shop/api/v2"
 time.sleep(5)
 req =requests.post(url,data=data).text
 if "order" in req:
  print(E+'Good 2K ')
 else:
  print(f'{A}Bad {req} ')
