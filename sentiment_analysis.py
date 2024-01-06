from googletrans import Translator
from nltk.sentiment import SentimentIntensityAnalyzer

def analisar_sentimentos_vader(texto):
    # Analisa os sentimentos do texto usando VADER.
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(texto)
    return score['compound']  # Retorna o score composto

def traduzir_para_ingles(texto):
    # Traduz o texto para o inglês.
    tradutor = Translator()
    traducao = tradutor.translate(texto, src='pt', dest='en')
    return traducao.text