def behdashtoSalamat(x,n) :
    if n == 0 :
        return "20"
    elif n > 0 and n!= 7 :
        if new_x < 0 :
            return 0
        return new_x

    elif n == 7 :
        return x


x = int(input())
n = int(input())
new_x = x - n
print(behdashtoSalamat(x,n))


