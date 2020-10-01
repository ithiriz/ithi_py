import socket

t_host = str(input("Enter the host to be scanned: "))   # Target Host, www.example.com
t_ip = socket.gethostbyname(t_host)     # Resolve t_host to IPv4 address

print (t_ip)      # Print the IP address

while 1:
	#t_port = int(input("Enter the port: "))  # Enter the port to be scanned
    t_port = [22]
    for i in t_port:
        if i in [80,22,333,555]:
            print ("checking....")
    try:
        sock = socket.socket()
        res = sock.connect((t_ip, t_port))
        print ("Port {}: Open" .format(t_port))
        sock.close()
    except:
        print ("Port {}: Closed" .format(t_port))
print ("Port Scanning complete")
