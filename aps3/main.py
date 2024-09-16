import numpy as np
import cv2 as cv
import math
import itertools

def criar_indices(min_i, max_i, min_j, max_j):
    '''
    Essa função gera uma matriz de coordenadas para cada pixel da imagem
    *função que implementada no handout 03.geometria_analitica
    '''
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack((idx_i, idx_j))
    return idx

def run():
    
    cap = cv.VideoCapture(0)

    #tamanho da tela 
    width = 300
    height = 300

    #angulo inicial de rotação
    angulo = 0 

    #velocidade inicial de rotacao (variavel para modificar o quao rapito vai rotacionar)
    velocidade_parcial = 0
    #distorcao inicial da imagem (variavel para distorcer a imagem)
    distorcer_imagem = 0 

    #caso nao consiga abrir a camera
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não consegui capturar frame!")
            break
        
        #para pegar a tecla que o usuario interagir
        key = cv.waitKey(1)

        #redimencionando a imagem para as especificacoes dadas 
        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
        image = np.array(frame).astype(float) / 255
        image_ = np.zeros_like(image)

        Xd = criar_indices(0, width, 0, height)
        Xd = np.vstack((Xd, np.ones(Xd.shape[1])))

        #aumenta a velocidade do que a imagem vai rotacionar - sentido horario
        if key == ord('w'):
            velocidade_parcial += 1
        
        #aumenta a velocidade do que a imagem vai rotacionar - sentido anti-horario
        if key == ord('e'):
            velocidade_parcial -= 1

        #aumentar cisalhamento
        if key == ord('s'):
            distorcer_imagem += 0.15
        
        #diminuir cisalhamento
        if key == ord('d'):
            distorcer_imagem -= 0.15

        #a cada vez que o loop roda, o angulo aumenta em um, fazendo com que a imagem rotacione inicialmente uniformimente no sentido anti-horario
        angulo += 1 + velocidade_parcial
        angulo_radianos = math.radians(angulo) #transformando o angulo em radianos

        #matriz de translação para rotacionar a imagem no centro da tela e não na origem (0,0)
        T = np.array([[1, 0, -150], [0, 1, -150], [0, 0, 1]]) 
        #matriz de rotacao da imagem 
        R = np.array([[math.cos(angulo_radianos), -math.sin(angulo_radianos), 0], [math.sin(angulo_radianos), math.cos(angulo_radianos), 0], [0, 0, 1]]) 
        #matriz de cisalhamento da imagem 
        C = np.array( [[1, distorcer_imagem, 0], [distorcer_imagem, 1, 0], [0, 0, 1]]) 
        T_inv = np.linalg.inv(T) #invertendo a matriz T

        #aplicando as transformacoes na matriz A
        A = T_inv @ R @ C @ T 
        #multiplicacao pelo inverso de A, para garantir que todos os pixels sejam aplicados correntamente na imagem
        A_ = np.linalg.inv(A) @ Xd

        #convertendo as coordenadas para valores inteiros
        Xd = Xd.astype(int) 
        A_ = A_.astype(int)

        #aplicando um filtro para apenas mostrar os pixels dentro das limitacoes da tela(300,300)
        filtro = (A_[0,:] >= 0) & (A_[1,:] >= 0) & (A_[0,:] < 300) & (A_[1,:] < 300) 
        Xd = Xd[:,filtro]
        A_ = A_[:,filtro]

        #para dar display na imagem
        A_[0, :] = np.clip(A_[0, :], 0, image.shape[0] - 1) 
        A_[1, :] = np.clip(A_[1, :], 0, image.shape[1] - 1)
        image_[Xd[0, :], Xd[1, :], :] = image[A_[0, :], A_[1, :], :]

        cv.imshow('Minha Imagem!', image_)

        #o usuario aperta 'q' para parar o programa 
        if key == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

run()
