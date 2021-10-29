def func(s=[], n=int(input("chislo n:"))):
    print(' для окончания ввода  напишите 0')
    a = int(input('-->> '))
    while True:
        if a==0 :
           break
        else :
            s.append(a)
            a = int(input('-->> '))
    for i in s:
        if n < i:
            print(i)

f = func ([]);
