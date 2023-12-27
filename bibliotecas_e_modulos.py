import random
import datetime as dt
# Um módulo pode ser uma biblioteca de códigos, o qual possui diversas funções (matemáticas, sistema operacional, etc.) as quais possibilitam a reutilização de código de uma forma elegante e eficiente.

#import moduloXXText
#import moduloXX as apelido
#from moduloXX import itemA, itemB

#! CLASSIFICAÇÃO DOS MODULOS
# Módulos built-in: embutidos no interpretador. 
# Módulos de terceiros: criados por terceiros e disponibilizados via PyPI. 
# Módulos próprios: criados pelo desenvolvedor.

#*Módulo random - Random é um módulo built-in usado para criar números aleatórios.
print(random.randint(1, 100)) # numero aleatorio entre 1 e 100
print(random.choice([1, 2, 3])) # numero aleatorio nessa lista
print(random.sample(range(100), k = 10)) # escolhe 10 numeros aleatorios que contem no tamanho da lista

#* Módulo OS - OS é um módulo built-in usado para executar comandos no sistema operacional. Vamos explorar as funções:
# os.getcwd(): retorna uma string com o caminho do diretório de trabalho. 
# os.listdir(path='.'): retorna uma lista com todas as entradas de um diretório. Se não for especificado um caminho, então a busca é realizada em outro diretório de trabalho. 
# os.cpu_count(): retorna um inteiro com o número de CPUs do sistema. 
# os.getlogin(): retorna o nome do usário logado. 
# os.getenv(key): retorna uma string com o conteúdo de uma variável de ambiente especificada na key. 
# os.getpid(): retorna o id do processo atual.

#* Módulo RE - O módulo re (regular expression) fornece funções para busca de padrões em um texto. Uma expressão regular especifica um conjunto de strings que corresponde a ela. As funções neste módulo permitem verificar se uma determinada string corresponde a uma determinada expressão regular. Essa técnica de programação é utilizada em diversas linguagens de programação, pois a construção de re depende do conhecimento de padrões. Vamos explorar as funções:
# re.search(pattern, string, flags=0): varre a string procurando o primeiro local onde o padrão de expressão regular produz uma correspondência e o retorna. Retorna None se nenhuma correspondência é achada.
# re.match(pattern, string, flags=0): procura por um padrão no começo da string. Retorna None se a sequência não corresponder ao padrão.
# re.split(pattern, string, maxsplit=0, flags=0): divide uma string pelas ocorrências do padrão.

#Módulo Datetime - Trabalhar com datas é um desafio nas mais diversas linguagens de programação. Em Python há um módulo built-in capaz de lidar com datas e horas. O módulo datetime fornece classes para manipular datas e horas. Uma vez que esse módulo possui classes, então a sintaxe para acessar os métodos deve ser algo similar a: modulo.classe.metodo(). Dada a diversa quantidade de possibilidades de se trabalhar com esse módulo, vamos ver um pouco das classes datetime e timedelta.
#* Operações com data e hora
hoje = dt.datetime.today()
ontem = hoje - dt.timedelta(days=1)
uma_semana_atras = hoje - dt.timedelta(weeks=1)
agora = dt.datetime.now()
duas_horas_atras = agora - dt.timedelta(hours=2)
#* Formatação
hoje_formatado = dt.datetime.strftime(hoje, "%d-%m-%Y")
ontempo_formatado = dt.datetime.strftime(ontem, "%d de %B de %Y")
#* Converção de string para data
data_string = "11/06/2019 15:30"
data_dt = dt.datetime.strftime(data_string, "%d/%m/%Y %H:%M")