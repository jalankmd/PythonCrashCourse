def addfunc(*args):
    ## I can use the built in sum function
    my_list = list(args)
    my_sum = sum(my_list)
    return my_sum

def multfunc(*args):
    my_list = list(args)
    result = 1
    for i in my_list:
        result = result * i
    return result
    