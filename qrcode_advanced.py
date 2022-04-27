#importing qrcode module
import qrcode

#importing Image module from PIL Package
from PIL import Image

#editing the qr code
qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, border=5, box_size=10,)

#adding data to the QR Code
qr.add_data("www.instagram.com/__caraddict05__")

qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="black")

img.save("Advanced_QRCode.png")