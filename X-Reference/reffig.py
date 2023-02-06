ifs = open('X-Reference/ref_tmp.bib', 'r', encoding="utf-8")
ofs = open('X-Reference/ref.bib', 'w', encoding="utf-8")


lines = ifs.readlines()
for j in range(len(lines)):
    line = lines[j][:-1]
    nline = ''
    lc = line.split()
    if len(lc):
        for i in range(len(line)):
            if line[i].isupper():
                nline += '{' + line[i] + '}'
            else:
                nline += line[i]
    ofs.write('{}\n'.format(nline))


ifs.close()
ofs.close()
