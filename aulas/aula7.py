import cv2 #importa a biblioteca OpenCV para gerar as imagens
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_DIR, '..', 'imagens', 'input', 'frutas.jpg')

imagem = cv2.imread(IMG_PATH) # Carrega a imagem 'frutas.jpg'

texto = 'Frutas' # Define o texto a ser adicionado à imagem

cv2.putText( #cv2.putText() é a função usada para adicionar texto à imagem. Os parâmetros são: imagem, texto, posição do texto, fonte, escala, cor e espessura)
    imagem, 
    texto,
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)

cv2.imshow('Imagem com Texto', imagem) # Exibe a imagem com o texto adicionado em uma janela
cv2.imwrite(os.path.join(BASE_DIR, '..', 'imagens', 'output', 'frutas_com_texto.jpg'), imagem) # Salva a imagem com o texto adicionado em um novo arquivo chamado 'frutas_com_texto.jpg'

cv2.waitKey(0) # Aguarda o usuário pressionar uma tecla para fechar a
cv2.destroyAllWindows() # Fecha todas as janelas abertas