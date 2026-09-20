import colorama
from colorama import Fore, Back, Style

colorama.init()

print("Дивимось вміст colorama:")
print(dir(colorama))

print("\nПеревіряєм кольори:")
print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Style.RESET_ALL)

print("\nАтрибути Fore:")
for item in dir(Fore):
    if not item.startswith("_"):
        print(item)