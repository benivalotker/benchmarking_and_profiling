import timeit

FibArray = [0,1]
input_list = range(100)

def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 

'''
what is faster?
'''
def generator_():
    res = (i for i in input_list if fibonacci(i)) 

def list_():
    res = [i for i in input_list if fibonacci(i)]       
   
def tuple_list():
    res = list((i for i in input_list if fibonacci(i)))

'''
timeit argument:
    * stmt - callable object or string
    * setup - code running before stmt run
    * number - stmt execute number
'''
time = timeit.timeit(generator_, number=100000)
print("generator = ", time)

time = timeit.timeit(list_, number=100000)
print("list = ", time)

time = timeit.timeit(tuple_list, number=100000)
print("tuples list = ", time)




