
import numpy as np
import cv2


def extract_signature(raw_image):
    nparr = np.fromstring(raw_image, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([90, 38, 0])
    upper = np.array([145, 255, 255])
    mask = cv2.inRange(image, lower, upper)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

    cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    boxes = []
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        boxes.append([x,y, x+w,y+h])

    boxes = np.asarray(boxes)
    left = np.min(boxes[:,0])
    top = np.min(boxes[:,1])
    right = np.max(boxes[:,2])
    bottom = np.max(boxes[:,3])

    result[close==0] = (255,255,255)
    ROI = result[top:bottom, left:right].copy()
    cv2.rectangle(result, (left,top), (right,bottom), (36, 255, 12), 2)

    # ===| Hanle Background Transparent |===
    # https://stackoverflow.com/a/55675125/2670847
    h, w, c = ROI.shape
    # append Alpha channel -- required for BGRA (Blue, Green, Red, Alpha)
    ROI_TRANS = np.concatenate([ROI, np.full((h, w, 1), 255, dtype=np.uint8)], axis=-1)
    # create a mask where white pixels ([255, 255, 255]) are True
    white = np.all(ROI == [255, 255, 255], axis=-1)
    # change the values of Alpha to 0 for all the white pixels
    ROI_TRANS[white, -1] = 0

    # ======================================

    # cv2.imshow('result', result)
    # cv2.imshow('ROI', ROI)
    # cv2.imshow('ROI_TRANS', ROI_TRANS)
    # cv2.imshow('close', close)
    # cv2.imwrite('result.png', result)
    # cv2.imwrite('ROI.png', ROI)
    # cv2.imwrite('ROI_TRANS.png', ROI_TRANS)
    # cv2.imwrite('ROI_TRANS_COMPRESSED.png', ROI_TRANS, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    # cv2.waitKey()
    return cv2.imencode('.png', ROI_TRANS)[1].tobytes()
