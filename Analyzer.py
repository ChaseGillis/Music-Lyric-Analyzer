total = 0
d = {}
for i in range(65, 91):
    i = chr(i)
    d[i] = 0

filename = input('Enter a filename: ')
try:
    file = open('songs/'+filename + '.txt', 'r')
    data = file.read()
    file.close()
except FileNotFoundError:
    print('File not found.')
else:
    for i in data:
        if i.isalpha():
            total += 1
        i = i.upper()
        if i in d:
            d[i] += 1
    print('Analyzing song ...')
    print()
    print('There are a total of', format(total, ',d'), 'letters in this song!')
    print()

    print('The song contains:')
    print('Letter : Frequency')
    print(d['A'])
    for x in d:
        percent = d[x] / total
        d[x] = percent * 100


    for i in sorted(d.keys()):
        print(format(i, '^6s'), ':', format(d[i], '.2f'),'%')
