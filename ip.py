
import socket
import sys
print  ("Enter Your Name DNS Or Target")
hostname = input ()
ip=socket.gethostbyname(hostname)
print ("Host Name Is:",hostname,
	"\n" 'Target Ip Is :',ip)
