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

Como usar (Linux CLI):

(Clonagem do repositório)
  git clone https://github.com/sdsamih/HideInBit
  cd HideInBit

(Opcional, criação do virtual enviroment):
  python3 -m venv venv 
  source venv/bin/activate 
  
(Instalação das dependências)
  pip install -r requirements.txt

(Inicialização do programa)
  cd interface
  python3 app.py

No navegador, acesse http://127.0.0.1:5000







