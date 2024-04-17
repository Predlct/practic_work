
for i1 in range(0, 9 + 1):
    for i2 in range(0, 9 + 1):
        for i3 in range(0, 9 + 1):
            for i4 in range(0, 9 + 1):
                for i5 in range(0, 9 + 1):
                    for i6 in range(0, 9 + 1):
                        if (f'{i1}{i2}{i3}{i4}{i5}{i6}' == f'{i1}{i6}{i5}{i4}{i3}{i2}' and
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 1}'[1:1+1] ==
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 1}'[5:5+1] and
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 1}'[2:2+1] ==
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 1}'[4:4+1] and
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 2}'[1:1+1] ==
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 2}'[4:4+1] and
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 2}'[2:2+1] ==
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 2}'[3:3+1] and
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 3}'[0:0+1] ==
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 3}'[5:5+1] and
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 3}'[1:1+1] ==
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 3}'[4:4+1] and
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 3}'[2:2+1] ==
                                f'{int(f'{i1}{i2}{i3}{i4}{i5}{i6}') + 3}'[3:3+1]):
                            print(int(f'{i1}{i2}{i3}{i4}{i5}{i6}'))
