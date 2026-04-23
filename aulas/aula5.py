import cv2 #importa a biblioteca OpenCV para gerar as imagens
import numpy as np #importa a biblioteca NumPy para modificar as matrizes de pixels das imagens

imagem = cv2.imread('frutas.jpg') # Carrega a imagem 'frutas.jpg'

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV) # Converte a imagem para o espaço de cores HSV

inferior = np.array([0, 120, 70]) # Define o limite inferior para a cor vermelha
superior = np.array([10, 255, 255]) # Define o limite superior para a cor vermelha

mascara = cv2.inRange(hsv, inferior, superior) # Cria uma máscara para a cor vermelha usando os limites definidos

resultado = cv2.bitwise_and(imagem, imagem, mask=mascara) # Aplica a máscara à imagem original para obter o resultado

imagem = cv2.resize(imagem, (640, 480)) # Redimensiona a imagem para 640x480 pixels
mascara = cv2.resize(mascara, (640, 480)) # Redimensiona a máscara para 640x480 pixels
resultado = cv2.resize(resultado, (640, 480)) # Redimensiona o resultado para 640x480 pixels

cv2.imshow('Imagem Original', imagem) # Exibe a imagem original em uma janela
cv2.imshow('Mascara', mascara) # Exibe a máscara em uma janela
cv2.imshow('Resultado', resultado) # Exibe o resultado da aplicação da máscara em uma janela

cv2.waitKey(0) # Aguarda o usuário pressionar uma tecla para fechar as janelas
cv2.destroyAllWindows() # Fecha todas as janelas abertas
