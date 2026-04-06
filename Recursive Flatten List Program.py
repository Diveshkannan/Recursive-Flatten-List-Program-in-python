List=[[[[[[[[[[[[1]]]]],5,6]]]]]]]
def flatten(x,result=None):
    if result is None:
        result=[]
    for i in x:
        if isinstance(i,list):
            flatten(i,result)
        else:
            result.append(i)
    return result
print(flatten(List))
    
