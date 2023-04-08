import os
import random
from pygame import mixer
import difflib


#setting console size to the minimum
os.system('mode con: cols=45 lines=5')
#setting my directory
my_musics_location = "E:\Music"
target = ""
init_count = 1
file_list = []
if os.path.exists(my_musics_location):
    for root, dirs, files in os.walk(my_musics_location):
        for file in files:
            file_list.append(os.path.join(root,file))
length = len(file_list) 
mixer.init()
  

#shuffle function to randomly choose an music from the musics list
def shuffle():
    
    args = file_list[random.randint(0 , length)]
    music_name = args.replace("E:\Music\\", "")
    music_name = music_name.replace(".mp3", "")
    if "turkye\\" in music_name:
        music_name = music_name.replace("turkye\\", "")
    if "farsi\\" in music_name:
        music_name = music_name.replace("farsi\\", "")    
    print(music_name)
    mixer.music.stop()
    mixer.music.load(args)
    mixer.music.play()
    
#search function if any input word we have    
def searcher(tr):

    music_name = tr.replace("E:\Music\\", "") 
    music_name = music_name.replace(".mp3", "")
    if "turkye\\" in music_name:
        music_name = music_name.replace("turkye\\", "")
    if "farsi\\" in music_name:
        music_name = music_name.replace("farsi\\", "")
    print(music_name)
    mixer.music.stop()
    mixer.music.load(tr)
    target = ""
    mixer.music.play()
    

#with pressing "enter", the new random music loads! 
while True:
    try:
            
            #first time launch
            if init_count :
                shuffle()
                init_count = 0
            
            #waits for any kind of input
            s = input()
            
            #input data is null = shuffle
            if s=="":
                shuffle()
            #input data is not null = search the input data
            else:
                    target = difflib.get_close_matches(s, file_list,length, 0)
                    target = target[0]
                    searcher(target)
        
    except :
        print("*** file has error ***")
        shuffle()
        continue  
    
    
#Ehsan Mokhtari
