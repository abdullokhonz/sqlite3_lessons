text: str = input('>>>')
new_text: str = ''
for i in text:
    if text.count(i) == 1:
        new_text += '('
    else:
        new_text += ')'
print(new_text)
