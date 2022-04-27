#importing the qrcode module
import qrcode
#assigning a variable
# url = input("Enter the url to generate QR Code")
img = qrcode.make("www.youtube.com")

#saving the qrcode
img.save("Your_QRCode.png")
