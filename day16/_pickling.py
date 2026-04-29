import pickle
L = {'abc':'123','def':'456','ghi':'789'}
with open('./1.txt','wb') as f:
    pickle.dump(L,f)