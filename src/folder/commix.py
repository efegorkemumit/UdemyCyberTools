#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def commix_hello():
	print(""" 
	
	-------------------------------------------
			COMMIX
	-------------------------------------------
	USE BURP SUITE
	
	example : commix --url="http://192.168.187.135/bWAPP/commandi.php" --cookie="PHPSESSID=b50548eac2338d9d3a41d29562490423; security_level=0" --data="target=www.nsa.gov&form=submit"

	
	
	
	
	""")
	fullurl = input(" ENTER FULL URL   : ")
	cookie = input(" ENTER COOKIE   : ")
	data = input(" ENTER DATA   : ")
	os.system("commix --url=\""+fullurl+"\" --cookie=\""+cookie+"\" --data=\""+data+"\" "  )
	
	
