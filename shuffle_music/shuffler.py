import os
import random
from pygame import mixer

#setting console size to the minimum
os.system('mode con: cols=50 lines=6')
#setting my directory
my_musics_location = "D:\Ehsan\Music"
#getting the musics list inside an array
music_ls = os.listdir(my_musics_location)

#shuffle function to randomly choose an music from the musics list
def shuffle():
    r = random.randint(0 , len(music_ls))
    s = my_musics_location+"\\"+music_ls[r]
    print("****************************")
    print(music_ls[r])
    print("next = > ")
    print("****************************")
    mixer.init()
    mixer.music.stop()
    mixer.music.load(s)
    mixer.music.play()   

#with pressing "enter", the new random music loads! 
while True:
    try:
        shuffle()
    except :
        continue    
    if input():
        continue

#Ehsan Mokhtari    