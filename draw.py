import cv2 as cv
import numpy as np

# can use already available image. creating a new blank image here
blank = np.zeros((500, 500, 3), dtype="uint8")

# 1. Paint the image a certain colour
# blank[:] = 0, 0, 255  # BGR
# painting a certain part of the image
blank[200:300, 200:300] = 0, 0, 255  # [row:row, column:column]
cv.imshow("Red", blank)

# 2. Draw a rectangle
cv.rectangle(
    blank, (200, 200), (300, 300), (255, 0, 0), thickness=2
)  # thickness=-1 or thickness=cv.FILLED for filling the rectangle
cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(
    blank, (blank.shape[0] // 2, blank.shape[1] // 2), 50, (0, 255, 0), thickness=-1
)
cv.imshow("circle", blank)

# 4. Draw a line
cv.line(blank, (250, 0), (250, 500), (255, 255, 255), thickness=2)
cv.imshow("line", blank)

# 5. Write text
cv.putText(
    blank, "Hello", (50, 300), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 5, (255, 255, 255), 2
)
cv.imshow("Text", blank)

cv.waitKey(0)
