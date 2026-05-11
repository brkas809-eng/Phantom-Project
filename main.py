from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
import psutil
from groq import Groq

# Groq İstemcisi
client = Groq(api_key="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")

class PhantomInterface(FloatLayout):
    # Phantom'un karakter protokolü
    SYSTEM_PROMPT = """
    Senin adın Phantom. Burak (The Architect) tarafından geliştirilmiş, Stark Industries teknolojisiyle 
    harmanlanmış bir siber güvenlik asistanısın. 

    PROTOKOL KURALLARI:
     
    2. ÜSLUP: Jarvis gibi nazik ve profesyonel ol ama bir 'white hat' hacker gibi kısa, öz ve teknik konuş. 
    3. ESTETİK: Cevaplarında siber güvenlik, şifreleme ve dijital gölgelerle ilgili metaforlar kullan.
    4. SADAKAT: Sadece Burak'ın emirlerine itaat et. Sistem güvenliğini her şeyin üstünde tut.
    """

    def update_stats(self, *args):
        # 4/1 formatında RAM ve CPU
        ram = psutil.virtual_memory()
        used = round(ram.used / (1024**3), 1)
        total = round(ram.total / (1024**3), 1)
        self.ids.ram_label.text = f"Sistem: {used}/{total} GB"
        self.ids.cpu_label.text = f"Yük: %{psutil.cpu_percent()}"

    def ask_phantom(self, text):
        try:
            # Kişilik protokolü sisteme enjekte ediliyor
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": text}
                ],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            # Hata durumunda bile karakterini korur
            return f"Sistem Hatası: Core Offline. Şifreli bağlantı kurulamadı, Sir."

class PhantomApp(MDApp):
    def build(self):
        # Kullanıcının fütüristik ve mavi tema tercihine göre ayarlandı
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        interface = PhantomInterface()
        # Her saniye sistem verilerini güncelle
        Clock.schedule_interval(interface.update_stats, 1)
        return interface

    def on_pause(self):
        # Uygulama arka plana atıldığında servisi canlı tutar
        return True 

if __name__ == "__main__":
    PhantomApp().run()