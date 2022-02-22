from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    serverName = '127.0.0.1'
    serverPort = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = 'MAIL FROM: py2076@nyu.edu\r\n'
    clientSocket.send(mailFrom.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = 'RCPT TO: py2076@nyu.edu'
    clientSocket.send(rcptTo.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    clientSocket.send('DATA\r\n')
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    # Fill in start
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg)
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg)
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    clientSocket.send('QUIT')
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    # Fill in end
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')