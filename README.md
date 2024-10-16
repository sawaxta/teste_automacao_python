# Automação de Validação de CNPJs
Este projeto implementa uma automação para validação de CNPJs usando o site da 4Devs. O programa recebe uma lista de CNPJs de um arquivo CSV, realiza a consulta para verificar a autenticidade de cada CNPJ, e retorna no terminal se o CNPJ é válido ou inválido. Além disso, o arquivo CSV é atualizado com o status de cada CNPJ.

Requisitos
Para executar o código, você precisará das seguintes bibliotecas Python:

pandas: Para manipulação e leitura de arquivos CSV.
pyautogui: Para automação de interações com o navegador e simulação de teclado/mouse.
pyperclip: Para copiar e colar textos durante a automação.
Você pode instalar as dependências executando o seguinte comando:

bash
Copiar código
pip install pandas pyautogui pyperclip
Como executar
Clone o repositório ou baixe o código.

Prepare um arquivo CSV com uma coluna chamada cnpj, contendo os CNPJs que deseja validar.

Execute o script Python conforme o exemplo abaixo:

bash
Copiar código
python validar_cnpj.py
O script abrirá o navegador automaticamente, acessará o site da 4Devs e validará os CNPJs fornecidos.

Verifique os resultados:

O terminal exibirá uma lista dos CNPJs válidos e inválidos.
O arquivo CSV original será atualizado com uma nova coluna chamada status, indicando se o CNPJ é "válido" ou "inválido".
Tecnologias Utilizadas
Python: Linguagem de programação principal.
pandas: Biblioteca para manipulação de dados e leitura de arquivos CSV.
pyautogui: Biblioteca usada para automação das interações com o navegador.
pyperclip: Biblioteca utilizada para copiar o resultado da validação do site.
Observações
O código foi desenvolvido para ser simples e eficiente, simulando interações reais com o site. A precisão da automação depende da resolução da tela e da posição dos elementos no site.
Certifique-se de que a tela e as coordenadas de clique estejam ajustadas corretamente para o seu ambiente.





Você disse:
pode reescrever todo em markdown? 
O ChatGPT disse:
ChatGPT
markdown
Copiar código
# Automação de Validação de CNPJs

Este projeto implementa uma automação para validação de CNPJs usando o site da 4Devs. O programa recebe uma lista de CNPJs de um arquivo CSV, realiza a consulta para verificar a autenticidade de cada CNPJ e retorna no terminal se o CNPJ é válido ou inválido. Além disso, o arquivo CSV é atualizado com o status de cada CNPJ.

## Requisitos

Para executar o código, você precisará das seguintes bibliotecas Python:

- `pandas`: Para manipulação e leitura de arquivos CSV.
- `pyautogui`: Para automação de interações com o navegador e simulação de teclado/mouse.
- `pyperclip`: Para copiar e colar textos durante a automação.

Você pode instalar as dependências executando o seguinte comando:

```bash
pip install pandas pyautogui pyperclip
Como executar
Clone o repositório ou baixe o código.

Prepare um arquivo CSV com uma coluna chamada cnpj, contendo os CNPJs que deseja validar.

Execute o script Python conforme o exemplo abaixo:

bash
Copiar código
python validar_cnpj.py
O script abrirá o navegador automaticamente, acessará o site da 4Devs e validará os CNPJs fornecidos.

Verifique os resultados:

O terminal exibirá uma lista dos CNPJs válidos e inválidos.
O arquivo CSV original será atualizado com uma nova coluna chamada status, indicando se o CNPJ é "válido" ou "inválido".
Tecnologias Utilizadas
Python: Linguagem de programação principal.
pandas: Biblioteca para manipulação de dados e leitura de arquivos CSV.
pyautogui: Biblioteca usada para automação das interações com o navegador.
pyperclip: Biblioteca utilizada para copiar o resultado da validação do site.
Observações
O código foi desenvolvido para ser simples e eficiente, simulando interações reais com o site. A precisão da automação depende da resolução da tela e da posição dos elementos no site.
Certifique-se de que a tela e as coordenadas de clique estejam ajustadas corretamente para o seu ambiente.
