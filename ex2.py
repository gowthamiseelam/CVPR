from PIL import Image,ImageDraw
img=Image.open('image.jpeg')
draw=ImageDraw.Draw(img)
draw.rectangle(xy=(100,100,500,500),
               fill=(255,255,10),
               outline=(255,255,255),
               width=40)
img.show()

import cv2
img=cv2.imread('image.jpeg')
wind_name='shape'
image=cv2.rectangle(img,(50,50),(150,150),(255,255,0),10)
cv2.imshow(wind_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()

