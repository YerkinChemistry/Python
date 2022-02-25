rus = {'one':'', 'two':'', 'three':'', 'four':''}
with open('problem5.txt', 'w', encoding='utf-8') as file1:
    with open('problem5.txt', 'w', encoding='utf-8') as file2:
        file2.writelines([line.replace()[0], rus_dic.get(line.split()[0])) for line in file2])
            