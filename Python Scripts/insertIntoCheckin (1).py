import pickle
import pymssql

# pickle_in = open("changedCheckin1.pickle", "rb")
# records = pickle.load(pickle_in)

# print(records[0])

def connectDB(records):
        mydb = pymssql.connect(host='DESKTOP-3BKTPOD', user='sa',password='helloworld',database='yelp')

        mycursor = mydb.cursor()


        val = []
        count_i=1
        for i in records:
            # print(i)
            print(count_i)
            count_i+=1
            # dates=i["friends"].split(",")
            # for j in range(len(dates)):
            for j in range(1,len(i)):
                val.append((i[0],i[j][0],str(i[j][1])))
                # print(val)


        print("exiting for")
        # print(val[0][2])
        # val=(records["user_id"],records["name"],records["average_stars"])
        # print(val)
        sql = "INSERT INTO checkinTable(b_id,date,occurence) VALUES (%s,%s,%s)"
        mycursor.executemany(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

if __name__ == '__main__':
    # extract()
    pickle_in = open("changedCheckin.pickle", "rb")
    records = pickle.load(pickle_in)
    connectDB(records)
    # print(records[0])
