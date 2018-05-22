from PIL import Image,ImageFilter

img=Image.open("sample.jpg")

img=img.rotate(-90)
img=img.convert("L")
img=img.crop((46,27,206,231))

img.thumbnail((75,75))

img.show()

str1=raw_input("enter image name")
img.save(str1+".jpg")


   