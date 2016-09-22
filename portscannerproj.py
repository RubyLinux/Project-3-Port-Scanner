# By RubyLinux  
# Port scanner
import socket
import sys
import time 
from datetime import datetime

# Pre scan code
hostthing = raw_input("Which host would you like to scan?")
hostthingIP  = socket.gethostbyname(hostthing)
print "*" * 50
print "Scanning", hostthingIP
print ("From ports 1 to 65535")
timern = datetime.now()
print timern
print "*" * 50

# Actual scan code
try:
	for port in range (1,65535):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(5)
		res = sock.connect_ex((hostthingIP, port))
		if res == 0:
			print "Port {} is open".format(port)
        sock.close()
except KeyboardInterrupt:
    print "Exit"
    sys.exit()
except socket.error:
    print "Couldn't connect to server"
    sys.exit()
except socket.gaierror:
    print 'Exiting'
    sys.exit()
finally:
	sock.close()

timern2 = datetime.now()
speed =  timern2 - timern

print "*" * 50
print 'Completed in: ', speed
print "*" * 50