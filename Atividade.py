
#aTIVIDADE PARA LIMPAR UM TEXTO E SEPARAR AS PALAVRAS EM PYTHON 
from unidecode import unidecode

with open("texto.txt", "r") as texto:
    conteudo = texto.read()

print(f'''O texto é: 
{conteudo}
''')

palavrass= []
quantidade= []
lista_menores_valores = []
lista_maiores_valores = []
numeros = []
numeros1 = []

texto_limpoo = False
funcaoo = False

pergunta_global = 1

while pergunta_global != '0':


    pergunta_p = input('''
                [I] - limpar os acentos desse texto
                [II] - Realizar a contagem das palavras e mostrar a quantidade das palavras em ordem decrescente
                [III] - Mostrar a quantidade de alguma palavra
                [IV] - Mostrar as palavras que menos apareceram no texto
                [V] - Mostrar as palavras que mais apareceram no texto
                [0] - Sair do programa
        Qual opção você deseja? --> '''
    )


    if (pergunta_p == '2' or pergunta_p == '3'or pergunta_p == '4' or pergunta_p == '5') and not texto_limpo:

        input("Não é possivel escolher essa opção agora")


    elif pergunta_p == '1':

        texto_sem_pontos_virgulas = conteudo.replace(",", "").replace(";", "").replace(".", "")
        conteudo_limpo = unidecode(texto_sem_pontos_virgulas)
        print("Texto Limpo: ")
        print()
        print(conteudo_limpo)
        
        texto_limpoo = True

    elif (pergunta_p == '3' or pergunta_p == '4' or pergunta_p == '5') and not funcao:

        input("Não é possivel escolher essa opção agora")


    elif (pergunta_p == '2'):

        palavras = conteudo_limpo.split()

        frequencia = {}
        for palavra in palavras:
            if palavra in frequencia:
                frequencia[palavra] += 1
            else:
                frequencia[palavra] = 1

        palavras_ordenadas = sorted(frequencia, key=frequencia.get, reverse=True)

        print("O texto tem", len(palavras), "palavras.")
        print("Palavras por frequência:")
        for palavra in palavras_ordenadas:
            print(palavra, ":", frequencia[palavra])
            palavrass.append(palavra)
            quantidade.append(frequencia[palavra])
        
        funcaoo = True
        #print(palavrass)
        #print(quantidade)
    
    elif pergunta_p == '3':

        while True:
            print()
            pergunta = input("Qual palavra você deseja saber a quantidade de vezes que aparece no texto: ")
            
            if not pergunta:
                print("Saindo do programa...")
                break

            if pergunta in palavrass:
                
                print(f"A palavra {pergunta} apareceu {quantidade[palavrass.index(pergunta)]} vezes no texto")
            else:
                input(f"A palavra {pergunta} não está no texto, digite outra palavra")


    elif pergunta_p == '4':

        numero_menos_frequente = min(quantidade)
        
        for i, numero in enumerate(quantidade):
            if numero == numero_menos_frequente:
                numeros.append(i)

        print(numeros)

        for x in numeros:
           lista_menores_valores.append(palavrass[x])

        print()
        print("Lista das palavras que menos aparecem: ")
        print()
        print(lista_menores_valores)


    elif pergunta_p == '5':
        numero_mais_frequente = max(quantidade)

        for en, number in enumerate(quantidade):
            if number == numero_mais_frequente:
                numeros1.append(en)
        
        for y in numeros1:
            lista_maiores_valores.append(palavrass[y])

        print()
        print("Lista das palavras que mais aparecem: ")
        print()
        print(lista_maiores_valores)


    elif pergunta_p == '0':
        print()
        print("saindo do programa...............")
        print()
        pergunta_global = '0'
    
    else:
        print()
        input("Esse não é um numero disponível, tente outro... ")
        print()