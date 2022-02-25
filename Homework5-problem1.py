text = open('text.txt', 'w+', encoding='utf-8')
while True:
    el = input('write something:')
    text.writelines(el)
    text.write('\n')
    if not el:
        break



