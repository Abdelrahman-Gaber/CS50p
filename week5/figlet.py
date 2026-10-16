import sys
from pyfiglet import Figlet

if sys.argv[1] not in ["-f", "--font"]:
    print("Not -f nor --font")
    sys.exit("Invalid Format")

try:
    f = Figlet(font=sys.argv[2])
except:
    sys.exit("Invalid Format")
user_text = input("Input: ")
print(f'Output: {f.renderText(user_text)}')