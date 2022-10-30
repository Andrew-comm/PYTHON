from PIL import  Image
im = Image.open("/home/andrea/Pictures/Screenshots/Screenshot from 2022-09-30 01-12-21.png")
new_im = im.rotate(90)
new_im.save("/home/andrea/Pictures/Screenshots/Screenshot from 2022-09-30 01-12-21-rotated.png")