# Задание 1

n = int(input())
x = set()

x = set(map(int, input().split()))

print(len(x))

# Задание 2

x = []
y = []

x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in range(len(x)):
    if x[i] != x[-1]:
        print(x[i], end=' ')
    else:
        print(x[i])

for i in range(len(y)):
    if y[i] != y[-1]:
        print(y[i], end=' ')
    else:
        print(y[i])
print(len(x) + len(y))

# Задание 3

l = list(map(int, input().split()))
x = []
for i in l:
    if i in x:
        print('YES')
    else:
        x.append(i)
        print('NO')

input()