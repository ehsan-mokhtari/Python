#ehsan mokhtari   12-may-2020   955367025

#the list of words for checking with input_word
myList = ["hello","yellow","below","goodbye","word","java","python","computer"]

#in the lists below we will put our words with edit distance values = 0(the same word),1,2,3
edit_distance_0 = []
edit_distance_1 = []
edit_distance_2 = []
edit_distance_3 = []

#m is lenght of input word and n is the lenght of word we are calculating edit distance value with it
def editDistance(input_word, target_word,m,n):

    #if input_word is an empty string, the edit distance value is the lenght of target_word
    if m==0:
         return n
    
    #if target_word is an empty string, the edit distance value is the lenght of input_word
    if n==0:
        return m
  
    if input_word[m-1]==target_word[n-1]:
        return editDistance(input_word,target_word,m-1,n-1)
  
    #returning +1 to edit_distance value in the case of letter insert,remove,replace recursivly
    return 1 + min(editDistance(input_word, target_word, m, n-1),    # Insert
                   editDistance(input_word, target_word, m-1, n),    # Rmeove
                   editDistance(input_word, target_word, m-1, n-1)   # Replace
                   )

input_word = input("enter your word : ")
m = len(input_word)

val = 0
for i in range(len(myList)):
   n = len(myList[i])
   val = editDistance(input_word,myList[i],m,n)
   if val == 0:
       edit_distance_0.append(myList[i]) 
   elif val == 1 :
       edit_distance_1.append(myList[i])
   elif val == 2:
       edit_distance_2.append(myList[i])        
   elif val == 3:
       edit_distance_3.append(myList[i])

print("edit distance = 0   =>  " ,edit_distance_0)
print("------------------------------------------------------------------------------")
print("edit distance = 1   =>  " ,edit_distance_1)
print("------------------------------------------------------------------------------")
print("edit distance = 2   =>  " ,edit_distance_2)
print("------------------------------------------------------------------------------")
print("edit distance = 3   =>  " ,edit_distance_3)
print("------------------------------------------------------------------------------")