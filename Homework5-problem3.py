text = open('problem3.txt', 'r', encoding='utf-8')
print('List of employers who earns less than 20000:')
sum = 0
n = 0
while True:
    a = text.readline().split()
    if len(a) != 2:
        break
    elif float(a[1]) < 20000:
        print(a[0])
    if sum >= 0:
        n += 1
        sum = sum + float(a[1])
print('average salary:', sum/n)