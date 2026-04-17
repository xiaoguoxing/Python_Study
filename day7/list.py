# list
list1 = ['1','2','3','4','5','6','7','8','9']
print('[0]:',list1[0])
print('[1]:',list1[1])
print('[-1]:',list1[-1])
# for i in range(0,len(list1)):
#     print(list1[i])
list1.append('10')
list1.insert(1,'11')
list1.pop() #删除末尾一个
list1.pop(8) #删除指定位置
list1[2] = '换了'
list1[3] = 123
list1[4] = True
list2 = ['123','abc',False]
list1[5] = list2
list3 = []
print(list1,'它的长度为：',len(list1))
list4 = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
print(list4[0][0])
print(list4[1][1])
print(list4[2][2])
