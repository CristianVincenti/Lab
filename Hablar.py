#para actualizar el pip: python -m pip install --upgrade pip
#para instalar la biblioteca pip install pytttsx3

import pyttsx3
engine = pyttsx3.init()
que_queres_que_diga = input (" Decis lo que queres que diga:  ")
engine.say (que_queres_que_diga)
rate = engine.getProperty  ('rate')
print (f" La velocidad actual es : {rate}")
engine.setProperty ('rate', 300) # velocidad de la voz al ejecutarse
engine.say (que_queres_que_diga)
engine.setProperty ('rate', 50) # velocidad de la voz al ejecutarse
engine.say (que_queres_que_diga)
#buscando las voces que tiene Windows instalado
voces = engine.getProperty('voices')
for voz in voces:
    print(f" El nombre es: {voz.name}")
#Cambiando la voz a la segunda, en este caso Ingles
engine.setProperty('voices', voces[1].id)
engine.say(que_queres_que_diga)

engine.runAndWait()

