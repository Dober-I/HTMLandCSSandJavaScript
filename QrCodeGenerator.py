# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import qrcode
import cv2


# Create The variable to store the information
# it also can be a link for an image
link = "https://google.com"  
data = "Insert something here"

# Encode The Link or Data
img = qrcode.make(data)
print(type(img))


# Save the QR Code
img.save("test1.jpg")



# Create The Decoder
decoder = cv2.QRCodeDetector()


# Load Your Data
file_name = "test1.jpg"
image = cv2.imread(file_name)


# Decode and Print the required information
link, data_points, straight_qrcode = decoder.detectAndDecode(image)
print(link)


#Determines the matrix size of the QR code.
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
