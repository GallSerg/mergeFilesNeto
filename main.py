def merge_files(filenames, output):
    file_list = []
    for file in filenames:
        with open(file, 'r', encoding='UTF-8') as f:
            q = f.readlines()
            file_list.append((f.name, len(q), *q))
    with open(output, 'w', encoding='UTF-8') as output:
        for tup in sorted(file_list, key=lambda x: x[1]):
            print(tup[0], '\n', tup[1], '\n', *tup[2:], sep='', file=output)


merge_files(['1.txt', '2.txt', '3.txt'], 'output.txt')

