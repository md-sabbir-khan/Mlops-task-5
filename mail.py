import smtplib

SERVER = ('smtp.gmail.com')

FROM = "sender@gmail.com"
password="senderpassword"

TO = ["receiveer@gmail.com"] # must be a list

SUBJECT = "Suspicious IP Address Detected "

# Taking ip From result.text file
 
f=open("/root/result.text", "r")
ip=f.read()


TEXT = (" The Suspicious IP Address is : {}".format(ip))

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.starttls() 
server.login(FROM, password) 
server.sendmail(FROM, TO, message)
server.quit()