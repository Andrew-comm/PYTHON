import socket

def serve(port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)

    print(f"Serving HTTP on port {port}...")
    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode()
        print(request)

        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!"
        client_socket.sendall(response.encode())
        client_socket.close()

if __name__ == '__main__':
    serve()