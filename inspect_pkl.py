import pickle

file_path = 'vectorstore/db_faiss/index.pkl'  # update path if needed

with open(file_path, 'rb') as f:
    data = pickle.load(f)

print(type(data))
print(data)
