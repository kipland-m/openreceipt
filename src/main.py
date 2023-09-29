import socket

printer_ip = "192.168.1.100"
printer_port = 9100


printer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
printer_socket.connect((printer_ip, printer_port))

data = b"Your receipt data here..."
printer_socket.send(data)