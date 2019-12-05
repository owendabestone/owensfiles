def open_loc(options, list1, list2):

#this function returns a list of options that has not yet been selected by list1 and list2 
    
        location_open  = []
        
        for num in options:
            
            if ((num in list1) == False) and ((num in list2) == False):
                
                location_open.append(num)
        
        return location_open 