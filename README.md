# APS 3

# Integrantes

- Luis Felipe(SocratesMorreu) e Caio Frigerio Liberal (Caiolib)

# Projeto de Efeitos de Vídeo em Tempo Real

Este projeto é um processador de efeito de vídeo em tempo real que realiza a rotação da imagem de vídeo capturada pela webcam do usuário, simulando um efeito de "girar" contínuo na tela. A rotação ocorre ao redor do centro da imagem, e a velocidade de rotação pode ser ajustada interativamente.

# Como Executar

- Para rodar o programa demo.py, siga os seguintes passos:

- Para rodar o demo é necessário ter o python instalado na maquina, caso não tenha, baixe o python em https://www.python.org/downloads/
- Installe o arquivo zip no GitHub
- Acesse a pasta do demo com o comando "cd" no terminal
- Instale as dependências necessárias usando o comando: "pip install -r requirements.txt"
- Use o comando "python demo.py" ou "python3 demo.py" para executar o programa

# Funcionalidades do programa 

- Inicialmente, o porgrama vai rotacionar a imagem em sentido anti-horario, rotacionando uniformimente
- a tecla 'w' aumenta a velocidade de rotacao no sentido anti-horario
- a tecla 'e' aumenta a velocidade de rotacao no sentido horario
- a tecla 's' aumenta o cisalhamento aplicado na imagem
- a tecla 'd' diminue o cisalhamento aplicado na imagem
- a tecla 'q' faz com que o usuario termine o programa 

# Modelo Matemático Implementado

O processo de rotação é alcançado através da aplicação de transformações lineares sobre os pixels da imagem capturada. Cada pixel é tratado como um ponto em um espaço bidimensional, e uma série de transformações é aplicada para rotacionar esse ponto ao redor do centro da imagem.

As transformações utilizadas incluem:

- Translação: A translação foi feita a partir da matriz T, que é multiplicada na matriz final para que a rotação ocorra no centro da tela ao invez da origem do plano carteziano(0,0)
- Rotação: a rotação foi aplicada a partir da matriz R = [[cos(θ), -sin(θ), 0], [sin(θ), cos(θ), 0], [0, 0, 1]], onde (θ) é o ângulo de rotação em radianos. Multiplicamos essa matriz na matriz final para rotaciona-la. Além disso, mudamos o angulo de rotação, alterando o θ dentro da matriz 
- Cisalhamento: o cisalhamento doi deito a partir da matriz C = [1, distorcer_imagem, 0], [distorcer_imagem, 1, 0], [0, 0, 1], aonde o usuario pode alterar o argumento 'distorcer_imagem' para aumentar ou diminuir o cisalhamento
- Translação inversa: multiplicamos o inverso da matriz resultante dos das transformções, A por Xd  para mapear os pontos da imagem transformada de volta aos pontos correspondentes na imagem original, assegurando a correta atribuição dos pixels e evitando artefatos, isto é, distorções na imagem final.

A combinação dessas transformações é realizada por meio do cálculo da matriz composta A, que é aplicada a cada pixel da imagem. Além disso, para evitar artefatos na imagem resultante, a transformação inversa A^{-1} é utilizada para mapear os pixels da imagem de destino de volta para a imagem original.
