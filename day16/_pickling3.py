import json
L = {'abc':'123','def':456,'ghi':True}
with open('./2.txt','w') as f:
    json.dump(L,f)