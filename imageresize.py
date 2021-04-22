import PIL
from PIL import Image
width=300
height=300
img=Image.open('ash.jpg')
img=img.resize((width,height),PIL.Image.ANTILIAS)
img.save('resize.jpg')
