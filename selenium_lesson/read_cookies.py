import pickle

with open('./my_cookies.dat', 'rb') as f:
    print(pickle.load(f))