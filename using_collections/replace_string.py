info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
print(f'You can join the parts like this {"+".join(parts)}')


info_list = []

for i in info:
    if i == ":":
        info_list.append('+')
    else:
        info_list.append(i)


print(f'The finished sentence is {"".join(info_list)}')
print(f'This also works like this {info.replace(':', '+')}')