[app]
title = Phantom
package.name = phantom_asistan
package.domain = org.architect.burak
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# KRİTİK İZİNLER
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, FOREGROUND_SERVICE, RECORD_AUDIO, WAKE_LOCK

# ARKA PLAN SERVİSİ TANIMI
android.services = PhantomService:service.py

# GEREKLİ KÜTÜPHANELER
requirements = python3,kivy,kivymd,psutil,groq,requests,certifi,charset-normalizer,idna,urllib3

# EKRAN AYARI
orientation = portrait
android.arch = armeabi-v7a

# SİSTEM ÜSTÜNDE GÖRÜNME İZNİ (API 23+)
android.api = 31
android.minapi = 21