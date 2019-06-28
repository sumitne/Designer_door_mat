n, o = input("Enter dimensions separated by space    ").split()
n = int(n)
o = int(o)
l = int(((n - 1) / 2))
j = int((o - 3) / 2)
k = j
m = 1
w = int((o - 7) / 2)

for i in range(l):
    print('-' * k, end='')
    print('.|.' * m, end='')
    m += 2
    print('-' * k, end='')
    k -= 3
    print("")

print('-' * w, end='')
print('WELCOME', end='')
print('-' * w)
k += 3
m -= 2
for i in range(l):
    print('-' * k, end='')
    print('.|.' * m, end='')
    m -= 2
    print('-' * k, end='')
    k += 3
    print("")

