# coding=utf8

import os
from time import sleep
from random import randint
import pyperclip

wordlist="                                                 OSX07sezrn&B,]u~>QP=q4DGMVZ/6da{p2[3hI8|kRULoFKWm?j<9i\"5TCgb+}x\\w`-'NEAH.lYcJ1:fy"
numlist="@#$%^*_();"
super_bit="v"
space="t"

def design():
 os.system("clear")
 

 print(" ██▓    ▄▄▄       ███▄    █   ▄████  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓")
 print("▓██▒   ▒████▄     ██ ▀█   █  ██▒ ▀█▒▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒")
 print("▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░")
 print("▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ")
 print("░██████▒▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ")
 print("░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ")
 print("░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░   ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░    ")
 print("░ ░    ░ ▒      ░   ░ ░ ░ ░   ░  ░        ░░   ░ ▒ ▒ ░░  ░░       ░      ")
 print("░  ░     ░  ░         ░       ░ ░ ░       ░     ░ ░                       ")
 print("                                ░               ░ ░                    ")   
 print("                                                                              -Br4v3_H3r0")
 print("\n")

def menu():
 design()
 print("CHOOSE ONE OF THE OPTIONS TO CONTINUE, MATE")
 print("1) ENCODE")
 print("2) DECODE")
 print("3) QUIT")
 print("\n")
 choice=input(">>>")

 if int(choice)==1:
  encryptor()
 elif int(choice)==2:
  decryptor()
 elif int(choice)==3:
  exit()
 else:
  print("WRONG INPUT!, PLS TRY AGAIN")
  sleep(1.5)
  os.system("clear")
  menu()
 
def check():
 design()
 repeator=True
 while repeator!=False:
 
    print("ENTER PASSPHRASE : ")
    ch=input(">>>")
    if ch=="123":
       repeator=False
       
       
       
 
    else:
       print("ACCESS DENIED!")
       sleep(1.5)
       os.system("clear")
       design()
     
 if repeator==False:
  menu()
 
def encryptor():
 
 design()
 print("ENTER THE TEXT TO ENCODE:")
 data=input(">>>")

 secret_num=""
 secret_code=""
 k=randint(0,8)
 num_code=str(k)

 for i in range(0,len(num_code)):
  bit=int(num_code[i])
  secret_num=secret_num+numlist[bit-1]

 

 for x in range(0,len(data)):
   i=ord(data[x])
   if(i==32):
      secret_code=secret_code+space
   else:
      secret_code=secret_code+wordlist[i+k]
 pyperclip.copy(secret_code+super_bit+secret_num)
 print("\n")
 print("ENCODED MESSAGE:")    
 print(secret_code+super_bit+secret_num)
 print("\n(Copied to clipboard!)")
 print("\n")
 print("Do you want to encode another message (y/n)")
 choice=input(">>>")

 if choice=='y' or choice=='Y':
  encryptor()
 elif choice=='n' or choice=='N':
  menu()
 else:
  os.system("clear")
  exit() 
 

def decryptor():
 design()
 print("ENTER THE TEXT TO DECODE:")
 code=input(">>>")
 
 number=""

 for i in range(len(code)-1,0,-1):
  if code[i]==super_bit:
   break
  
  else:
   for j in range(0,9,1):
    if code[i]==numlist[j]:
     number=str(j+1)+number
 
 og_code=""

 for x in range(0,len(code)):

   if code[x]==super_bit:
    break
  
   for i in range(0,len(wordlist)):
    if code[x]==space:
      og_code=og_code+" "
      break

    elif code[x]==wordlist[i]:
       og_code=og_code+chr(i-int(number))
       break
 pyperclip.copy(og_code)
 print("\n")
 print("DECODED MESSAGE:")    
 print(og_code)
 print("\n(Copied to clipboard!)")
 print("\n")
 print("Do you want to decode another message (y/n)")
 choice=input(">>>")

 if choice=='y' or choice=='Y':
  decryptor()
 elif choice=='n' or choice=='N':
  menu()
 else:
  os.system("clear")
  exit()
 os.system("clear")
check()


