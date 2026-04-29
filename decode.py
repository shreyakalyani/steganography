import stepic 
from PIL import Image

print("*-----------------------------*")

file = input("PHOTO : ")
img = Image.open(file)
decoded = stepic.decode(img)

print("DATA is : "+ str(decoded))

print("*-----------------------------*")