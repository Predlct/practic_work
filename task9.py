list = "performer - track1\n performer2 - track2\n performer3 - track3\n performer4 - track4\n performer5 - track5"

father_list = list.splitlines()

nlist = father_list[::-1]

mather_list = '\n'.join(nlist)

print(mather_list)

