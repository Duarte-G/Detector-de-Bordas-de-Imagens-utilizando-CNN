# Detector de Bordas de Imagens utilizando Redes Neurais Convolucionais
Como parte do estudo sobre reconhecimento de imagens, desenvolvi um modelo para detecção de bordas usando filtros de Sobel, incorporando conceitos de redes neurais convolucionais.
A detecção de bordas é uma técnica essencial no processamento de imagens, pois permite identificar mudanças significativas na intensidade dos pixels, destacando os contornos e estruturas importantes dentro da imagem.

Os filtros de Sobel aplicados são definidos da seguinte forma:
- **Filtro de Sobel Horizontal:**
<p align="center">
  <img src="https://github.com/user-attachments/assets/b5c446ce-b368-435a-ae56-7e781b23ad1c">
</p>
Detecta bordas verticais ao calcular a variação horizontal da intensidade dos pixels.

- **Filtro de Sobel Vertical:**
<p align="center">
  <img src="https://github.com/user-attachments/assets/b0a09640-51c9-4222-b86e-687f5fe6fcb3">
</p>
Detecta bordas horizontais ao calcular a variação vertical da intensidade dos pixels.

Após aplicar esses filtros à imagem, amplifiquei o contraste das bordas detectadas para tornar as bordas mais visíveis. Este processo facilita a visualização das características estruturais e contornos na imagem. 
A visualização das bordas realçadas demonstra como técnicas de filtragem podem acentuar características específicas em imagens, sendo muito importante para tarefas de processamento de imagens e aprendizado de máquina.
<p align="center">
  <img src="https://github.com/user-attachments/assets/97a7f1ce-1b5f-4248-a393-77faa37824ca">
</p>

## Como Usar
 - Clone o repositório para sua máquina local.
 - Instale as bibliotecas necessárias no código
 - Execute o .ipynb para explorar o código e resultados.
 - Sinta-se à vontade para alterar a imagem para testar outras; apenas lembre-se de redimensionar a imagem para o tamanho adequado e ajustar os parâmetros conforme necessário.
