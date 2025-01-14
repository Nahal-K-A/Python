import cv2 as cv


def rescaleFrame(frame, scale):  # works fro images, videos, and LIVE videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread("Images/Landscape.jpg")
img = rescaleFrame(img, 0.175)
cv.imshow("BGR", img)

# # Converting to greyscale
# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Greyscale", grey)

# Blur an image
blur = cv.GaussianBlur(
    img, (5, 5), cv.BORDER_DEFAULT
)  ##ksize impact the intensity of the blur. 2x2 tuple must be odd
cv.imshow("blur", blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)

cv.waitKey(0)
