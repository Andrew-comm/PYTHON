import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the web server and port
server_address = ('www.example.com', 80)

# Connect to the server
client_socket.connect(server_address)

# Send an HTTP request to fetch a web page
request = "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
client_socket.send(request.encode())

# Receive the server's response
response = b''
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

# Print the response (the web page content)
print(response.decode())

# Close the socket
client_socket.close()

