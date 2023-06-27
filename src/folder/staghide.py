#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def steghide_hello():
	print(""" 
	
	-------------------------------------------
			STEGHIDE
	-------------------------------------------
	
	
	
	
	""")
	
	fname = input(" Enter FNAME DESKTOP   : ")
	os.system(" steghide --extract -sf  /home/kali/Desktop/"+ fname +" " )
