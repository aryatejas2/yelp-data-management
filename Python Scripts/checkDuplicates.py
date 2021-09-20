import pickle
pickle_in = open("checkin.pickle", "rb")
records = pickle.load(pickle_in)

count_i=0
for i in records:
    count_i+=1
    # print(count_i)
    dates_old = i["date"].split(",")
    # print(dates_old)
    non_dup_dates=list(set(dates_old))
    # print(non_dup_dates)
    if len(dates_old)!=len(non_dup_dates):
        print(count_i)
    # dates=list(dict.fromkeys(dates))
    # dates_temp=[]
    # dates_count=[1]*len(dates)
    # for j in range(len(dates)):
    #     for k in range(len(dates)):
    #         if j!=k:
    #             if dates[j]==dates[k]:
    #                 print(count_i)
    #                 # dates_count[j]+=1
    #                 # print(dates[j])
    #                 # dates.remove(dates[j])
    #                 # dates_temp.append()
    #                 print("element removed")
    # i["date"]=",".join(str(x) for x in dates)
    # dates_count = ",".join(str(x) for x in dates_count)
    # print(dates_count)
    # i.update({'dates_count':dates_count})
    # print(i)