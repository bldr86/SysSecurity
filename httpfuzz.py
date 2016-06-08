# Fuzzed HTTP Requests trying to find
# the maximum size that the server
# can handle

import sys, socket, time

# Use in the form "python httpfuzz.py host port"

host = sys.argv[1] # Recieve IP from user
port = int(sys.argv[2]) # Recieve Port from user

length = 100 # Initial length of 100 A's

while (length < 3000): # Stop once we've tried up to 3000 length
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Declare a TCP socket
	client.connect((host, port)) # Connect to user supplied port and IP address

	command = "GET /" +  length * "A" + " HTTP/1.1\r\nHost: "+ host + "\r\nConnection: Close\r\n\r\n"
	client.send(command) # Send the user command with a variable length name
	data = client.recv(1024) # Recieve Reply
	client.close() # Close the Connection
	time.sleep(2)
	print "Length Sent: " + str(length) # Output length of the request
	length += 100 # Try again with an increased length
