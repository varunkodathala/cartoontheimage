import cv2
import numpy as np 

img = cv2.imread('/Users/varun/Documents/cartoon_effect/vizag.jpg')
img = cv2.resize(img,(720,360))


gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_edges = cv2.Canny(gray_img,127,255)
gray_thresh = cv2.adaptiveThreshold(gray_img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,20)


color_smooth = cv2.bilateralFilter(img,9,300,300)

color = cv2.bitwise_and(color_smooth,color_smooth,mask = gray_thresh)

x = img.shape[0]
y = img.shape[1]

final_image = np.zeros((2*x,y,3),np.uint8)

final_image[:x,:,:] = img
final_image[x:,:,:] = color

cv2.imwrite('final_image.jpg',final_image)
cv2.imshow("Final",final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
