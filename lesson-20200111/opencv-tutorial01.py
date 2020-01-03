import cv2

src = cv2.imread('senba-takako-profile.jpg')
cv2.namedWindow("imput image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("imput image", src)
cv2.waitKey(0)
cv2.destroyAllowWindows()

print("Hi, 膳場貴子")
