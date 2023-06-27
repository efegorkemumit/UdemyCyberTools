#!/usr/bin/env python
# -*- coding utf-8 -*-
import os


def hydra_hello():
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	

	print(""" 
	
	-------------------------------------------
		   	HYDRA 
	-------------------------------------------
	
	
	    0-         select        Desktop File Name
	    1-         Directory     common.txt
	    2-         Username      names.txt
	    3-         Directory     apache-user-enum-1.0.txt
	    4-         Directory     apache-user-enum-2.0.txt
	    5-         Directory     directory-list-1.0.txt
	    6-         Directory     directory-list-2.3-medium.txt
	    7-         Directory     directory-list-2.3-small.txt
	    8-         Directory     directory-list-lowercase-2.3-medium.txt
	    9-         Directory     directory-list-lowercase-2.3-small.txt
	    10-        Directory     medium.txt
	    11-        Password      fasttrack.txt
	    12-        Password      best110.txt
	    13-         General      rockyou.txt
	
	
	
	
	""")
	
	ip = input(" IP exampe : ssh, ftp, imap  ftp://10.10.10.10     : ")
	inputid = input(" INPUT ID : ")
	username = input(" ENTER USERNAME : ")
	SSL = input(" SSL  Y/N : ")
	sslkt=''
	if(SSL=='Y' or SSL=='y'):
		sslkt='-S'
	else:
		sslkt=''
	
	fname =''
	if(inputid=='0'):
	       filename = input(" filename : ")
	       fname ="/home/kali/Desktop/"+filename+""
	if(inputid=='1'):
	       fname ="./src/wordlist/common.txt"
	if(inputid=='2'):
	       fname ="./src/wordlist/names.txt"
	if(inputid=='3'):
	       fname ="./src/wordlist/apache-user-enum-1.0.txt"
	if(inputid=='4'):
	       fname ="./src/wordlist/apache-user-enum-2.0.txt"
	if(inputid=='5'):
	       fname ="./src/wordlist/directory-list-1.0.txt"
	if(inputid=='6'):
	       fname ="./src/wordlist/directory-list-2.3-medium.txt"
	if(inputid=='7'):
	       fname ="./src/wordlist/directory-list-2.3-small.txt"
	if(inputid=='8'):
	       fname ="./src/wordlist/directory-list-lowercase-2.3-medium.txt"
	if(inputid=='9'):
	       fname = "./src/wordlist/directory-list-lowercase-2.3-small.txt"
	if(inputid=='10'):
	       fname = "./src/wordlist/medium.txt"
	if(inputid=='11'):
	       fname = "./src/wordlist/fasttrack.txt"
	if(inputid=='12'):
	       fname = "./src/wordlist/best110.txt"
	


	os.system("hydra  "+sslkt+" -l "+username+" -P " +fname+ " " +ip+ " " )
	       
	
			
		
	

