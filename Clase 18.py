import pyttsx3
import speech_recognition as sr
from groq import Groq
engine = pyttsx3.init()
r = sr.Recognizer()

hablar_escribir = input (" Desea escribir la pregunta? (S/n): ").lower()
desea_escuchar = input(" Desea escuchar la respuesta de la AI? (S/n):  ").lower()

while True:
        if hablar_escribir =="n":
        #abre microfono
            with sr.Microphone() as source:
                print (" Hable (tiene 10 segundos): ")
            #ajusta el audiodel microfono
                r.adjust_for_ambient_noise(source)
            #Escucha el audio del microfono durante 10 segundos
                audio=r.listen(source,timeout=10, phrase_time_limit=5)
            #Ajusta el nivel de ruido ambiental para obtener mejores resultados
                audio = r.listen (source)
                try:
                    pregunta= r.recognize_google(audio, language = 'es-ES').lower()
                    print(f"Dijiste: {pregunta}")
                except sr.UnknownValueError:
                    print(" Lo siento, no he podido entender lo que has dicho.")
                except sr.RequestError:
                    print(" Lo siento, ha habido un problema al intentar comunicarme con el servicio de Google")
        else:
            pregunta = input ("Escriba la pregunta: ")
            
        if pregunta =="no" or pregunta == "termina" or pregunta =="cortala" or pregunta == "No quiero continuar":
            break
        else:
            usuario = Groq(
                api_key="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",
            )
            
            interaccion_chat = usuario.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": pregunta, # detallamos lo que queremos saber
                    }
                ],
                model="llama3-8b-8192", #copia el modelo complatible y lo pegas, reemplaza 
            )

            respuesta = interaccion_chat.choices[0].message.content
            if desea_escuchar != "n":
                engine.say (respuesta)
                engine.runAndWait()
                print (respuesta)
                