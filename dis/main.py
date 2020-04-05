'''
very simple example that diff between the instruction number
    1 - regular looping
    2 - list comprehensions 
'''
import dis

def regular_loop():
    cube_numbers = []
    for n in range(0,10):
        if n % 2 == 1:
            cube_numbers.append(n**3)

def list_comp():
    cube_numbers = [n**3 for n in range(1,10) if n%2 == 1]


print(dis.dis(regular_loop), "\n--------------------")
print(dis.dis(list_comp), "\n--------------------")


'''
very simple example that diff between the instruction number
    1 - regular looping
    2 - sets (unions)
'''
a = [1,2,3,4,5]
b = [2,3,4,5,6]
overlaps = []

def regular_loop_1():
    for x in a:
        for y in b:
            if x==y:
                overlaps.append(x)

def sets_():
    overlaps = set(a) & set(b)

print(dis.dis(regular_loop_1), "\n--------------------")
print(dis.dis(sets_), "\n--------------------")