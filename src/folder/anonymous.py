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
			ANONYMOUS
	-------------------------------------------
	
	1-DNS CHANGER
	2-VPN
	3-MACCHANGER
	4-MACCHANGER ORIGINAL
	5-MACCHANGER OPTIMIZED
	
	
	
	""")
	
def anonymous_hello():
	figlet()
	home()

	
	inputid=input(" Enter ID : ")
	if(inputid=="1"):
		os.system("sudo nano /etc/resolv.conf  ")
	if(inputid=="2"):
		os.system("sudo openvpn /home/kali/Desktop/tools/src/component/vecihi.ovpn ")
	if(inputid=="3"):
		os.system("sudo macchanger -r eth0")
	if(inputid=="4"):
		os.system("sudo macchanger -p eth0")
	if(inputid=="5"):
		mac=input(" MAC ADDRESS  : ")
		os.system("sudo macchanger --mac "+mac+ " eth0")

	
	
	
	
	
