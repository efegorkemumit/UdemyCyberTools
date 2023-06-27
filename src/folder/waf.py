#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def waf_hello():
	print(""" 
	
	-------------------------------------------
			FIREWALL
	-------------------------------------------
	
	
	
	
	""")
	inputid = input(" Enter IP ADDRESS OR WEBSITE   : ")
	os.system("wafw00f  "+inputid)
