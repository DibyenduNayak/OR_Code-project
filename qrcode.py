import pyqrcode


content="i love python programming"


url=pyqrcode.create(content)
url.png("qr1.png",5)
print("QR code is generated successfully")
