# coding=utf8

import os
from time import sleep
from random import randint
from termcolor import colored
import pyperclip


wordlist="㡈㟜㒱㑪㞥㠘㙸㚉㕑㟆㟦㝶㡡㔺㠐㟙㤳㙋㜹㒛㤜㢽㝢㛝㚝㡪㢅㙙㕡㓿㣱㔹㖥㤺㜧㝋㗪㒢㛓㐬㓖㑌㡝㡔㙵㑑㞐㗥㞞㛉㑁㣊㖅㑍㝪㛕㐙㞦㙅㛗㗬㘗㒅㣄㠑㐤㘢㥁㣁㟱㢬㑅㖌㔇㘧㢞㠙㓑㒁㡺㣕㒃㔪㔗㕦㡅㗯㗅㓠㚾㞎㢾㒘㝚㜒㙞㘪㙳㥑㚇㐒㤚㛐㜑㞊㡄㢀㑤㖣㢣㘕㣉㔎㕵㓬㟎㢖㠌㗺㐖㐔㢇㑣㘸㔡㓧㜺㑽㣥㢚㞴㗚㚟㙑㠺㡁㔩㘩㓓㢲㟃㣃㤆㥕㓸㟮㟿㖘㔯㙍㒕㛸㑶㢜㥌㖈㣂㟳㡴㞀㠡㚘㘖㙥㐄㕳㕥㥆㗕㡐㑾㘓㐡㢰㘯㤐㟖㚫㙾㣝㖸㢺㔨㚛㗆㒯㠟㕱㓫㗎㞋㑛㝈㗛㞯㠗㖜㙿㔀㜘㠼㠳㚈㕧㝎㡿㢹㕽㢗㛹㔏㣑㙭㟲㕈㓲㝮㐝㡑㠉㤀㟫㚞㤞㣮㒞㞈㜄㒍㒆㓘㣾㤄㑯㒭㤸㞽㑃㓩㒣㠦㣯㢻㥂㤁㥉㝓㣎㒌㓒㙠㘁㣓㐲㟒㛊㓡㟨㖴㞔㜩㙻㜨㟏㢄㔼㓹㢱㗶㣳㒳㖞㡷㤙㓮㠾㙼㤘㥐㓻㣦㢪㜀㗡㢦㟺㜴㜷㛆㢷㐆㣣㥍㖛㒠㚳㐹㐪㘋㢭㒜㘠㚴㚅㚜㖳㜼㒋㕔㣆㤍㗤㡭㑎㐗㚚㤖㜠㙰㛱㓃㡒㖊㜃㚲㞿㛤㢛㟋㙈㤩㖂㐺㚽㓗㣤㘂㥗㣛㚂㠨㘥㚱㠯㐦㘇㘏㖡㝐㔣㛻㔁㚍㐨㘊㕍㒡㕆㞨㜏㝭㞤㙉㕂㑴㜜㖹㞷㢃㕓㙪㞡㢵㛚㟌㓽㚡㓇㚒㐽㙟㓾㠢㖫㠪㗻㢼㝧㠹㝂㣷㓀㑉㠮㑿㙐㒚㘀㡵㜽㔱㓊㜋㞉㕒㑻㖝㕣㚎㣏㞰㤾㗿㥅㙖㚁㤡㙡㗼㔥㒒㜾㗂㞕㘎㟚㚹㒏㕢㥓㟬㟘㞖㚠㐧㓷㗇㐩㔵㔒㤣㛼㡧㤧㔂㟪㐓㟶㙤㜂㑵㖨㕤㥃㡮㑸㡸㐑㐰㢳㔦㘹㒈㒖㟊㓨㡤㚪㜈㤿㛍㠋㗽㘒㓍㔘㠈㟞㓆㝣㢨㣨㒂㡏㥈㣵㝃㡞㟐㑨㤪㞺㘄㙣㢍㛛㝹㗢㝔㑝㤯㕖㜚㛞㜯㝍㙢㒮㛋㘷㙎㣬㑞㗵㑰㖱㜌㓴㑮㢯㕷㗧㡜㔙㗌㜲㕴㖤㖗㕉㟥㗍㝛㢊㚗㖲㤫㐕㐮㠭㜤㡼㐷㠬㣍㒇㑭㕩㚕㖄㕝㟑㠀㑺㞅㛌㕇㢤㘝㝳㠔㓜㛖㗟㞜㜡㛠㚤㜫㣖㜭㔬㛀㕶㡳㡙㓢㣺㛿㝸㛙㙯㟹㒩㘼㢿㒪㤻㜓㕺㡋㣿㔍㔽㑧㤕㤗㠓㛲㖇㒊㟄㕨㗱㖀㙏㓋㗣㒿㙂㘐㝰㡚㕪㐼㒹㠖㡠㞪㐍㐘㙷㤑㛷㔆㛎㓈㞙㒙㢒㗊㗓㚥㜰㞻㜢㛩㡆㡍㟯㕌㝉㟕㟔㟽㛮㣠㝟㣽㘆㝬㜣㐭㟧㠊㣀㝾㚼㝦㚬㠍㐿㔶㠕㢏㔈㤮㚖㡹㝘㓅㚿㗙㒝㝝㝤㣼㓣㜸㤅㓁㒔㑈㝵㣚㕯㠱㔰㐫㔞㔴㐐㗮㗠㚧㣙㝥㢌㠝㤽㜻㓏㑆㡀㝜㛂㐣㔮㑔㗗㖭㥀㢁㡦㞇㖯㗑㛥㢔㢑㡖㞒㘣㒨㔛㓙㤢㟁㕜㛄㢕㘦㑫㒶㠂㑏㡛㟤㘻㖖㢶㞧㖓㕻㠷㖚㤉㡊㣰㐠㙶㣌㕏㡟㖼㘿㚩㑐㚔㔋㚋㘺㖙㞼㕟㒲㤱㜥㡌㤨㖧㝽㘫㤤㝻㕗㤛㘤㕾㜖㡲㐥㗦㙇㝞㚓㣅㝡㑕㘌㚸㟓㛳㜇㗲㣗㢙㞁㗋㜁㞫㙮㚆㕎㔔㘉㝺㛶㥔㞩㢎㗭㣪㐛㠁㕸㔧㞲㐢㕠㕼㞂㛣㔓㜛㝱㗴㚶㞟㓌㝀㡂㔖㟭㑩㙘㕊㝒㠴㓛㝌㣞㣈㣔㖢㖎㒤㙁㕃㓳㐳㑊㗾㝖㤂㖏㟷㘴㜮㓞㙱㚰㒷㠧㜍㚏㠫㤈㗞㔜㗸㢘㞹㡗㔿㜬㔲㝄㞘㛬㤷㢓㔻㤋㙦㤎㣻㘅㚙㛢㢴㠚㟟㛯㚷㙕㞾㛟㔫㢢㘶㠩㞌㑹㖉㒽㕬㑟㘈㠥㖩㓺㙜㥇㐜㡬㘚㘳㛏㛅㙓㚃㣟㗝㐋㤓㞣㙬㟴㒻㟸㓥㘙㔝㒰㚊㞑㡾㣶㒥㛔㡎㛴㔄㗜㔭㜶㝊㐊㑡㘞㞭㔾㘟㙊㢉㐎㠇㒗㔊㑱㖑㙴㓤㗨㚭㕐㘭㞱㡱㒄㝼㠤㙗㕅㞆㣘㝩㠽㟈㓚㤃㞶㢮㝑㔤㞗㘮㢝㘽㛃㒦㛁㠆㡘㓝㗖㚨㕕㘍㤵㓐㜗㠸㞬㚣㣒㕰㓟㒼㜟㔚㕀㞠㙀㡯㛫㖟㡉㚄㑒㟰㣡㤦㡰㙛㠅㖾㟼㛘㐾㛈㕛㥎㞛㐏㑇㤌㚮㑥㚀㙄㒧㜊㞵㘾㑗㢋㘡㞄㕋㖋㑼㚯㢩㔕㥏㡢㒐㞚㡃㔉㠲㤥㕹㛒㞮㣩㙃㟢㖍㖁㝿㚻㔟㔳㞝㚑㖿㝠㠵㟅㓔㖆㞃㑳㡽㗀㡥㗁㝆㛑㣫㣐㒟㓄㑂㣭㖰㟻㝙㤭㑷㖻㙌㗄㑖㠜㘰㙚㒸㠠㠿㛽㠛㕞㓱㘘㗫㞢㓰㚌㝅㑙㡶㞸㙲㕁㜦㚢㓪㤒㥋㚵㛜㘔㙒㢆㞓㛦㣴㐵㖦㙝㣢㕿㡓㝫㤊㛾㒉㜿㜔㑜㐻㡕㘱㒬㑬㓶㛧㔑㖶㜉㗐㤠㔐㝴㔢㖐㤼㗳㥒㗹㗈㠄㜎㕮㙔㓼㟂㔅㕘㛺㡣㑚㑲㖵㙹㝁㤇㙫㗏㑘㘲㒴㖪㛵㐱㘛㘑㜳㐯㤟㗒㢐㝨㕫㒀㗉㣜㑋㒫㚐㖷㓎㗘㣇㝷㝏㜱㚦㐚㑦㐇㒺㟣㤹㠻㚺㗷㡻㟡㤶㒎㘬㐶㘵㠣㠎㙺㖒㐸㓭㥖㜪㗰㡩㣸㐟㟀㘃㤴㢸㟗㙆㜙㤔㓕㢫㐅㞳㖔㓵㝗㒑㐈㔸㠶㢠㡨㗃㘨㛡㔠㕙㝲㔌㑓㔷㙨㛨㖺㣧㟍㥊㓂㜞㛇㝕㜕㤰㠞㑢㣹㓦㟝㢧㖕㐴㐌㖬㟾㕚㙧㡫㘜㟛㢥㑀㐉㞍㜅㤏㑠㠰㟩㠒㐞㣋㤬㕭㤝㖠㒓㜆㓉㢟㜝㛭㑄㒵㠃㡇㟵㤲㜐㢂㖮㙽㕄㣲㗩㕲㝯㢈㠏㒾㛪㗔㟇㜵㔃㢡㓯㙩㟠㥄㞏㖃㛰㖽㟉㝇" 
numlist="﨤逸都﨧﨨﨩飯飼館"
super_bit="邏"

