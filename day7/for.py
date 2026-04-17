# for
AI = ['agent','skills','mcp','cli','prompt','token','tool','LLM','context']
for item in AI:
    print(item)

count = 0
for num in [1,2,3,4,5,6,7,8,9]:
    count = count+num
print(count)

count2 = 0
for num in list(range(101)):
    count2 = count2+num
print(count2)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

for item in AI:
    print(f'hello, {item}!')

x = 1
while x < 100:
    if x>=10:
        break
    #print(x)
    x = x + 1
#print('END')
y = 1
while y < 10:
    y = y + 1
    if y % 2 == 1:
        continue
    print(y)
print('END')