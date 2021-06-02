
# coding: utf-8

class Decryption:

    #reading Decrytion key file
    def readDecryptKeyFile():
        
        decryptFile = open('DecryptionKeyFile.txt', 'r')
        for line in decryptFile:
            fields = line.split(",")
            d=fields[0]
            n=fields[1]
 
        D = int(d)
        N = int(n)
        print('d is:',D)
        print('n is:',N)
        decryptFile.close()
        
        Decryption.decryption(D, N)

    #reading cipher text file   
    def readCipherTextFile():
        
        decryptFile = open('CipherTextFile.txt', 'r')
        for line in decryptFile: 
            msg = line.split(",")
            
        print('Cipher Text:', msg)
        return msg
        
    #decryption methd that use to decryt the cipher text in order to retreive the plain message
    def decryption(d,n):
        
        CipherText = Decryption.readCipherTextFile()
        
        integerCode =[]
        for i in range(0, len(CipherText)-1):
            code = int(CipherText[i], 16)
            integerCode.append(code)
            
        print('Text:', integerCode) 
        
        text=[]
        msg=[]
        for i in range(0,len(integerCode)):
            
            m=(integerCode[i]**d)%n
            text.append(m)
            plainText=chr(text[i])
            msg.append(plainText)

             #writing retrieved plain text msg in to the decrypted  msg file 
            with open('DecryptedMsgFile.txt', 'a') as a:
                a.write(plainText)
                
        #print('Plian Text:',msg)
        a.close() 
        
    def main():
        
        Decryption.readDecryptKeyFile()
        
        
Decryption.main()
        
        

