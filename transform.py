
import cv2
import numpy as np

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    # top-left top-right bottom-right bottom-left
    for i in range(len(pts)):
        rect[i] = pts[i]

    """
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]		#top-left
    rect[2] = pts[np.argmax(s)] 	#bottom-right

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]	#top-right
    rect[3] = pts[np.argmax(diff)]	#bottom-left
    """
    return rect


def perspective_transformation(img, pts):
    # get ordered points and unpack them
    rect = order_points(pts)
    (tl, tr, bl, br) = rect

    # compute width of new image
    # distance between topmost two points
    widthT = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
    # distance between bottommost two points
    widthB = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)

    # compute height
    # distance between leftmost points
    heightL = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    # distance between rightmost points
    heightR = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)

    # find max height and width
    maxWidth = max(int(widthB), int(widthT))
    maxHeight = max(int(heightL), int(heightR))

    print('width:' + str(maxWidth))
    print('height:' + str(maxHeight))

    dst = np.float32([[0, 0],
                      [maxWidth - 1, 0],
                      [maxWidth - 1, maxHeight - 1],
                      [0, maxHeight - 1]])

    # compute perspective transform matrix
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))

    return warped