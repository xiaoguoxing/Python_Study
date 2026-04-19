#sorted
print(sorted([3,2,5,-7,5,3,-2,9,5]))
print(sorted([3,2,5,-7,5,3,-2,9,5],key=abs))
print(sorted(['bob','about','Zoo','Credit']))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower, reverse=True))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)
def by_score(t):
    return t[1]

L3 = sorted(L, key=by_score,reverse=True)
print(L3)