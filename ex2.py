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


img=cv2.imread('image.jpeg')
wind_name='Resize'
image=cv2.resize(img,(500,500))
cv2.imshow("original",img)
cv2.imshow(wind_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows() 


img=cv2.imread('image.jpeg')
wind_name='rotate'
image=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("original",img)
cv2.imshow(wind_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows() 


import cv2

haar_file = 'haarcascade_frontalface_default.xml'
img_path = 'face1.jpg' 

image = cv2.imread(img_path)
image=cv2.resize(image,(500,500))

if image is None:
    print("Image not loaded correctly. Please check the file path.")
else:
    face_cascade = cv2.CascadeClassifier(haar_file)

    if face_cascade.empty():
        print("Haar Cascade file could not be loaded. Please check the file path.")
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('Detected Faces', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


