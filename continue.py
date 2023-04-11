while True:
    s = input('输入一个单词：')
    if s == 'quit':
        break
    if len(s) < 3:
        print('太短了')
        continue
    print('单词长度有效')