def design():
 os.system("clear")
 
 # print(len(wordlist)) 1364
 print(colored(" ██▓    ▄▄▄       ███▄    █   ▄████  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓",'green'))
 print(colored("▓██▒   ▒████▄     ██ ▀█   █  ██▒ ▀█▒▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒",'green'))
 print(colored("▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░",'green'))
 print(colored("▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ",'green'))
 print(colored("░██████▒▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ",'green'))
 print(colored("░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ",'green'))
 print(colored("░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░   ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░    ",'green'))
 print(colored("░ ░    ░ ▒      ░   ░ ░ ░ ░   ░  ░        ░░   ░ ▒ ▒ ░░  ░░       ░      ",'green'))
 print(colored("░  ░     ░  ░         ░       ░ ░ ░       ░     ░ ░                       ",'green'))
 print(colored("                                ░               ░ ░                    ",'green'))
 print(colored("                                                                              -Br4v3_H3r0",'red'))
 print("\n")

def menu():
 design()
 print(colored("CHOOSE ONE OF THE OPTIONS TO CONTINUE, MATE",'blue'))
 print(colored("1) ENCODE",'green'))
 print(colored("2) DECODE",'green'))
 print(colored("3) QUIT",'green'))
 print("\n")
 choice=input(colored(">>>",'magenta'))

 if int(choice)==1:
  encryptor()
 elif int(choice)==2:
  decryptor()
 elif int(choice)==3:
  print("\n")
  print(colored("SEE YA LATER HACK3R :)",'green'))
  exit()
 else:
  print(colored("WRONG INPUT!, PLS TRY AGAIN",'red'))
  sleep(1.5)
  os.system("clear")
  menu()
 
def check():
 design()
 repeator=True
 while repeator!=False:
 
    print(colored("ENTER PASSPHRASE : ",'blue'))
    ch=input(colored(">>>",'magenta'))
    if ch=="hello":
       repeator=False
       
       
       
 
    else:
       print(colored("ACCESS DENIED!",'red'))
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
 k=randint(0,1000)
 num_code=str(k)

 for i in range(0,len(num_code)):
  bit=int(num_code[i])
  secret_num=secret_num+numlist[bit-1]

 

 for x in range(0,len(data)):
   i=ord(data[x])
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
  
   for i in range(0,1364):
    if code[x]==wordlist[i]:
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


