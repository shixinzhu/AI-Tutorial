import cv2
import numpy as np

def cmaera_handle():
	capture = cv2.VideoCapture(0)
	while(True):
		ret, frame = capture.read()
		cv2.flip(frame, 1) # 调整左右位置
		cv2.imshow("camera", frame)
		cv2.imwrite('fastbit-tech.png', frame)
		c = cv2.waitKey(50)
		if c == 27:           # ESC
			break 

def show_img_info(image):
    print(type(image))        # 打印图片在内存中的类型
    print(image.shape)
    print(image.size)          # 注意这个数字的来源 481 *  457 * 3
    print(image.dtype)
    print(np.array(image))

src = cv2.imread('senba-takako-profile.jpg')
cv2.namedWindow("imput image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("imput image", src)
show_img_info(src)
cmaera_handle()

cv2.waitKey(0)
cv2.destroyAllowWindows()

print("Hi, 膳場貴子")
