import cv2
import numpy

ahash = {  "0":"00000000","1":"00000001","2":"00000010","3":"00000011","4":"00000100","5":"00000101","6":"00000110" , 
           "7":"00000111","8":"00001000","9":"00001001",
           "a":"00001010","b":"00001011","c":"00001100","d":"00001101","e":"00001110","f":"00001111","g":"00010000","h":"00010001",
           "i":"00010010","j":"00010011","k":"00010100","l":"00010101","m":"00010110","n":"00010111","o":"00011000","p":"00011001",
           "q":"00011010","r":"00011011","s":"00011100","t":"00011101","u":"00011110","v":"00011111","w":"00100000","x":"00100001",
           "y":"00100010","z":"00100011",
           "A":"00100100","B":"00100101","C":"00100110","D":"00100111","E":"00101000","F":"00101001","G":"00101011",
           "H":"00101100","I":"00101101","J":"00101110","K":"00101111","L":"00110000","M":"00110001","N":"00110010",
           "N":"00110011","O":"00110100","P":"00110101","Q":"00110110","R":"00110111","S":"00111000","T":"00111001",
           "U":"00111010","V":"00111011","W":"00111100","X":"00111101","Y":"00111110","Z":"00111111",
           " ":"01000000","#":"01000001","!":"01000010","@":"01000011","$":"01000100","%":"01000101","^":"01000110",
           "&":"01000111","*":"01001000","(":"01001001",")":"01001010","-":"01001011","_":"01001100","+":"01001101",
           "=":"01001110",".":"01001111","/":"01010000","?":"01010001",":":"01010010",";":"01010011","<":"01010100",
           ">":"01010101","`":"01010110","~":"01010111",",":"01011000","[":"01011001","]":"01011010","{":"01011011",
           "}":"01011100","|":"01011101","\\":"01011110"
 }

#the text you want to encrypt insied image
inputText = "hello my name is @Ehsan@ and blah blah Blah wow!"         

def encrypt(input_text):
    temp = ""
    for i in input_text:
        temp+=ahash[i]
    return temp

def decrypt(input_text):
    temp=""
    for i in range(int(len(input_text)/8)):
        temp += list(ahash.keys())[list(ahash.values()).index(input_text[8*i:8*(i+1)])]
    return temp    

def encrypt_image(img_path,input_text):
    img = cv2.imread(img_path,1)
    rows,cols,dims = img.shape
    img = img.flatten()
    length = len(input_text)
    if length<10:
        length="000"+str(length)
    elif length<100 :
          length="00"+str(length)
    elif length<1000 :
          length="0"+str(length)   
    elif length<10000 :
          length=str(length)         
    text = "###"+length+"###"+input_text
    text = encrypt(text)
    for i in range(int(len(text)/2)):
        tmp = str(bin(img[i]))
        tmp = tmp[:-2] + text[2*i] + text[(2*i)+1]
        tmp = int(tmp[2:], 2)
        img[i] = tmp
    return img.reshape((rows,cols,dims)).astype(numpy.ubyte)

def decrypt_image(img_path):
    img = cv2.imread(img_path,1)
    rows,cols,dims = img.shape
    img = img.flatten()
    check_data = ""
    for i in range(40):
        tmp = str(bin(img[i]))
        check_data += tmp[-2] + tmp[-1]
    if decrypt(check_data[:24])=="###":
        ln = int(decrypt(check_data[24:57]))
        data = ""
        for i in range(40,(ln*4)+40):
            tmp = str(bin(img[i]))
            data += tmp[-2] + tmp[-1]
        data = decrypt(data)
        return data    
    else:
        return None


#for encrypting use codes below
#eimage = encrypt_image("lenna.png",inputText)
#cv2.imwrite("encrypt.png",eimage)
#cv2.waitKey(0)

#for decrypting the image use the codes below
#decrypt_text = decrypt_image("encrypt.png")
#print(decrypt_text)