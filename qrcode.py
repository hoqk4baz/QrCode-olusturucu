import keyboard
import qrcode
import dialogs
import time

print("  _____             _      ______                ")
print(" |  __ \           | |    |  ____|               ")
print(" | |  | | __ _ _ __| | __ | |__   _ __  ______ _ ")
print(" | |  | |/ _` | '__| |/ / |  __| | '_ \|_  / _` |")
print(" | |__| | (_| | |  |   <  | |____| | | |/ / (_| |")
print(" |_____/ \__,_|_|  |_|\_\ |______|_| |_/___\__,_|")
print("                              Telegram: @dwstoree")
print("")

time.sleep(1)
print("URL'leri Yada yazıları QRcode dönüştürür")
print("")

if keyboard.is_keyboard():
	dark = keyboard.get_selected_text()
else:
	
	dark = input("Url veyahut Yazı giriniz: ")

if dark:
	img = qrcode.make(dark)
	img.show()
else:
	dialogs.hud_alert('Herhangi bir metin girmediniz', 'HATA')
