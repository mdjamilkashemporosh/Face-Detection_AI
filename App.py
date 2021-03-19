import cv2

# Choose an Image to Detect Face
img = cv2.imread('./image.jpg')

# Convert Image into GreyScale
greyScaled_Img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show Image 
cv2.imshow('Face Detection',greyScaled_Img)

# Waition for an Action
cv2.waitKey()
  



print("Code Compiled Successfully")
