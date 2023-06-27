#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def sherlock_hello():
	print(""" 
	
	-------------------------------------------
			SHERLOCK
	-------------------------------------------
	
	
	
	
	""")
	username = input(" ENTER USERNAME   : ")
	os.system("sudo python3 /home/kali/Desktop/tools/src/component/sherlock/sherlock/sherlock.py "+ username +"  " )
