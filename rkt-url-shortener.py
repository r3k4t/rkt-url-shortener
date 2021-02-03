
import os
import sys
import bitly_api 

os.system("clear")

print ("                  ===================================")
print ("                  |        Rkt Url Shortener        |")
print ("                  ===================================")
print ("                  |Author : Rahat Khan Tusar(rkt)   |")
print ("                  |Github : https://github.com/r3k4t|")
print ("                  ===================================")
print

url=raw_input('Enter a link(Ex:https://www.google.com):')

BITLY_ACCESS_TOKEN ='2a917e7994b7f2b3b0619132c41f69977ea26651'

b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN) 

resp =b.shorten(url) 

print(resp) 

