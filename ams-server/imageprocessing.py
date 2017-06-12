import zbar
from Crypto.Cipher import AES
from PIL import Image
import cv2
import base64
import sys, qrcode
import qrtools
from qrtools import QR
from Crypto import Random 
import os
from base64 import decodestring
     
def ipu(image_data,image_name):
       #to convert image to string
        #with open(image_data, "rb") as imageFile:


        #    str = base64.b64encode(imageFile.read())
        #    print str
        #file = open("newdata.txt","w") 
        
 
        #file.write(str+ "\n") 


        #to convert string to image
        #
    fh = open("%s.JPEG"%image_name, "wb")
    fh.write(image_data.decode('base64'))
    fh.close()
    picture = cv2.imread("%s.JPEG"%image_name)
    # Converts image to grayscale.        
    grayscale = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
    numpyarray = Image.fromarray(grayscale)
    width, height = numpyarray.size
    zbar_image = zbar.Image(width, height, 'Y800', numpyarray.tobytes())
    return zbar_image

def scanner(image_data, image_name):
    while True:
        scannedimg = ipu(image_data, image_name)
        # Scans the zbar image.
        scanner = zbar.ImageScanner()
        scanner.scan(scannedimg)
        # Prints data from image.
        for decoded in scannedimg:
            #print(decoded.data)
            extracteddata = decoded.data      
        print(extracteddata)
        decrypt(extracteddata)
        break

def decrypt(cipher):
    key = "thisisakeyforenc"        
    BLOCK_SIZE=16
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(key, AES.MODE_ECB, IV)
    decrypted = aes.decrypt(base64.b64decode(cipher))
    real_data = decrypted[0:8]
    print(real_data)
    print "Decrypted data:  %r" % real_data
    file = open("testfile.txt","a") 
    file.write(real_data+ "\n") 
            

                