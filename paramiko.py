import paramiko
ssh = paramiko.SSHLIST()
ssh.set_missing_host_key_policy[paramiko.inte/.addPolicy])

ssh.[]connect(testname= "18.225.165.113", username="kali"
	Key_filename= 'D:\\Descargas\\jerkour", port=33'

sftp_client = ssh.open_sftp()
print(sftp_client.getcwd())
sftp_client-chdir("/home/kali")
print(sftp_client.getcwd())
sftp_clien.put(localpath: 'upload_JV.txt', remotepath: '/home/escritorio/upload_JV.txt')
sftp_clientclose()
ssh.close()