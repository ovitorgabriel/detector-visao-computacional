import cv2 #importa a biblioteca OpenCV para gerar as imagens

imagem = cv2.imread('imagem.jpg') # lê a imagem do arquivo e armazena na variável 'imagem'

imagem = cv2.resize(imagem, (640, 480)) # Redimensiona a imagem para 640x480 pixels

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # Converte a imagem para preto e branco

bordas = cv2.Canny(cinza, 100, 200) # Detecta as bordas da imagem usando o algoritmo Canny
# O primeiro parâmetro tem sensibilidade mínima de 100 e o segundo parâmetro tem sensibilidade máxima de 200

cv2.imwrite('imagem_bordas.jpg', bordas) # Salva a imagem com as bordas detectadas em um novo arquivo chamado 'imagem_bordas.jpg'

contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Encontra os contornos das bordas detectadas

cv2.drawContours(imagem, contornos, -1, (0, 0, 255), 2) # Desenha os contornos encontrados na imagem original com a cor vermelha e espessura de 2 pixels

cv2.imwrite('imagem_com_contornos.jpg', imagem) # Salva a imagem com os contornos desenhados em um novo arquivo chamado 'imagem_com_contornos.jpg'

cv2.imshow('Imagem Original', imagem) # Mostra a imagem original em uma janela com o título 'Imagem Original'
cv2.imshow('Imagem Preto e Branco', cinza) # Mostra a imagem em preto e branco em uma janela com o título 'Imagem Preto e Branco'
cv2.imshow('Bordas Detectadas', bordas) # Mostra as bordas detectadas em uma janela com o título 'Bordas Detectadas'

cv2.waitKey(0) # Aguarda o comando através do teclado para fechar as janelas
cv2.destroyAllWindows() # Fecha as janelas das imagens após o comando recebido

print('original:', imagem.shape) # Imprime a matriz de pixels da imagem original no console
print('cinza:', cinza.shape) # Imprime a matriz de pixels da imagem em preto e branco no console
print('bordas:', bordas.shape) # Imprime a matriz de pixels da imagem com as bordas detectadas no console
