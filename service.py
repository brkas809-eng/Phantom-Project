from jnius import autoclass
from time import sleep

# Android kütüphanelerine erişim
PythonService = autoclass('org.kivy.android.PythonService')
service = PythonService.mService

def start_listening():
    while True:
        # Burada basitleştirilmiş bir döngü var
        # Normalde 'SpeechRecognition' arka planda sürekli dinleme yapar
        print("Phantom Arka Planda Aktif...")
        sleep(5)

if __name__ == '__main__':
    start_listening()