import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
 
# настройки
opts = {
    "name":('тоша', 'антошка', 'тофа', 'тош', 'тож', 'тоже'),
    "act": ('скажи','расскажи','покажи','сколько','произнеси','подскажи', 'как', 'как пройти', 'как дойти', 'как найти', 'каков', 'какое'),
    "cmds": {
        "way": ('путь','к кабинету','в кабинет', 'в группу', 'к группе'),
        "menu": ('меню','меню на день','меню на сегодня','будут есть','блюда'),
        "plan": ('мероприятия', 'мероприятие', 'планы'),
    }
}
 
# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

speak("Тоша слушает")


def callback(recognizer, audio):
            try:
                voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
                print("[log] Распознано: " + voice)
        
                if voice.startswith(opts["name"]):
                    # обращение к Тоше
                    cmd = voice
                
                    for x in opts['act']:
                        cmd = cmd.replace(x, "").strip()
                    # распознает и выполняет команду
                    cmd = recognize_cmd(cmd)
                    execute_cmd(cmd['cmd'])
                
            except sr.UnknownValueError:
                print("[log] Голос не распознан!")
            except sr.RequestError as e:
                print("[log] Неизвестная ошибка!")


 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC
 
def execute_cmd(cmd):
    if cmd == 'way':
        # сказать путь
        speak("Поднимитесь на второй этаж, третья дверь налево")
   
    elif cmd == 'menu':
        # сказать меню
        speak("На завтрак овсяная каша на молоке и чай, на обед борщ с хлебом, на полдник кефир, на ужин пюре с куриной котлетой")

    elif cmd == 'plan':
        # сказать план на день
        speak("Сегодня зарядка, пение и французский")
   
    else:
        print('Я вас не понимаю, повторите!')

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
    r.adjust_for_ambient_noise(source)
 
stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) #infinity loop



	
