#!/usr/bin/env python
# -*- coding utf-8 -*-
import os


def medusa_hello():
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	

	print(""" 
	
	-------------------------------------------
		   	MEDUSA
	-------------------------------------------
	
		Type : 
		1 - Just Password
		2 - Just Username
		3- - Usename Password
	
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
	


	types = input(" TYPE : ")
	ip = input(" IP address : ")
	portName = input(" Port Name Example ssh, ftp : ")
	      
	          
	inputid=''
	if(types=="1"):
		Username= input(" Username : ")
		inputid = input(" inputid : ")
	if(types=="2"):
		Password= input(" Password : ")
		inputid = input(" inputid: ")
	if(types=="3"):
		inputid2 = input(" PassFile : ")
		inputid = input(" UserFile : ")
	    	    	
	    
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
	       
	fname2 =''
	if(inputid2=='0'):
	       filename = input(" filename : ")
	       fname2 ="/home/kali/Desktop/"+filename+""
	if(inputid2=='1'):
	       fname2 ="./src/wordlist/common.txt"
	if(inputid2=='2'):
	       fname2 ="./src/wordlist/names.txt"
	if(inputid2=='3'):
	       fname2 ="./src/wordlist/apache-user-enum-1.0.txt"
	if(inputid2=='4'):
	       fname2 ="./src/wordlist/apache-user-enum-2.0.txt"
	if(inputid2=='5'):
	       fname2 ="./src/wordlist/directory-list-1.0.txt"
	if(inputid2=='6'):
	       fname2 ="./src/wordlist/directory-list-2.3-medium.txt"
	if(inputid2=='7'):
	       fname2 ="./src/wordlist/directory-list-2.3-small.txt"
	if(inputid2=='8'):
	       fname2 ="./src/wordlist/directory-list-lowercase-2.3-medium.txt"
	if(inputid2=='9'):
	       fname2 = "./src/wordlist/directory-list-lowercase-2.3-small.txt"
	if(inputid2=='10'):
	       fname2 = "./src/wordlist/medium.txt"
	if(inputid2=='11'):
	       fname2 = "./src/wordlist/fasttrack.txt"
	if(inputid2=='12'):
	       fname2 = "./src/wordlist/best110.txt"
	       
	       
	if(types=="1"):
	    	Username = input(" Username Enter: ")
	    	os.system("medusa -h "+ip+" -M "+portName+"  -u "+Username+" -P "+fname2+" ")
	    
	if(types=="2"):
	   	 Password = input(" Password Enter : ")
	   	 os.system("medusa -h "+ip+" -M "+portName+"  -U "+fname+" -p "+Password+" ")
	    
	if(types=="3"):
	    	 os.system("medusa -h "+ip+" -M "+portName+"  -U "+fname+" -P "+fname2+" ")
	  
			
		
	

