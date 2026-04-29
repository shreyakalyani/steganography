import stepic
from PIL import Image 
from cryptography.fernet import Fernet

print("*-----------------------------*")


key = Fernet.generate_key()
print(key)
enc = Fernet(key)

text = input("DATA : ")
text_enc = enc.encrypt(text.encode())
file = input("PHOTO : ")

img = Image.open(file)
img_stegano = stepic.encode(img , text_enc)

img_stegano.save("stegano.png")

print("*-----------------------------*")

input("COMPLETE(press enter --> exit)")