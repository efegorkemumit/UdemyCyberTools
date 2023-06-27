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
		    BASIC INFORMATION
	-------------------------------------------
	
	1-DNSENUM
	2-DNSMAP
	3-NETDISCOVER
	4-DYMTRI
	
	
	
	
	""")
	
def basicInfo_Hello():
	figlet()
	home()
	
	
	inputid=input(" Enter ID : ")
	if(inputid=="1"):
		ip=input(" ip address or website : ")
		filename =input(" filename : ")
		os.system("dnsenum "+ ip +" -o /home/kali/Desktop/"+filename +" ")
	if(inputid=="2"):
		ip=input(" ip address or website : ")
		os.system("dnsmap "+ ip +"  ")
	if(inputid=="3"):
		os.system("sudo netdiscover")
	if(inputid=="4"):
		ip=input(" ip address or website : ")
		filename =input(" filename : ")
		os.system("dmitry "+ ip + " -winsebfb -o /home/kali/Desktop/"+filename + " ")
	
	
	
