# Sorting Hat

Diante de uma situação ocorrida no sétimo semestre da minha graduação, em que a turma, diante da divisão da sala em
grupos com temas pré-selecionados para apresentação de seminários, decidiu que gostaria de selecionar o interesse
nos grupos pelos temas, e não pelas pessoas que o compunham, estivemos frente a um grande problema: como distribuir
as pessoas nos grupos, de acordo com as preferências de temas, sem passar horas tentando encontrar uma configuração
de grupo-pessoas que pudesse priorizar a primeira opção de cada um?

## Preparando o ambiente

Para utilizar o projeto aqui presente, você deve ter instalado o **Python 3.8.+** e configurar o ambiente virtual.
Caso você não conheça e não saiba como configurar, sugiro a leitura:
[venv— Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html).

Com o ambiente virtual criado e ativado, você pode instalar as bibliotecas utilizadas no projeto usando:

```
pip install -r requirements.txt
```

As bibliotecas (e suas respectivas versões) estão listadas no arquivo `requirements.txt`.

Você vai precisar também de um diretório chamado `files`, que você deve criar na raiz do projeto. Dentro dele,
crie/coloque o arquivo com as informações a serem processadas. O arquivo deve se chamar `arquivo.csv`, e seguir o
seguinte padrão de colunas:

| Nome ou apelido 	| Tema de preferência               	| Tema alternativo         	|
|-----------------	|-----------------------------------	|--------------------------	|
| João            	| Relações Escola e Cultura Popular 	| Medicalização (TOD/TDAH) 	|

> O projeto segue o padrão de escolha de 2 temas por aluno, sendo um preferencial e outro alternativo.

Utilize a **vírgula como o caracter de separação**.

Com tudo isso pronto, você pode executar.

## Executando

Para executar o projeto, utilize o arquivo `main.py`:

```
python main.py
```

Ao final da execução, será exibido no console o resultado, e ele também será salvo em um arquivo de nome
`arquivo_resultados.csv` dentro do diretório `files`.