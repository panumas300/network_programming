import telnetlib


username = 'cisco'
password = 'cisco'

f = open('myswitches.txt')
x = list(f)
j = []
for i in x:
    if '\n' in i:
        j.append(i[0:-1])
    else:
        j.append(i)

for line in j:
    print(line)
    print("Configuring Switch " + (line))
    text = str(line)
    IP = text

    tn = telnetlib.Telnet(IP)

    tn.read_until (b'Username: ')
    tn.write (username.encode ('ascii') + b'\n')

    if password :
        tn.read_until (b"Password: ")
        tn.write (password.encode('ascii') + b"\n")

    tn.write (b"conf t \n")

    for n in range(2,10):
        tn.write(b"vlan " + str(n).encode('ascii') + b'\n')
        tn.write(b"name Ptyhon_VLAN_ " + str(n).encode('ascii') + b'\n')

    tn.write(b"end \n")
    tn.write (b"exit \n")

    print (tn.read_all().decode('ascii'))



