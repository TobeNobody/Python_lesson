def int_func(text):
    return text.title()

def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)

output = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output.append(int_func(word))

print(" ".join(output))
