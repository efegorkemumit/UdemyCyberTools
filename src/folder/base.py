#!/usr/bin/env python
# -*- coding utf-8 -*-


import os
import base64


def cryptology_hello():
	print(""" 
	------------------------------
	
		CRYPTOLOGY
	------------------------------
	""")
	
	Evalue = input(" Enter Value  :  ")
	
	print(""" 
	------------------------------
	------------------------------
	------------------------------
	
	""")
	
	try:
		data= Evalue
		data = base64.b64decode(data.encode().decode())
		print("Base64   : " +data.decode('utf-8'))
	except:
		print("Base64   : Error")
	
	try:
		data= Evalue
		data = base64.b32decode(data.encode().decode())
		print("Base32   : " +data.decode('utf-8'))
	except:
		print("Base32   : Error")
		
	
	try:
		data= Evalue
		data = base64.b16decode(data.encode().decode())
		print("Base16   : " +data.decode('utf-8'))
	except:
		print("Base16   : Error")
		
	
	try:
		data= Evalue
		data = bytearray.fromhex(dataencode().decode())
		print("Hex   : " +data.decode('utf-8'))
	except:
		print("Hex   : Error")
