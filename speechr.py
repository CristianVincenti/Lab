import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hable: ")
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source,timeout=10, phrase_time_limit=5)
    audio = r.listen (source)
    try:
        text= r.recognize_google(audio, language = 'es-ES')
        print(f"Dijiste: {text}")
    except sr.UnknownValueError:
        print(" Lo siento, no he podido entender lo que has dicho.")
    except sr.RequestError:
        print(" Lo siento, ha habido un problema al intentar comunicarme con el servicio de Google")
        