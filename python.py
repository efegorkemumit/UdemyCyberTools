#!/usr/bin/env python
# -*- coding utf-8 -*-


import os
import src.folder.anonymous as anonymous
import src.folder.basicInfo as basicinfo
import src.folder.nmap as nmap
import src.folder.passw as passw
import src.folder.medusa as medusa
import src.folder.base as basecry
import src.folder.waf as waf
import src.folder.hydra as hydra
import src.folder.sherlock as sherlock
import src.folder.whois as whois
import src.folder.gobuster as gobuster
import src.folder.weevely as weevely
import src.folder.sqlmap as sqlmap
import src.folder.commix as commix
import src.folder.hash as hashhh
import src.folder.existool as existool
import src.folder.staghide as staghide



def figlet():
	os.system("setxkbmap tr")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet efe gorkem umit")
	
def home():
	print(""" 
	
	------------------------------------------- -------------------------------------------
			TOOLS				  	BRUTE FORCE
	------------------------------------------- -------------------------------------------
	
	1-ANONYMOUS					10-MEDUSA
	2-BASIC INFORMATION				11-HYDRA
	3-NMAP						12-GOBUSTER
	4-PASWWD					13-METASPLOIT
	5-FIREWALL					14-MSFVENOM
	6-SHERLOCK
	7-WHOIS
	
	------------------------------------------- -------------------------------------------
		  CRYPTOLOGY Steganography			INJECTION
	------------------------------------------- -------------------------------------------
	
	20-BASIC CRYPTOLOGY				31-WEEVLEY
	21-HASH ANALYZ					32-SQLMAP
	22-EXIFTOOL					33-COMMIX
	23-STEGHIDE			
							
	
	
	
	""")

	

figlet()
home()

inputid = input(" Enter ID   : ")
if(inputid=="1"):
	anonymous.anonymous_hello()
if(inputid=="2"):
	basicinfo.basicInfo_Hello()
if(inputid=="3"):
	nmap.nmap_Hello()
if(inputid=="4"):
	passw.passw_hello()
if(inputid=="5"):
	waf.waf_hello()
if(inputid=="6"):
	sherlock.sherlock_hello()
if(inputid=="7"):
	whois.whois_hello()
if(inputid=="10"):
	medusa.medusa_hello()
if(inputid=="11"):
	hydra.hydra_hello()
if(inputid=="12"):
	gobuster.gobuster_hello()
if(inputid=="13"):
	os.system("msfconsole" )
if(inputid=="14"):
	os.system("msfvenom" )
if(inputid=="20"):
	basecry.cryptology_hello()
if(inputid=="21"):
	hashhh.hash_hello()
if(inputid=="22"):
	existool.exiftool_hello()
if(inputid=="23"):
	staghide.steghide_hello()
if(inputid=="31"):
	weevely.weevely_hello()
if(inputid=="32"):
	sqlmap.sqlmap_hello()
if(inputid=="33"):
	commix.commix_hello()

	



