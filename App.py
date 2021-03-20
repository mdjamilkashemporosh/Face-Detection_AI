import cv2

Trained_Face_Data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Choose an Image to Detect Face
img = cv2.imread('./image.jpg')

# Convert Image into GreyScale
greyScaled_Img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Detect Faces
Face_Cordinates = Trained_Face_Data.detectMultiScale(greyScaled_Img)

# Draw Rectangles Around the Faces 
for(x,y,w,h) in Face_Cordinates : 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# Show Image 
cv2.imshow('Face Detection',img)

# Waition for an Action
cv2.waitKey()

print("Code Compiled Successfully")
