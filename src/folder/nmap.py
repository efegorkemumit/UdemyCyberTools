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
			NMAP
	-------------------------------------------
	
	1-sP   			
	2--p 1-65535 -sV -sS -T4   
	3-v -sS -A -T4 
	4-v -sS -A -T5 
	5-v -sV -O -sS -T5 
	
	
	
	""")
	
def nmap_Hello():
	figlet()
	home()
	
	
	inputid=input(" Enter ID : ")
	ip=input(" IP : ")
	if(inputid=="1"):
		os.system("sudo nmap -sP "+ ip +"  ")
	if(inputid=="2"):
		os.system("sudo nmap -p 1-65535 -sV -sS -T4  "+ ip +"  ")
	if(inputid=="3"):
		os.system("sudo nmap -v -sS -A -T4  "+ ip +"  ")
	if(inputid=="4"):
		os.system("sudo nmap -v -sS -A -T5 "+ ip +"  ")
	if(inputid=="5"):
		os.system("sudo nmap -v -sV -O -sS -T5  "+ ip +"  ")
		
		
