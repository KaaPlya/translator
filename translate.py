
from translate import Translator
from colorama import Fore,init
import subprocess
 
print("Tarjimonga hush kelibsiz\n")

user = input(Fore.YELLOW+" [ * ] "+Fore.WHITE+"Tarjima qilmoqchi bogan so`zingizni yozing : ")

options = Translator(from_lang='en', to_lang='uz')
translate = options.translate(user)

print(Fore.YELLOW+'----------'+Fore.WHITE+' Tarjima '+Fore.YELLOW+'----------')

print(translate)

echo = subprocess.getoutput(f"echo {translate} >> translate.txt")