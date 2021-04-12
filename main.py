from socket import *

from pip._vendor.distlib.compat import raw_input

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server
mailServer = "localhost"
mailPort = 25


# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
recv = clientSocket.recv(1024).decode()
print ('test')
print (recv)
if recv[:3] != '220':
    print ('220 reply not received from server.')

# Send HELLO command and print server response.
heloCommand = ' EHLO Alice \r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print (recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.')

 #Send MAIL FROM command and print server response.
command = 'STARTTLS \r\n'
clientSocket.send(command.encode())
recva = clientSocket.recv(1024).decode()
print(recva)
mailfromCommand = 'MAIL FROM: brandonjohns914@yahoo.com \r\n.'
clientSocket.send(mailfromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('mail from 250 reply not received from server.')

# Send RCPT TO command and print server response.
rcpttoCommand = 'RCPT TO: brandonjohns914@yahoo.com \r\n'
clientSocket.send(rcpttoCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('rcpt to 250 reply not received from server.')

# Send DATA command and print server response
dataCommand = 'Data'
print(dataCommand)
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('data 250 reply not received from server.')

# Send message data.
message = raw_input('Enter Message Here: ').encode()

# Fill in end# Message ends with a single period.
mailMessageEnd = '\r\n.\r\n'
clientSocket.send(message )
clientSocket.send(mailMessageEnd.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('end msg 250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'Quit\r\n'
print(quitCommand)
clientSocket.send(quitCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('quit 250 reply not received from server.')

    pass

