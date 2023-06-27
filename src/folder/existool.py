#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def exiftool_hello():
	print(""" 
	
	-------------------------------------------
			EXIFTOOL
	-------------------------------------------
	
	
	
	
	""")
	
	fname = input(" Enter FNAME DESKTOP   : ")
	os.system(" exiftool /home/kali/Desktop/"+ fname +" " )
