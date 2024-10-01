 #API Key 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
#!snippets
import pyttsx3
from groq import Groq
while True:
    pregunta = input("Ingrese su pregunta o una Q para salir  ").capitalize()
    if pregunta == "Q":
            exit (" Gracias por usar nuestra aplicacion")
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
    engine = pyttsx3.init()
    engine.say (respuesta)
    engine.runAndWait()
    print (respuesta)