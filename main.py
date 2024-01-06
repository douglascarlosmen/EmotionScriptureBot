from constants import TEXTOS_BIBLICOS, LIMIAR_POSITIVO, LIMIAR_NEGATIVO
from sentiment_analysis import analisar_sentimentos_vader, traduzir_para_ingles
from speech import falar, reconhecer_fala
import random
import nltk

# Certifique-se de ter feito nltk.download('vader_lexicon') anteriormente
nltk.download('vader_lexicon')

def escolher_texto_biblico(polaridade):
    if polaridade > LIMIAR_POSITIVO:  # Limiar ajustado para positivo
        categoria = "positivo"
    elif polaridade < LIMIAR_NEGATIVO:  # Limiar ajustado para negativo
        categoria = "negativo"
    else:
        categoria = "neutro"
    
    textos_sugeridos = TEXTOS_BIBLICOS[categoria]
    texto_selecionado = random.choice(textos_sugeridos)
    return texto_selecionado

def main():
    texto = reconhecer_fala()
    if texto:
        texto_em_ingles = traduzir_para_ingles(texto)
        polaridade = analisar_sentimentos_vader(texto_em_ingles)
        texto_biblico_sugerido = escolher_texto_biblico(polaridade)        
        print(f"Texto bíblico sugerido para reflexão: {texto_biblico_sugerido}")
        falar(texto_biblico_sugerido)

if __name__ == "__main__":
    main()
