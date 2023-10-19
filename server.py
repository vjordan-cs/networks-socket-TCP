import socket


HOST = "0.0.0.0"
PORT = 3000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server started. Listening on {HOST}:{PORT}")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected by {client_address}")

    data = client_socket.recv(1024)
    while data:
        print(data.decode("utf-8"))
        data = client_socket.recv(1024)

    client_socket.close()
