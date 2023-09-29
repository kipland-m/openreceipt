import socket

printer_ip = "192.168.1.100"
printer_port = 9100  # Default port for Raw Socket

try:
    printer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    printer_socket.settimeout(5)  # Set a timeout for the connection attempt
    printer_socket.connect((printer_ip, printer_port))
    
    # If the connection was successful, you can print a success message.
    print("Successfully connected to the printer.")
    
    # You can send your print data here.
    data = b"Your receipt data here..."
    printer_socket.send(data)
    
    printer_socket.close()  # Close the connection when done
    
except socket.error as e:
    # Handle connection errors here
    print(f"Error: {e}")
except Exception as e:
    # Handle other exceptions here
    print(f"An error occurred: {e}")