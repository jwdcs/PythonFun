# Basic Python3 program designed to check whether a specific IP's port is open or not
import socket

# A port scanner scans an IP and checks to see if a particular port is open
# AF_INET = IPv4, first parameter specifies type of connection
# SOCK_STREAM means it is a TCP (Transmission Control Protocol) socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Some IP's to test against
# Your own IP: ("192.168.1.1")
# This is the IP address of hackthissite.org ("137.74.187.103")
# We acquired it by using 'ping hackthissite.org' in Command Prompt
# Or, similarly, you could get it by entering 'hackthissite.org' for website input

host = ""
if(int(input("Enter 1 if you want to check a specific website, otherwise input 0: ")) == 1):
    try: 
        host = socket.gethostbyname(input("Enter website address: "))
        print("The IP Address of this website is", host)
    except Exception as e: 
        print("Error: the exception '" + str(e) + "' has occurred. Please run the script again.")
        quit()
else:
    try:
        host = input("Enter the specific IP: ")
    except Exception as e:
        print("Invalid input,", e, ". Start the script again.")
        quit()

port = int(input("Enter a port number to check: "))

while (port > 65535 or port < 0):
    print("You have entered a port either greater than 65,535 or less than 0. This is invalid. Try again.")
    port = int(input("Enter a port number to check: "))

print("Checking port, this may take some time...")

def portScanner(port):
    if s.connect_ex((host, port)):
        print("Port {0} is open for {1}".format(str(port), host))
    else:
        print("Port {0} is closed for {1}".format(str(port), host))

portScanner(port)
