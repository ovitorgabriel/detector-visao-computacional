import cv2 # Importa a biblioteca OpenCV para gerar as imagens

imagem = cv2.imread('imagem.jpg') # Vai ler a imagem do arquivo e armazenar na variável 'imagem'

cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL) # Cria uma janela redimensionável para a imagem original
cv2.resizeWindow('Imagem Original', 600, 600) # Redimensiona a janela da imagem original para 600x400 pixels

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # Converte a imagem para preto e branco

cinza = cv2.resize(cinza, (600, 600)) # Redimensiona a imagem original para 600x400 pixels

print('Original:', imagem.shape) # Imprime a matriz de pixels da imagem original no console
print('Preto e Branco:', cinza.shape) # Imprime a matriz de pixels da imagem

cv2.imshow('Imagem Original', imagem) # Mostra a imagem original em uma janela com o título 'Imagem Original'
cv2.imshow('Imagem Preto e Branco', cinza) # Mostra a imagem em tons de cinza em uma janela com o título 'Imagem Preto e Branco'

cv2.imwrite('imagem_cinza.jpg', cinza) # Salva a imagem em preto e branco em um novo arquivo chamado 'imagem_cinza.jpg'

cv2.waitKey(0) # Aguarda o comando através do teclado para fechar as janelas
cv2.destroyAllWindows() # Fecha as janelas das imagens após o comando recebido