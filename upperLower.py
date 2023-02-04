# function to accept string and calc num of upper and lower case nums
def upperLower(string):
    upper = 0
    lower = 0
    
    #traverse character by character
    for i in range(len(string)):
        if string[i] >= 'A' and string[i] <= 'Z':
            upper = upper + 1
        elif string[i] >= 'a' and string[i] <= 'z':
            lower = lower + 1
    print('num of upper case: ', upper)
    print('num of lower case: ', lower)
    
upperLower('The quick Brow Fox')
