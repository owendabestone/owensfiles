def find_pos1(string,symbol):
    # this function returns a list of position values of where the symbol is located
    
    output = []
    
    last_position = string.find(symbol)
    
    output.append(last_position)
    
    
    while last_position != -1:
        
        output.append(string.find(symbol,last_position + 1))
        
        last_position = output[-1]
        
    output = output[0:-1]    
    
    
    return output  