import pickle

# pickle_in = open("changedCheckin1.pickle", "rb")
# records = pickle.load(pickle_in)

pickle_in = open("changedCheckin.pickle", "rb")
records = pickle.load(pickle_in)

print(records[1])