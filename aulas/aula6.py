import cv2 #importa a biblioteca OpenCV para gerar as imagens
import numpy as np #importa a biblioteca NumPy para modificar as matrizes de pixels das imagens

imagem = cv2.imread('frutas.jpg') # Carrega a imagem 'frutas.jpg'
imagem = cv2.resize(imagem, (640, 480)) # Redimensiona a imagem para 640x480 pixels

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV) # Converte a imagem para o espaço de cores HSV

# vermelho faixa 1
inferior1 = np.array([0, 120, 70]) # Define o limite inferior para a cor vermelha
superior1 = np.array([10, 255, 255]) # Define o limite superior para a cor vermelha

# vermelho faixa 2
inferior2 = np.array([170, 120, 70]) # Define o limite inferior para a cor vermelha
superior2 = np.array([180, 255, 255]) # Define o limite superior para a cor vermelha

mascara1 = cv2.inRange(hsv, inferior1, superior1) # Cria uma máscara para a cor vermelha usando os limites definidos
mascara2 = cv2.inRange(hsv, inferior2, superior2) # Cria uma máscara para a cor vermelha usando os limites definidos

mascara = mascara1 + mascara2 # Combina as duas máscaras para obter a máscara final

contornos, _ = cv2.findContours(
    mascara,
    cv2.RETR_EXTERNAL, # Recupera apenas os contornos externos
    cv2.CHAIN_APPROX_SIMPLE # Aproxima os contornos para reduzir o número de pontos e economizar memória
)

contador = 0 # Inicializa um contador para contar os objetos detectados

contador_mascara = [] # Cria uma lista vazia para armazenar os contornos que atendem ao critério de área

for contorno in contornos: # Itera sobre cada contorno encontrado
    area = cv2.contourArea(contorno) # Calcula a área do contorno usando a função contourArea
    print('Área do contorno: ', area) # Imprime a área do contorno para depuração
    if 300 < area < 15000: # Verifica se a área do contorno é maior que 300 pixels e menor que 15000 pixels
        contador += 1 # Se for, incrementa o contador de objetos detectados
        contador_mascara.append(contorno) # Adiciona o contorno à lista de máscaras
        cv2.drawContours(imagem, [contorno], -1, (0, 255, 0), 2) # Desenha o contorno na imagem original usando a cor verde e uma espessura de 2 pixels

print('Quantidade de frutas vermelhas detectadas: ', contador) # Imprime a quantidade de frutas vermelhas detectadas

cv2.imshow('Imagem com Contornos', imagem) # Exibe a imagem com os contornos desenhados em uma janela
cv2.imshow('Mascara', mascara) # Exibe a máscara em uma janela

cv2.waitKey(0) # Aguarda o usuário pressionar uma tecla para fechar as janelas
cv2.destroyAllWindows() # Fecha todas as janelas abertas
