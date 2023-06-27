#!/usr/bin/env python
# -*- coding utf-8 -*-
import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def home():
	print(""" 
	
	-------------------------------------------
		    PASSW
	-------------------------------------------
	
	1-CRUNCH
	2-WINRAR ZIP CRACK
	
	
	
	
	""")
	
def passw_hello():
	figlet()
	home()
	
	
	inputid=input(" Enter ID : ")
	if(inputid=="1"):
		first =input(" first : ")
		dated =input(" dated : ")
		filename =input(" filename : ")
		character =input(" character : ")
		os.system("sudo crunch "+first+" "+dated+" "+character+" -o /home/kali/Desktop/"+filename +"  ")
		
	if(inputid=="2"):
		filename =input(" filename : ")
		os.system("sudo python3 /home/kali/Desktop/tools/src/component/pyrarcr/pyrarcr.py  /home/kali/Desktop/"+filename+" ")
		
	
	
	
	
