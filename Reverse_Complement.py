def reverse_complement(input_seq):
    string = input_seq
    
    res = []
    res[:] = string
    res.reverse()
    # seperates the string into a list of characters and reverse the order of the list
    
    for i in range(len(string)):
        
        if (res[i] == 'A'):
            res[i] = 'T'
            
        elif (res[i] == 'T'):
            res[i] = 'A'
            
        elif (res[i] == 'C'):
            res[i] = 'G'
            
        elif (res[i] == 'G'):
            res[i] = 'C'
    
    # converts the list of DNA nucleotides to its complement.
    
    finalstring = ''.join(res)
    
    return finalstring

print("Enter a sequence:")
input_seq = input()
print(reverse_complement(input_seq))
