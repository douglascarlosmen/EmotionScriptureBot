import pyttsx3
import speech_recognition as sr

def falar(texto):
    # Usa a síntese de voz para falar o texto.
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def reconhecer_fala():
    # Reconhece a fala do usuário
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga como você está se sentindo hoje: ")
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não entendi o que você disse, tente novamente.")
            return None
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados; {e}")
            return None
