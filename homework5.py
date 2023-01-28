import sys
print(sys.executable)
print(sys.version)
print(sys.platform)

print("Бібліотека Colorama."
      "Одна з найпопулярніших бібліотек для редагування кольору тексту а також поліпшеної читабельності виводу."
      "\n Version: 0.4.6 "
      "\n Summary: Cross-platform colored terminal text."
      "\n Author-email: Jonathan Hartley <tartlay@tartley.com>")

from colorama import Fore, Back, Style
print(Fore.MAGENTA + 'some magenta text')
print(Back.LIGHTCYAN_EX + 'and with a cyan background')
print(Style.DIM + 'and in a dim text')
print(Style.RESET_ALL)
print('back to normal now')

print("Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET."
      "\nBack: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET."
      "\nStyle: DIM, NORMAL, BRIGHT, RESET_ALL")