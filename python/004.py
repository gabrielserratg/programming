#!/usr/bin/python3
import sys, random
from datetime import datetime

print(datetime.now())

from datetime import datetime as dt
print(dt.now())

def new_line():
        print('\n')
new_line()

#Advanced Strings
print("Advanced Strings: ")
my_name = "Gabriel"
print(my_name[0]) #first initial
print(my_name[-1]) #last letter

sentence = "este é meu texto basico!"

print(sentence[:4]) #first word
print(sentence[-7:-1]) #last word

print('\n') #Pular linha

#esse print vai usar o "in" para saber c tem alguma letra em uma certa palavra
print("Tem a letra A em apple :", "A" in "Apple") #não esta usando variavel
letter = "A"
word = "Apple"
print("Tem a letra A em Apple :", letter in word) #usando variavel , como letter e word
