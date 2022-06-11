import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.0.87", 5050))
welcome = sock.recv(4096).decode()
print("Connected to server")
print("Server:", welcome)
while True:
    msg = input("Enter a message: ")
    if msg:
        sock.send(msg.encode())
        print("Server:", sock.recv(4096).decode())