#!/usr/bin/env python3
#shebang line for linux / mac

from copy import deepcopy
import cv2 # import the opencv Library
import numpy as np

# main function, where our code should be
def main():
    print("python main function")

    # Reading the image from disk
    original_image = cv2.imread('Aula_2\Ex1\lake.png', cv2.IMREAD_COLOR)
    if original_image is None:
        print("Erro: imagem não encontrada!")
        return

    # Make the image darker on the right hand side
    h, w, channels = original_image.shape
    middle_width = round(w / 2)

    # fatores de 1 até 0 (100 passos)
    factors = np.linspace(1, 0, 100)
    print('factors = ' + str(factors))

    # começa com uma cópia da original
    image = deepcopy(original_image)

    for factor in factors: # progressive nightfall
        for y in range(0, h): # iterate all rows
            for x in range(middle_width, w): # iterating cols from middle to last
                bgr = image[y, x, :]                  # pega valor atual da imagem
                bgr_darkened = bgr * factor  # aplica escurecimento
                image[y, x, :] = bgr_darkened         # substitui pixel

        cv2.imshow('Darkened', image)
        cv2.waitKey(10) # 50 ms entre frames

    # se a janela foi fechada pelo X, interrompe o loop (gpt)
        if cv2.getWindowProperty('Darkened', cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

