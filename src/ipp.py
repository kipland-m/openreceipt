import subprocess

printer_ip = '192.168.1.100'  # Replace with the actual IP address of your printer
text_file = r'C:\Users\kip_m\Python\openreceipt\src\receipt.txt' # Replace with the path to your text file

# Use a command-line utility like 'lp' to send the text file to the printer
subprocess.run(['powershell', '-Command', f'Get-Content "{text_file}" | Out-Printer -Name "{printer_ip}"'])
