import pickle
pickle_in = open("checkin.pickle", "rb")
records = pickle.load(pickle_in)

# records=records[0:15]
# count_i=0
# for i in records:
#     count_i+=1
#     print(count_i)
#     dates = i["date"].split(",")
#     # dates=list(dict.fromkeys(dates))
#     # dates_temp=[]
#     dates_count=[1]*len(dates)
#     for j in range(len(dates)):
#         for k in range(len(dates)):
#             if j!=k:
#                 if dates[j]==dates[k]:
#                     # print(i)
#                     dates_count[j]+=1
#                     # print(dates[j])
#                     # dates.remove(dates[j])
#                     # dates_temp.append()
#                     print("element removed")
#     # i["date"]=",".join(str(x) for x in dates)
#     dates_count = ",".join(str(x) for x in dates_count)
#     # print(dates_count)
#     i.update({'dates_count':dates_count})
#     # print(i)
# pickle_out=open("checkin.pickle","wb")
# pickle.dump(records,pickle_out)
# pickle_out.close()

count=1
count_rec=0
count1=1
# records=records[0:2]
final_list=[]
for i in records:
    temp_list=[]
    dates = i["date"].split(",")
    for k in range(len(dates)):
        dates[k]=dates[k].strip()
    # print(count1)
    # count1+=1
    # temp_list.append(i["business_id"])
    temp=[i["business_id"]]
    for j in range(len(dates)):
        temp_list.append((dates[j],dates.count(dates[j])))
        if dates.count(dates[j]) >1:
            print("same")
    temp_list=list(set(temp_list))
    temp_list=temp+temp_list
    final_list.append(temp_list)
pickle_out=open("changedCheckin.pickle","wb")
pickle.dump(final_list,pickle_out)
pickle_out.close()
# print(final_list)
    # for j in range(len(dates)):
    #     for k in range(len(dates)):
    #         if j!=k:
    #             if dates[j].strip()==dates[k].strip():
    #                 print("same")
    # one="".join(list(set(dates))).strip()
    # two="".join(dates).strip()
    # count_rec+=1
    # print("rec count ",count_rec)

    # if one!=two:
    #     # print(i)
    #     count+=1
    # print(count)

# print(records[161949]['date'])