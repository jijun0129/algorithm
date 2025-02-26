word = input().strip()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 크로아티아 알파벳을 길이가 1인 문자로 바꾼다.
for c in cro:
    word = word.replace(c, ' ')
# 문자열의 길이가 크로아티아 알파벳의 수
print(len(word))
