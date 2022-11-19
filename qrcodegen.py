    # Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
import os

def qrgenerate(inp):
    # String which represents the QR code
    
    if inp == "":
        return print("Invalid URL!")
    print("URL to be used: ", inp)
    # Generate QR code
    u = pyqrcode.create(inp)

    # Create and save the svg file naming "myqr.svg"
    u.svg("myqr.svg", scale = 8)

    # Create and save the png file naming "myqr.png"
    u.png('myqr.png', scale = 6)
    print("QR Created at: ",os.getcwd())
    # os.open("./myqr.png")
    input("Press Enter to exit!")


inp = input("Enter the valid URL for QR Code Generation - \n Example www.google.com or https://shrimahakaleshwar.com/history \n\n URL:")
qrgenerate(inp)