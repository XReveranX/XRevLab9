#Генератор, применяющий заданную функцию к каждому элементу последовательности N раз.

def func(x):
    print(x)

def besk_posl(N):
    numb = 2
    while True:
        b=0
        for i in range(8):
            if ((numb % (i+2)) == 0) and (b==0):
                b=1
            elif (b==0):
                for i in range(N):
                    yield (func(numb))
                    b=1
        numb += 1

a=besk_posl(2)
for i in a:
    None


'''
def gener(posl, N):
    for j in posl:
        for i in range(N):
            yield (func(j))

posl=range(0,111,3)
a=gener(posl, 2)
for i in a:
    None
'''
