import socket
while True:
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("your IP address is : ",ip_address)
    print("if you are using vpn, for reloading your new ip address press Enter")
    print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    if(input()):
        pass