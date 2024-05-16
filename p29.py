# p29.py
# Sreenivas Rajesh
# 5/15/24
# Description: program to write random numbers and sort it

import random
range1=random.randint(50,55)
myFile = open("randomNumbers.txt", 'w')
for x in range (0,range1, 1):
    myFile.write (str(random.randint(0,100)) + '\n')
myFile.close()

myFile = open("randomNumbers.txt", 'r')
fileasList = myFile.read().splitlines()
print ("randomNumbers.txt = ", fileasList)



                  

for z in range(0,len(fileasList)-1, 1):
    for x in range (0, len(fileasList) -1, 1):
        if int(fileasList[x]) > int(fileasList[x+1]):
            temp = fileasList[x]
            fileasList[x] = fileasList [x+1]
            fileasList[x+1] = temp
print("File as list = ", fileasList)

if len(fileasList)%2 != 0 :
    medianIndex = int ( len(fileasList)/2 ) 
    median1 = fileasList[medianIndex]
    print ('median =', median )

if len(fileasList) %2 == 0:
    medianIndex1 = int(len(fileasList)/2)
    medianIndex2 = int(len(fileasList)/2)-1
    median2 = (int(fileasList[medianIndex1]) +int(fileasList[medianIndex2]))/2
    print ('median =', median2)

'''
=============== RESTART: /Users/sreenivasrajesh/Documents/p29.py ===============
randomNumbers.txt =  ['43', '25', '23', '62', '94', '91', '65', '16', '21', '93', '52', '31', '59', '23', '72', '100', '15', '13', '75', '47', '40', '42', '94', '29', '2', '64', '94', '19', '48', '47', '65', '85', '75', '75', '45', '91', '32', '89', '64', '6', '94', '9', '53', '11', '100', '40', '14', '78', '23', '18', '6', '40']
File as list =  ['2', '6', '6', '9', '11', '13', '14', '15', '16', '18', '19', '21', '23', '23', '23', '25', '29', '31', '32', '40', '40', '40', '42', '43', '45', '47', '47', '48', '52', '53', '59', '62', '64', '64', '65', '65', '72', '75', '75', '75', '78', '85', '89', '91', '91', '93', '94', '94', '94', '94', '100', '100']
median = 47.0
'''
  
