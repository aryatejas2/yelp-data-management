import pickle
import json

# records=[]
# for line in open("C:\\KaranManghi\\RIT\\Semester 4\\Big Data\\Project\\review.json", encoding="utf8", mode='r'):
#     records.append(json.loads(line))
# # print(records)
# pickle_out = open("review.pickle", "wb")
# pickle.dump(records, pickle_out)
# pickle_out.close()

pickle_in = open("changedCheckin.pickle", "rb")
records = pickle.load(pickle_in)
print(len(records))
# dates=records[0]["date"].split(",")
# print(dates)
# print(records[0]["date"].count(","))
print(records[0])

# temp=records[0]['friends'].split(",")

# print(len(temp))

