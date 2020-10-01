import socket

t_host = str(input("Enter the host to be scanned: "))   # Target Host, www.example.com
t_ip = socket.gethostbyname(t_host)
ihti = ["22","80"]
print ("Port Scanning complete")
