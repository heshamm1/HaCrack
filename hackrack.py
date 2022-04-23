import hashlib
import sys
import pyfiglet
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('HaCrack', font='slant'),
       'yellow', attrs=['bold'])
print(">>>>>>>>>> By: Hesham Ahmed <<<<<<<<<<")
print("______________________________________")
print("")

HASH = input("Put your Hash: ")

def main():
    with open("wordlist.txt", 'r') as f:
        for line in f:
            for word in line.split():
                HashWL = hashlib.sha256(word.encode('utf-8')).hexdigest()
            if HashWL.upper() == HASH or HashWL.lower() == HASH:
                print(f'[+] Password found: {word}')
                exit(0)
            else:
                print(f'[-] Guess: {word} incorrect...')
        print('Password not found in wordlist...')

if __name__ == '__main__':
        main()