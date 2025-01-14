import cv2 as cv

# img = cv.imread("Images/Spiderman.jpg")
# cv.imshow("Spiderman", img)
# cv.waitKey(0)

vid = cv.VideoCapture("Vids/bird.mp4")
while True:
    isTrue, frame = vid.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break
