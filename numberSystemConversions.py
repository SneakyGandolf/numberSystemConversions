# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 00:04:09 2022

    Number System conversion Calculator
    Ability to convert all binary, 4???? octal, decimal, hexidecimal to each other using recursion

    @author: caeli
"""

import sys
'''
1. Create main and communicate with console
2. Create each conversion function --> 1,2,4,8,10,16
3. Call them respectively

    -- Potential probelms -- 
    
Hexidecimal is not an int so how do I read it in
    -Don't cast to int but have if statements to determine conversion type
        -Input string type not integer
        
    -If words are typed in miss spelled.
        -Propose I make a dictionary ex) {'decimal': 10}
        -and check keys to ensure the string entered is in the dict


'''
hexaDict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 0: '0'}


def binaryConversions(binaryNum, desiredType):
    
    sum = 0
    binaie = str(binaryNum)
    binaryN = binaie[::-1]
    return binaryN[0]
    for i in range(binaryN):
        if binaryN[i] == '1':
            sum = sum + 2**(i+1)
                
    return sum
    if desiredType == 'decimal': 
        #return int(str(binaryNum), 2)
        pass
    
    elif desiredType == 'hexadecimal':
        
        return int(str(binaryNum), 16)
        
    elif desiredType == 'octal':
        
        return int(str(binaryNum), 8)



def octalConversions(octalNum, desiredType):
    
    if desiredType == 'binary':
        pass
    
    elif desiredType == 'hexadecimal':
        pass
        
    elif desiredType == 'decimal':
        pass



def decimalConversions(deciNum, desiredType):
    
    if desiredType == 'binary':
        
        if deciNum == 0:
            return 0
        return (deciNum % 2 + 10 * decimalConversions(deciNum // 2, desiredType))
    
    elif desiredType == 'hexadecimal':
        if deciNum == 0:
            return ''
        return decimalConversions(deciNum // 16, desiredType) + hexaDict[deciNum % 16]
    #FIGURE OUT A WAY TO DO THIS WITHOUT 1-9 IN THE DICTIONARY

    elif desiredType == 'octal':
    
        if(deciNum > 0):
            # recursively calling on n/8    
            decimalConversions(int(deciNum/8), desiredType)
            # printing the remainder
            print(deciNum%8, end='')
    
'''
        result = ''
        if deciNum == 0:
            return result
        decimalConversions(deciNum // 8, desiredType)
        remainder = str(deciNum % 8)
        print('fof', remainder, decimalConversions(deciNum // 8, desiredType))

        result += remainder
'''
    




def hexadecimalConversions(hexVal, desiredType):
    
    if desiredType == 'binary':
        pass
    
    elif desiredType == 'decimal':
        pass
        
    elif desiredType == 'octal':
        pass









if __name__ == '__main__':
    
    print("Greetings. I'm a Bitwise Conversion Bot who is ready to convert at your command.")
    #Would be dope to have a multiple choice selection instead the user having to type
    startType = input("Type the start type you need converted. ex) binary, decimal, etc.\n").lower()
    '''should be a try / except
    if startType == 'binary' or startType == 'hexadecimal' or startType == 'decimal' or startType == 'octal':
        pass
    else:
        print('Du you rememeber how too spelll?')
        sys.exit(1)
    '''
    endType = input("Type the end type you want converted to. ex) octal, hexadecimal, etc.\n").lower() 
    '''should be a try / except
    if endType == 'binary' or endType == 'hexadecimal' or endType == 'decimal' or endType == 'octal':
        pass
    else:
        print('Du you rememeber how too spelll?')
        sys.exit(1)
    '''

    value = int(input("Type the integer you wish to be converted\n"))
    #check to make sure value is typed in correctly

    if startType == 'binary':
        result = binaryConversions(value, endType)
    elif startType == 'decimal':
        result = decimalConversions(value, endType)
    elif startType == 'hexadecimal':
        result = hexadecimalConversions(value, endType)
    elif startType == 'octal':
        result = octalConversions(value, endType)

    print('Result of {1} to {2} conversion --> {0}'.format(result, startType, endType))


