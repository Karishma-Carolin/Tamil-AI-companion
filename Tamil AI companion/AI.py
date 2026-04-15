import speech_recognition as sr
from gtts import gTTS
import os
import time
from playsound import playsound
import datetime
import subprocess
import sys
import pywhatkit
from googletrans import Translator
import pygame

def speak(text):
    tts = gTTS(text=text, lang='ta')
    filename = "response.mp3"
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove(filename)

def listen_tamil():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ பேசுங்கள் (Speak now)...")
        audio = r.listen(source)

    try:
        print("🔍 உரையாக்கம் நடக்கிறது...")
        text = r.recognize_google(audio, language='ta-IN')
        print("📝 நீங்கள் சொன்னது:", text)
        return text
    except sr.UnknownValueError:
        print("🤔 ஏதாவது தவறு நடந்தது. புரியவில்லை.")
        return "மன்னிக்கவும், உங்கள் உரையை புரிந்து கொள்ள முடியவில்லை."
    except sr.RequestError:
        print("⚠️ இணைய இணைப்பு தேவைப்படுகிறது.")
        return "இணைய இணைப்பு இல்லை."

def open_software(software_name):
    software_name = software_name.lower()
    if 'chrome' in software_name or 'குரோம்' in software_name:
        speak('குரோம் திறக்கிறது...')
        print('குரோம் திறக்கிறது...')
        speak('Opening Chrome')
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

    elif 'microsoft edge' in software_name or 'எட்ஜ்' in software_name:
        speak('மைக்ரோசாஃப்ட் எட்ஜ் திறக்கிறது...')
        print('மைக்ரோசாஃப்ட் எட்ஜ் திறக்கிறது...')
        speak('Opening Microsoft edge')
        program = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        subprocess.Popen([program])

    elif 'play' in software_name or 'இசை' in software_name or 'பாடல்' in software_name:
        speak('யூடியூபில் திறக்கிறது...')
        print('யூடியூபில் திறக்கிறது...')
        speak('Opening Youtube')
        pywhatkit.playonyt(software_name)

    elif 'notepad' in software_name or 'நோட்பேட்' in software_name:
        speak('நோட்பேட் திறக்கிறது...')
        print('நோட்பேட் திறக்கிறது...')
        speak('Opening notepad')
        subprocess.Popen(['notepad.exe']) 

    elif 'calculator' in software_name or 'கால்குலேட்டர்' in software_name:
        speak('கால்குலேட்டர் திறக்கிறது...')
        print('கால்குலேட்டர் திறக்கிறது...')
        speak('Opining calculator')
        subprocess.Popen(['calc.exe'])
    else:
        speak(f"மன்னிக்கவும், {software_name} என்ற மென்பொருளை என்னால் கண்டுபிடிக்க முடியவில்லை")

def close_software(software_name):
    software_name = software_name.lower()
    if 'chrome' in software_name or 'குரோம்' in software_name:
        speak('குரோம் மூடப்படுகிறது...')
        os.system("taskkill /f /im chrome.exe")

    elif 'microsoft edge' in software_name or 'எட்ஜ்' in software_name:
        speak('மைக்ரோசாஃப்ட் எட்ஜ் மூடப்படுகிறது...')
        os.system("taskkill /f /im msedge.exe")

    elif 'notepad' in software_name or 'நோட்பேட்' in software_name:
        speak('நோட்பேட் மூடப்படுகிறது...')
        os.system("taskkill /f /im notepad.exe")
        
    elif 'calculator' in software_name or 'கால்குலேட்டர்' in software_name:
        speak('கால்குலேட்டர் மூடப்படுகிறது...')
        os.system("taskkill /f /im calculator.exe")
    else:
        speak(f"மன்னிக்கவும், {software_name} என்ற திறந்த மென்பொருளை என்னால் கண்டுபிடிக்க முடியவில்லை")
def cmd(text):

    if 'நிறுத்து' in text or 'stop' in text:
        speak('நிரல் நிறுத்தப்படுகிறது. விடைபெறுகிறேன்!')
        sys.exit()
        
    if 'திற' in text or 'open' in text:
        software_name = text.replace('திற', '').replace('open', '').strip()
        open_software(software_name)
        
    elif 'மூடு' in text or 'close' in text:
        software_name = text.replace('மூடு', '').replace('close', '').strip()
        close_software(software_name)

    elif 'நேரம்' in text or 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        speak(f'தற்போதைய நேரம் {current_time}')

    elif 'வணக்கம்' in text or 'hai' in text or 'hello' in text:
        speak("வணக்கம் சார்!")

    elif "காலை வணக்கம்" in text or "good morning" in text:
        speak("வெப்பமான காலை வணக்கம்")
        speak("நீங்கள் எப்படி இருக்கிறீர்கள்?")

    elif "நான் நன்றாக இருக்கிறேன்" in text or "I am fine" in text:
        speak("மிகவும் நல்லது")

    elif "நான் யார்" in text or "who I am" in text:
        speak("நீங்கள் பேசுகிறீர்கள், அப்படியானால் நீங்கள் ஒரு மனிதர் தான்.")

    elif 'நன்றி' in text or 'thank you' in text:
        speak("இது என் மகிழ்ச்சி சார்!")

    elif 'நன்றாக' in text or 'fine' in text or 'good' in text:
        speak("நீங்கள் நன்றாக இருப்பது எனக்கு மகிழ்ச்சி அளிக்கிறது")

    elif 'உன் பெயர் என்ன' in text or 'what is your name' in text:
        speak('என் பெயர் நான்சி, உங்கள் செயற்கை நுண்ணறிவு உதவியாளர்')

    else:
        speak('மன்னிக்கவும், நான் உங்கள் கேள்வியை புரிந்து கொள்ளவில்லை')
    
    return True

def main():
    while True:
        text = listen_tamil()
        speak("நீங்கள் சொன்னீர்கள்: " + text)
        cmd(text)
        time.sleep(1)

if __name__ == "__main__":
    main()
