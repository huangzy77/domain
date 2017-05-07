# -*- coding:utf-8 -*- 
import requests
import time
from xml.etree import ElementTree  


def request_func(url):
	try:
		r = requests.get('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}'.format(url),timeout=60)
		#time.sleep(1)
		t=r.text.decode('gbk').encode('utf8') #ElementTree不支持ＧＢＫ编码，所以要转码
		t=t.replace('gb2312', 'utf-8')
		root =ElementTree.fromstring(t)	
	except:
		print("Network is wrong,Trying restart...")
		time.sleep(3)
		return(request_func(url))
	return root


def query(domine,flag):
	domine_list=[domine+'.com',domine+'.net',domine+'.cn',domine+'.top',domine+'.club',domine+'.shop',domine+'.vip',domine+'.site',\
				domine+'.co',domine+'.tv',domine+'.click',domine+'.cc',domine+'.pro',domine+'.store',domine+'.ltd',domine+'.link']
	for d in domine_list:
		root=request_func(d)
		print d
		print(root[2].text)
		if root[2].text=='210 : Domain name is available':
			try:
				output = open('youcanget_words.txt', 'a+')
				output.write(str(flag)+" ")
				output.write(d+" ")
				output.write(root[2].text)
				output.write('\n')
				output.close()
				print("This is ok!")
			except:
				print("Write file is something wrong!")
		else: print("This domain is not ok!")
	

if __name__ == '__main__':
    # main()
	flag=0
	file_object = open('English_list.txt','r')
	for line in file_object:
		flag+=1
		print flag
		query(line.strip('\n'),flag)
	file_object.close()


