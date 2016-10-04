def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    flattend_list=[]
    for i in aList:
        if type(i) is list:
            flattend_list += flatten(i)
        else:
            flattend_list.append(i)
    return flattend_list

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(l))