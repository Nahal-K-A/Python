import cv2 as cv


def rescaleFrame(frame, scale):  # works fro images, videos, and LIVE videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# ___IMAGE RESCALING___
img = cv.imread("Images/Spiderman.jpg")
# cv.imshow("Image", img)

resized_img = rescaleFrame(img, scale=0.4)
cv.imshow("resized Image", resized_img)
cv.waitKey(0)


def changeRes(width, height):  # works for LIVE videos
    vid.set(3, width)
    vid.set(4, height)


# ___VIDEO RESCALING___
vid = cv.VideoCapture("Vids/bird.mp4")

while True:
    isTrue, frame = vid.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    # cv.imshow("Video", frame)
    cv.imshow("video Resized", frame_resized)
    if cv.waitKey(17) & 0xFF == ord("d"):
        break
