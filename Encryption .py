
# coding: utf-8

class Encryption:

    #reading encryption key file
    def readEncryptionKeyFile():

        Encryptfile = open('EncryptionKeyFile.txt', 'r')
        for line in Encryptfile:
            fields = line.split(",")
            e=fields[0]
            n=fields[1]
 
        E = int(e)
        N = int(n)
        print('e is:',E)
        print('n is:',N)
        
        Encryption.encryption(E, N)
        
     #reading plainText file   
    def readPlainTextFile():
        
        plainFile = open('plainTextFile.txt', 'r')
        for line in plainFile: 
            msg = line.split()
            
        print('Plain Text Message:',msg)
        numbers=[]
        msgSet=[]
        for i in range (0,len(msg)):
            intMSG = msg[i]

            for j in range (0,len(intMSG)):
                numbers = list(intMSG)
                msgSet.append(numbers[j])

        print('Plain Text Array:',msgSet)
        plainFile.close()
        return msgSet


            
    #Encryption method is use to encryt the plain text
    def encryption(e,n):
        
        message = Encryption.readPlainTextFile()
        
        intCode =[]
        for i in range(0, len(message)):
            cd=hex(ord(message[i]))
            intCode.append(cd)
            
        
        cipher=[]
        text=[]
        for i in range(0,len(intCode)):
            
            #calculation of the encryted value
            c = (int(intCode[i],16)**e)%n
            cipher.append(hex(c))
            cipherText = str(cipher[i])
            text.append(cipherText)
            
            #Writing cipher text in to the cipher text file
            with open('CipherTextFile.txt', 'a') as a:
                a.write(cipherText)
                a.write(",")
              
        a.close() 
            
        print('Cipher Text:',text)
        
        
    def main():
        Encryption.readEncryptionKeyFile()
        
Encryption.main()


