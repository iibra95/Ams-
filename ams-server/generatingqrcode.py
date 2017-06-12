import base64
from Crypto import Random 
from Crypto.Cipher import AES 
from qrtools import QR
from qrcode import * 
import qrcode

def encryptingqrcode(plaintext):
    while len(plaintext) < 16:
        plaintext += "_"
    #length of block
    BLOCK_SIZE=16
    #key of encryption
    key = "thisisakeyforenc"
    #intial Vector
    IV = Random.new().read(BLOCK_SIZE)
    #AES encrypton method it take the key and the mode and IV to start the algorithm
    aes = AES.new(key, AES.MODE_ECB, IV)
    #encrypting step
    encrypted = base64.b64encode(aes.encrypt(plaintext))
    #prinitng Ciphertext
    #print(encrypted)
        
    return encrypted

def generate(plaintext):
    #intial QRCode
    qr = QRCode(version=2, error_correction=ERROR_CORRECT_H)
    #adding the encrypted data to QRcode
    data = encryptingqrcode(plaintext)
    qr.add_data(data)
    # Generate the QRCode itself
    qr.make()
    #im contains a PIL.Image.Image object
    im = qr.make_image(fit=True)
    # Saving the qrcode image
    im.save("adhaaaaam2.png")


