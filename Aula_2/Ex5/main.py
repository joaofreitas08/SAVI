#!/usr/bin/env python3
# shebang line for linux / mac

from copy import deepcopy
import glob
import cv2  # import the opencv library
import numpy as np

# main function, where our code should be

    # --------------------------
    # Choose Template 
    # --------------------------
def imageCrop(action, x, y, flags, *userdata):
    global tlx, tly, brx, bry
    if action == cv2.EVENT_LBUTTONDOWN:
        tlx, tly = x, y
    elif action == cv2.EVENT_LBUTTONUP:
        brx, bry = x, y
            
        cv2.rectangle(image, (tlx, tly), (brx, bry), (0, 255, 0), 2)
        cv2.imshow("display", image)

        image_crop = image[tly:bry, tlx:brx]
        cv2.imwrite('Aula_2/Ex5/image_crop.png', image_crop)


def main():

    global image #para conseguir comunicar
    # --------------------------
    # Read image
    # --------------------------
    image_filename = 'Aula_2/Ex5/school.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
    #H, W, numchannels = image.shape

    cv2.namedWindow("display")
    cv2.setMouseCallback("display", imageCrop)

    while True:
        cv2.imshow("display", image)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC para sair
            break


    template_filename = 'Aula_2\Ex5\image_crop.png'
    template = cv2.imread(template_filename, cv2.IMREAD_COLOR)
    h, w, numchannels = template.shape



    # Apply template Matching
    result = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
    #print('result = ' + str(result))
    #print('result type ' + str(result.dtype))

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print('max_loc' + str(max_loc))

    # Draw a rectange on the original image

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)

    cv2.imshow('Scene', image)
    #cv2.imshow('Template', template)
    #cv2.imshow('Result', result)
    cv2.waitKey(25)  #

    cv2.waitKey(0)  # 0 means wait forever until a key is pressed


if __name__ == '__main__':
    main()