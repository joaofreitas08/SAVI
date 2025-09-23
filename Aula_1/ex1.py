import cv2

def main():
    print("Python main function")

    # Carregar a imagem em escala de cinza
    image = cv2.imread("Aula_1/Images/im.png", cv2.IMREAD_COLOR)

    # Verificar se a imagem foi carregada
    if image is None:
        print("Erro: imagem não encontrada!")
        return

    # Info da imagem
    print(type(image))
    print("dtype =", image.dtype)
    print("shape =", image.shape)  # (183, 275)

    # Pegar a cor do pixel no canto superior esquerdo
    color = image[0, 0]
    print("Color of the top-left most pixel =", color)

    # Criar retângulos dentro do tamanho válido
    image[150:180, 0:275] = 255   # faixa branca no rodapé
    image[0:183, 50:90] = 100     # faixa cinza vertical

    #como separar r,g,b

    

    # Mostrar imagem
    cv2.imshow("My window name", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()




