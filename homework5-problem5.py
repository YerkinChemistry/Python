text = open('problem5text.txt', 'w', encoding='utf-8')
text_in = [el for el in range(10)]
for el in text_in:
    text.write(' ')
    text.write(str(el))
print(sum(text_in))
text.close()
