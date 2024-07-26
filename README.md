Projeto de álgebra linear sobre implementação de esteganografia e criptografia em imagens, desenvolvido no curso de Ciência da Computação da Universidade Federal de Rondônia 


- [x] Conversão de mensagem em texto para binário (ASCII)
- [x] Identificar canal de cor mais adequado (~~o que gera menos mudancas de bit, ou~~ o que tem menor contribuicao na imagem?)
- [x] Isolar canal de cor ideal da imagem
- [x] Criar lógica de iteração da imagem baseado na senha (hashing)
- [x] Usar a lógica de iteração para manipular o canal de cores
- [x] Aplicar o canal de cores manipulado na imagem original
- [x] Usar a lógica de iteração para recuperar a mensagem binária
- [x] Reverter a mensagem binária para ASCII
- [x] Interface gráfica pra codificar e decodificar sem usar o terminal

👍👍👍

Como usar (Linux CLI):<br>

(Clonagem do repositório)<br>
  git clone https://github.com/sdsamih/HideInBit<br>
  cd HideInBit<br>

(Opcional, criação do virtual enviroment):<br>
  python3 -m venv venv <br>
  source venv/bin/activate <br>
  
(Instalação das dependências)<br>
  pip install -r requirements.txt<br>

(Inicialização do programa)<br>
  cd interface<br>
  python3 app.py<br>

No navegador, acesse http://127.0.0.1:5000<br>







