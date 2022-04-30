
resulting_list = []

for i in range (1,4):
    filename = f'{i}.txt'
    with open(filename, mode = "r", encoding = 'utf-8') as file:
        resultfile = file.read().split('\n')
        resultfile.append(filename)
        resulting_list.append(resultfile)

with open('4.txt', mode = 'a', encoding='utf-8') as file:
    file4 = file
    sorted_resulting_list = sorted(resulting_list, key=len)
    for text in sorted_resulting_list:
        file4.write("%s\n" % text[-1])
        file4.write("%s\n" % str(len(text[0:-2])))
        for element in text[0:-2]:
            file4.write("%s\n" % element)



# file4.write('\n'.join(element).join('\n'))

