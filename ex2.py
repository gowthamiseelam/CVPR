from PIL import Image,ImageDraw
img=Image.open('image.jpeg')
draw=ImageDraw.Draw(img)
draw.rectangle(xy=(100,100,500,500),
               fill=(255,255,10),
               outline=(255,255,255),
               width=40)
img.show()


