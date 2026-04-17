# dict
d = {'skills': 100, 'name': 90, 'pop': 50}
# d['name'] = 110
# print('name' in d)
# print(d.get('name'))
# d.pop('pop')
# for k,v in d.items():
#     print(k,v)
# set
s = {1, 2, 3, 4, 5}
# s2 = set([1,2,3,4,5])
s.add(6)
s.remove(3)
# print(s)
s1 = {1, 2, 3, 4, 5}
s2 = {1, 6, 7, 4, 5}
# print(s1 & s2)  # 交集
# print(s1 | s2)  # 并集
# print(s1 ^ s2)  # 对称差集
# print(s1 - s2)  # 差集
# print(s2 - s1)  # 差集

# print(s1.intersection(s2))# 交集
# print(s1.union(s2))# 并集
# print(s1.difference(s2)) # 差集
# print(s1.symmetric_difference(s2)) # 对称差集

sort = ['c','b','a']
sort.sort()
print(sort)

abc = 'abc'
abc1 = abc.replace('a','A')

print(abc1)