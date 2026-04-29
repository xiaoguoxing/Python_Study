try:
    with open('./1.txt', 'r') as f:
        # print(f.read(5))
        # print(f.readline())
        # print(f.readlines())
        for line in f.readlines():
            print(line)
finally:
    pass

try:
    with open('./icon.png', 'rb') as f:
        pass
        # print(f.read())
        # print(f.read(5))
        # print(f.readline())
        # print(f.readlines())
        # for line in f.readlines():
        #     print(line)
finally:
    pass
try:
    with open('./1.txt', 'r',encoding='gbk',errors='ignore') as f:
        print(f.read())
        # print(f.read(5))
        # print(f.readline())
        # print(f.readlines())
        # for line in f.readlines():
        #     print(line)
finally:
    pass
try:
    pass
    # with open('./2.txt', 'w') as f:
    #     f.write(str(list(range(101,200))))
    # with open('./2.txt', 'a') as f:
    #     f.write(str(list(range(101,200))))
finally:
    pass