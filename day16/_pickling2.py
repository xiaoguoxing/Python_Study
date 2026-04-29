import pickle
with open('./1.txt','rb') as f:
    L=pickle.load(f)
    print(L)