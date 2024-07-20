import numpy as np
import keras
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D
from keras.preprocessing import image
from PIL import Image

# Função para carregar e processar a imagem personalizada
def carregar_e_processar_imagem(caminho_imagem, tamanho):
    # Carregar a imagem
    img = Image.open(caminho_imagem).convert('L')  # Converter para cinza
    img = img.resize(tamanho)  # Redimensionar para 500x500 pixels
    img_array = np.array(img)  # Converter para array numpy
    img_array = img_array.astype('float32') / 255  # Normalizar
    img_array = img_array.reshape((1, tamanho[0], tamanho[1], 1))  # Adicionar dimensão de lote
    return img_array

# Carregar e processar uma imagem personalizada
caminho_imagem = 'img\spider-man.jpg'
imagem_personalizada = carregar_e_processar_imagem(caminho_imagem, tamanho=(500,500))

# Modelo para detecção de bordas
classificador = Sequential()

# Filtro de Sobel horizontal
horizontal = np.array([[-1, -2, -1],
                       [ 0,  0,  0],
                       [ 1,  2,  1]], dtype='float32')

# Filtro de Sobel vertical
vertical = np.array([[-1,  0,  1],
                     [-2,  0,  2],
                     [-1,  0,  1]], dtype='float32')

# Adicionar filtros como camadas Conv2D
classificador.add(Conv2D(1, (3, 3), input_shape=(500,500, 1), use_bias=False,
                         kernel_initializer=keras.initializers.Constant(horizontal.reshape((3, 3, 1, 1)))))
classificador.add(Conv2D(1, (3, 3), use_bias=False,
                         kernel_initializer=keras.initializers.Constant(vertical.reshape((3, 3, 1, 1)))))

# Compilar o modelo
classificador.compile(loss='mean_squared_error', optimizer='adam')

# Detecção de borda no teste
edges = classificador.predict(imagem_personalizada)

# Ampliação de contraste para bordas detectadas
fator_escala = 2.0
edges_ampliadas = np.clip(edges * fator_escala, 0, 1)

# Visualizar imagem de teste e bordas detectadas
plt.figure(figsize=(15, 10))

plt.subplot(1, 2, 1)
plt.imshow(imagem_personalizada[0].reshape(500, 500), cmap='gray')
plt.title('Imagem Original')

plt.subplot(1, 2, 2)
plt.imshow(edges_ampliadas[0].reshape(496, 496), cmap='gray')
plt.title('Bordas Ampliadas')

plt.show()
