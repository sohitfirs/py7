# Задание 1

n = int(input())
x = set()

x = set(map(int, input().split()))

print(len(x))
print()

# Задание 2

x = []
y = []

x = list(map(int, input().split()))
y = list(map(int, input().split()))

print()

for i in range(len(x)):
    print(x[i], end=' ')
print()

for i in range(len(y)):
    print(y[i], end=' ')   
print ()

print(len(set(x).intersection(set(y))))
print()

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