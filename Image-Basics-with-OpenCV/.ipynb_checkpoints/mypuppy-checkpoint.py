import cv2
img=cv2.imread(r"C:\Users\DELL\Desktop\Computer-Vision-with-OpenCV-and-Deep-Learning\Numpy\00-puppy.jpg")

while True:
    cv2.imshow("Puppy",img)
    if cv2.waitkey(1) & 0xFF==27:
        break
        
cv2.destroyAllWindows()