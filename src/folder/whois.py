#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def whois_hello():
	print(""" 
	
	-------------------------------------------
			WHOIS
	-------------------------------------------
	
	
	
	
	""")
	website = input(" ENTER WEBSITE OR IP   : ")
	os.system("sudo apt-get install whois " )
	os.system("clear" )
	figlet()
	os.system("sudo whois " + website + " " )
