import paramiko

hostname = "10.4.15.22"
port = 22
user = "heart"
passwd = "062822"

try:
    client = paramiko.SSHClient()
    client.load_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=user, password=passwd)
    while True:
        try:
            cmd = input("$> ")
            if cmd == "exit": break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break
    client.close()
except Exception as err:
    print(str(err))