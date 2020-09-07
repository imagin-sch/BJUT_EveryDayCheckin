from requests import *
import json
import datetime

# Author : Imagin
# Blog : https://imagin.vip
# Date : 2020.9.07
# Time : 11:07:41
# python3 
# imagin wants a girl friend ❤


nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
base_url = "https://itsapp.bjut.edu.cn"
login_url = base_url + "/uc/wap/login/check"
user = "your student number"
password = "your pass"
data = {"username" : user, "password" : password}
s = session()

# 登录
try:
	login_res = s.post(login_url, data)
except Exception as e:
	print("[-] err on login!")


# 判断登录是否成功
try:
	login_data = json.loads(login_res.text)
	if login_data['m'] == '操作成功':
		print("[+] login success.")
	else:
		print("[-] login fail, " + login_data['m'])
except Exception as e:
	print("[-] json parse err.")


# 开始打卡
daka_url = base_url + "/xisuncov/wap/open-report/save"
daka_data = { "tw": 1 }
try:
	daka_res = s.post(daka_url, daka_data)
except Exception as e:
	print("[-] err on daka!")
	print(e)


# 判断打卡是否成功
try:
	daka_data = json.loads(login_res.text)
	if daka_data['m'] == '操作成功':
		print("[+] daka success.")
	else:
		print("[-] daka fail, " + daka_data['m'])
except Exception as e:
	print("[-] json parse err on daka.")

print("[+] {} all done.".format(nowTime))

# origin package:
"""
POST /uc/wap/login/check HTTP/1.1
Host: itsapp.bjut.edu.cn
Connection: close
Content-Length: 41
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://itsapp.bjut.edu.cn
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://itsapp.bjut.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fitsapp.bjut.edu.cn%2Fsite%2Fncov%2Fbjutdailyup
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: eai-sess=385vn4ha3f4lpk49aanlmdj2s3; UUkey=a586d5cb40dc4bca764634e006af6763

username=student_num&password=pass
"""


""" 
POST /xisuncov/wap/open-report/save HTTP/1.1
Host: itsapp.bjut.edu.cn
Connection: close
Content-Length: 4
Accept: application/json, text/plain, */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Origin: https://itsapp.bjut.edu.cn
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://itsapp.bjut.edu.cn/site/ncov/bjutdailyup
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: eai-sess=cookie1; UUkey=cookie2

tw=1
"""