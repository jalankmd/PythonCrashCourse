def addfunc(L):
    ## I can use the built in sum function
    my_sum = sum(L)
    return my_sum

def multfunc(L):
    result = 1
    for i in L:
        result = result * i
    return result
    