
# coding: utf-8


import random

class RSA_Algorithm:
    
    
    def main():
    
        RSA_Algorithm.generateEncryptionDecryptionKeys()
    
    
    #gcd method for generating gcd of two given numbers
    def gcd(x, y):
        
        while y != 0:
            x, y = y, x % y
        
        return x


    #extendedgcd method is for helping to find the mode inverse.
    def extendedgcd(i, j):

        if i==0:
            return(j,0,1)
        r,s,t = RSA_Algorithm.extendedgcd(j%i, i)
        
        return (r,t -(j//i)* s,s)
    
    
    #findModInverse method is for generating mode inverse when sending two numbers as parameters
    def findModInverse(o, m):

        r,s,t = RSA_Algorithm.extendedgcd(o, m)
        if r != 1:
            raise Exception('No modular inverse')
            
        return s%m

    
    #isPrime method use to check whether the number is prime or not
    def isPrime(num):
        
        if(num==2):
            return True
        elif((num<2) or ((num%2)==0)):
            return False
        elif(num>2):
            for i in range(2,num):
                if not(num%i):
                    return False
        return True

    
    #isCoPrime method use to check whether the two given number are co-prime or not
    def isCoPrime(a,b):
        
        return RSA_Algorithm.gcd(a, b) == 1

    
    
    def generateEncryptionDecryptionKeys():
       
        primeList = []
        for i in range(0,50):
            #Generating random Numbers in the range of 10 to 100
            no = random.randint(10,100)
            #check whether they are prime numbers or not by calling isPrime method
            if RSA_Algorithm.isPrime(no) == True:
                primeList.append(no)
            
        #1.Randomly choosing prime numbers for p and q from primeList array   
        p = random.choice(primeList)
        print('P is:',str(p))
        q = random.choice(primeList)
        print('Q is:',str(q))
        
        #2.Find the n by multiplying p and q
        n = p * q
        #3.calculating phy(n) using below equation
        phyN = (p-1)*(q-1)
        
        print('N is: ',n)
        print('Phy(n) is: ',phyN)
        
        #4.generating e by using below for loop. e should be a prime and co prime of e and n
        while True:
            num=2
            for num in range(phyN):
                if(1<num<phyN):
                    if RSA_Algorithm.isPrime(num)== True:
                        if RSA_Algorithm.isCoPrime(num,phyN)== True:
                            e=num;
                            break
                            
            if RSA_Algorithm.gcd(e, phyN) == 1:
                break


       #5. Generating d using below equation by using fineModInverse method
        d = RSA_Algorithm.findModInverse(e, phyN)
        
        #6.Assigning decrytion key and encrytion key to variables
        EncryptionKey = e,n
        DecryptionKey = d,n
        
        print('Encryption Key(Public key):', EncryptionKey)
        print('Decryption Key(Private key):', DecryptionKey)
        
        #6.calls the method that use to save encryption and decrytion keys
        RSA_Algorithm.generateKeyFiles(e,n,d)
        

    #use to save encryption and decrytion keys in to text files
    def generateKeyFiles(e,n,d):

        e = str(e)
        d = str(d)
        n = str(n)

       #open the file and writing encrytion key
        with open('EncryptionKeyFile.txt', 'w') as en:
            en.write(e)
            en.write(",")
            en.write(n)
            en.write(",")
            en.close()
        print("Encrytion key is successfully saved to the file!")
        
        #open the file and writing encrytion key   
        with open('DecryptionKeyFile.txt', 'w') as de:
            de.write(d)
            de.write(",")
            de.write(n)
            de.write(",")
            de.close()
        print("Decryption key is successfully saved to the file!")

RSA_Algorithm.main()



        

