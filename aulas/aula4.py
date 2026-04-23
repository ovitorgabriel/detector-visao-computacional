import cv2 #importa a biblioteca OpenCV para gerar as imagens
import numpy as np #importa a biblioteca NumPy para modificar as matrizes de pixels das imagens

# Carrega a imagem 'frutas.jpg' e redimensiona para 640x480 pixels
imagem = cv2.imread('frutas.jpg')
imagem = cv2.resize(imagem, (640, 480))

imagem1 = cv2.imread('frutas.jpg') # Carrega a imagem 'frutas.jpg' novamente para comparação
imagem1 = cv2.resize(imagem1, (640, 480)) # Redimensiona a imagem para 640x480 pixels

# Converte a imagem para preto e branco para facilitar a detecção de bordas
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplica o algoritmo Canny para detectar as bordas na imagem em preto e branco
bordas = cv2.Canny(cinza, 30, 120)

kernel = np.ones((3, 3), np.uint8) # Cria um kernel de 5x5 para a operação de dilatação
bordas = cv2.dilate(bordas, kernel, iterations=1) # Aplica a dilatação para fortalecer as bordas detectadas

# Detecta os contornos das bordas encontradas na imagem usando o método findContours
contornos, hierarquia = cv2.findContours(
    bordas,
    cv2.RETR_EXTERNAL, # Recupera apenas os contornos externos
    cv2.CHAIN_APPROX_SIMPLE # Aproxima os contornos para reduzir o número de pontos e economizar memória
)
contador = 0 # Inicializa um contador para contar os objetos detectados

contornos_grandes = [] # Cria uma lista vazia para armazenar os contornos grandes

for contorno in contornos: # Itera sobre cada contorno encontrado
    area = cv2.contourArea(contorno) # Calcula a área do contorno usando a função contourArea
    if area > 250: # Verifica se a área do contorno é maior que 250 pixels
        contador += 1 # Se for, incrementa o contador de objetos detectados
        contornos_grandes.append(contorno) # Adiciona o contorno à lista de contornos grandes

print('Quantidade de objetos detectados:', contador) # Imprime a quantidade de objetos detectados
print('Área do último contorno processado:', area) # Imprime a área do último contorno processado

# Desenha os contornos encontrados na imagem original usando a cor verde e uma espessura de 2 pixels
cv2.drawContours(imagem, contornos_grandes, -1, (0, 255, 0), 2)

# (0, 255, 0) representa a cor verde no formato BGR (Blue, Green, Red)
# (, 2 ) representa a espessura da linha e pode ser ajustada para 3 ou 4 para linhas mais grossas

# Exibe a imagem com contornos e a original em janelas separadas
cv2.imshow('Contornos', imagem)
cv2.imshow('Original', imagem1)

# Aguarda o usuário pressionar uma tecla para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
