# Crypto-Chinese
An cybersec approach to encrypt messages in a unique way.

## Requirements
Install pyperclip using

> pip install pyperclip

### To run langcrypt-chinese.py run this command:

- python3 langcrypt-chinese.py

PASSWORD: hello 

#### Some machines dont support the ascii values of chinese characters so you might see something like this as your output = 㡁㚟㢲㢲㤆邏都﨤 (some identical blocks)
#### Dont worry, you can still use this output as each character is unique and decryption still works well



### To run langcrypt-normal.py run this command:

- python3 langcrypt-normal.py

PASSWORD: 123

### To run security_checker.py run this command:

- python3 security_checker.py

This program is made so that we could see how a single string can be encrypted with more than 1000 keys chosen randomly at a time depicting its security level

This program takes 3 values as input:

- Text to Encode : The text to be encoded 
- No. of reps (N): No. of encrypted strings to be generated
- Range : This value can be between (2- 1364) and the program will chose N random values from range (0 - Range) and hence choose that key
(There are 1364 keys in total. A low value of Range depicts low security as the smaller the range is, the chances of repetition of a particular key is high)

The keys are encoded in chinese characters so you might face the same situationas mentioned above (see the lancrypt-chinese.py part). 
