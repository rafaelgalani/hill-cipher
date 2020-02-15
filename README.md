# HILL CIPHER - EC10 - FTT - DESAFIO

## RA 082150282 - Rafael Galani
## RA 082150267 - Rafael Cardoso

A cifra de Hill é uma cifra que usa álgebra linear para codificação das mensagens. Converte-se as letras da mensagem em números, e agrupa-se os números de N em N, sendo N o tamanho da matriz quadrada utilizada como chave. Cada elemento da mensagem codificada é o produto de um agrupamento de N caracteres com a matriz escolhida. Para o caminho inverso, a decodificação, basta utilizar a matriz inversa. Portanto, é necessário que a matriz escolhida para codificar seja inversível - determinante diferente de 0.

A solução foi dada em python, as bibliotecas seguem no `requirements.txt`. Para rodar, basta abrir o arquivo `hill-cipher-ftt` com o comando `python .\hill-cipher-ftt.py`.