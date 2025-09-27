#!/usr/bin/env python3
import cv2
import numpy as np

def main():
    print("python main function")

    # --------------------------
    # Read image
    # --------------------------
    image_filename = 'Aula_2/Ex6/scene.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)

    template_filename = 'Aula_2/Ex6/wally.png'
    template = cv2.imread(template_filename, cv2.IMREAD_COLOR)
    h, w, numchannels = template.shape

    # Apply template Matching
    result = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print('max_loc = ' + str(max_loc))

    # Get coordinates of Wally
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Criar versão a preto e branco da imagem
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # converter para 3 canais

    # Copiar a região do Wally a cores para cima da imagem cinzenta
    roi_color = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]  #wally cima vaixo. esquerda direita
    gray_bgr[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = roi_color #colocar roi_color por cima de gray bgr

    # Mostrar resultado
    cv2.imshow('Scene with Wally Highlighted', gray_bgr)
    cv2.imshow('Template', template)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
