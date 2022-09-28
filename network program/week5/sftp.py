import paramiko

hostname = "10.4.15.22"
username = "heart"
passwd = "062822"
port = 22

try:
    p = paramiko.Transport((hostname,port))
    p.connect(username=username,password=passwd)
    print("[*] Connected to "+ hostname + " via SSh")
    sftp = paramiko.SFTPClient.from_transport(p)
    print("[*] Strating file download")
    sftp.get("/home/heart/Hello","week5/download.text")
    print("[*] File download complete")
    print("[*] Starting file upload")
    sftp.put("week5/download.text","/home/heart/test")
    print("[*] File upload complete")
    p.close()
    print("[*] Disconnected from server")

except Exception as err:
    print("[!] " +str(err))