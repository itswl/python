hostname=input('please input ip:defulf: 0.0.0.0')  
username=input('please input username:defulf: root')  
password=input('please input password:defult: *****')  
port_str=input('please input port:defult: 22')


if not hostname:
        hostname = '0.0.0.0'
print(hostname)
if not username:
	username ='root'
print(username)
if not password:
	password = '*****'
print(password)
if not port_str:
	port=22
else:
	port = int(port_str)
print(port)
