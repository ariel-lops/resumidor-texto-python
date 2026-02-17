def receber_texto():
    print("Cole o texto abaixo (finalize com uma linha vazia):")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)
    return " ".join(linhas)

def limpar_texto(texto):
    texto= texto.lower()
    texto = texto.replace("\n", " ")
    texto = ' '.join(texto.split())
    return texto
def separar_frases(texto):
    frases = texto.split('. ')
    return [frase.strip() for frase in frases if frase]
texto = receber_texto()
texto_limpo = limpar_texto(texto)
frases = separar_frases(texto_limpo)
print(texto_limpo)

STOPWORDS = {"de","a","o", "e", "para", "com", "em", "um", "uma"}
def calcular_frequencia_palavras(texto):
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        if palavra not in STOPWORDS:
            if palavra in frequencia:
                frequencia[palavra] += 1
            else:
                frequencia[palavra] = 1
    return frequencia
def pontuar_frases(frases, frequencia):
    pontuacao = {}
    for frase in frases:
        palavras = frase.split()
        for palavra in palavras:
            if palavra in frequencia:
                if frase in pontuacao:
                    pontuacao[frase] += frequencia[palavra]
                else:
                    pontuacao[frase] = frequencia[palavra]
    return pontuacao
frequencia_palavras = calcular_frequencia_palavras(texto_limpo)
pontuacao = pontuar_frases(frases, frequencia_palavras)

frases_ordenadas = sorted ( 
    pontuacao,
    key=pontuacao.get,
    reverse=True
)
N = 3
resumo = frases_ordenadas[:N]

resumo_frases = [
    frase for frase in frases
    if frase in resumo
]
resumo = " . ".join(resumo_frases)

print("\nResumo:")  
print(resumo)