import telnetlib
import time

username = 'cisco'
password = 'cisco'
IP = '123.123.123.113'

tn = telnetlib.Telnet(IP)

tn.read_until(b'Username: ')
tn.write(username.encode('ascii') + b'\n')

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"sh ip int brief \n")

time.sleep(1)
tn.write(b"exit \n")

print(tn.read_all().decode('ascii'))