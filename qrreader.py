from pyzbar.pyzbar import decode
from PIL import Image
# readingimage
img=Image.open("qr1.png")
cont=decode(img)
if cont:
    # If QR code(s) detected, print the decoded data
    print(cont[0].data.decode())
else:
    print("No QR code found.")