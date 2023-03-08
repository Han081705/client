import socket

def transfer_file_socket_client(file_name, host='172.20.10.7', port=12345):
    # create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the server's address and port
    server_address = (host, port)
    print('connecting to {} port {}'.format(*server_address))
    client_socket.connect(server_address)
    print("connected")

    file = open(file_name, 'wb')
    file_data = client_socket.recv(1024)
    file.write(file_data)
    file.close()
    print("recieved successfullly")

def receive_video(file_name, host='172.20.10.7', port=12345):
    # create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the server's address and port
    server_address = (host, port)
    print('connecting to {} port {}'.format(*server_address))
    client_socket.connect(server_address)
    print("connected")

    file = open(file_name, 'wb')
    with open(file_name, 'wb') as f:
            while True:
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
                file.close()
    print("recieved successfullly")

def send_video(file_name, host='172.20.10.7', port=12345):
    # create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the server's address and port
    server_address = (host, port)
    print('connecting to {} port {}'.format(*server_address))
    connection = client_socket.connect(server_address)
    print("connected")

    with open(file_name, 'rb') as f:
        chunk = f.read(1024)
        while chunk:
            client_socket.send(chunk)
            chunk = f.read(1024)

    client_socket.close()

if __name__ == '__main__':
    #receive_video('video/tes_file.mov')
    send_video("video/test_send.mov")