text = open('problem2.txt', 'r', encoding='utf-8')
n = 1
while True:
    a = text.readline()
    print(f"{n} -line have the following number of words:", end='')
    print(len(a.split()))
    n +=1
    if len(a.split()) == 0:
        break
print(f"overall we have {n-1} lines")
text.close()


