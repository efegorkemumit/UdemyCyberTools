#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def hash_hello():
	print(""" 
	
	-------------------------------------------
			HASH ANALYZ
	-------------------------------------------
	
	
	
	
	""")
	os.system("sudo python /home/kali/Desktop/tools/src/component/hash-identifier/hash-id.py" )
