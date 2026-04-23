import cv2 # Importa a biblioteca OpenCV para gerar as imagens

imagem = cv2.imread('imagem.jpg') # Vai ler a imagem do arquivo e armazenar na variável 'imagem'

print(imagem) # Imprime a matriz de pixels da imagem no console

cv2.imshow('Minha Primeira Imagem', imagem) # Mostra a imagem em uma janela com o título 'Minha Primeira Imagem'

cv2.waitKey(0) # Aguarda o comando através do teclado para fechar a janela
cv2.destroyAllWindows() # Fecha a janela da imagem após o comando recebido
