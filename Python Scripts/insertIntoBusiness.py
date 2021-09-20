import pymssql
import pickle

def connectDb(records):
    global_categories =[]
    print("Entered connectDb function ! ")
    cnx = pymssql.connect(host='DESKTOP-3BKTPOD', user='sa',password='helloworld',database='yelp')
    mycursor = cnx.cursor()
    mysql_query = "insert into businessTable(business_id ,name,categories ,monday ,tuesday ,wednesday ,thursday ,friday ,saturday ,sunday ,state ,postal_code ,address ,city ,BusinessAcceptsCreditCards ,GoodForKids,WheelchairAccessible ,DogsAllowed,Smoking) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    final =[]
    count =0
    for rec in records:
        b_id = rec["business_id"]
        temp =[]
        name = rec["name"]
        cat = rec["categories"].split(",") if rec["categories"] else None
        #print("categories! ",cat)
        if cat is not None:
            for x in cat:
                temp.append(x.strip())
            cat = temp
        if cat is not None:
            categories = ",".join(cat)
        else:
            categories = None
        #print("categories! =",categories)
        if rec["hours"]:
            monday = rec["hours"]["Monday"] if "Monday" in rec["hours"] else None
            tuesday =rec["hours"]["Tuesday"] if "Tuesday" in rec["hours"] else None
            wednesday = rec["hours"]["Wednesday"] if "Wednesday" in rec["hours"] else None
            thursday =rec["hours"]["Thursday"] if "Thursday" in rec["hours"] else None
            friday = rec["hours"]["Friday"] if "Friday" in rec["hours"] else None
            saturday =rec["hours"]["Saturday"] if "Saturday" in rec["hours"] else None
            sunday =rec["hours"]["Sunday"] if "Sunday" in rec["hours"] else None
        else:
            monday= None
            tuesday = None
            wednesday = None
            thursday = None
            friday = None
            saturday = None
            sunday = None
        state = rec["state"] if "state" in rec else None
        postal_code = rec["postal_code"] if "postal_code" in rec else None
        if postal_code is not None:
            if postal_code=="":
                postal_code = None
            elif postal_code[0] == "u":
                postal_code = eval(postal_code)
        address = rec["address"] if "address" in rec else None
        city = rec["city"] if "city" in rec else None
        BusinessAcceptsCreditCards =rec["attributes"] and (rec["attributes"]["BusinessAcceptsCreditCards"] if "BusinessAcceptsCreditCards" in rec["attributes"] else None)
        GoodForKids = rec["attributes"] and (rec["attributes"]["GoodForKids"] if "GoodForKids" in rec["attributes"] else None)
        WheelchairAccessible =rec["attributes"] and  (rec["attributes"]["WheelchairAccessible"] if "WheelchairAccessible" in rec["attributes"] else None)
        DogsAllowed =rec["attributes"] and (rec["attributes"]["DogsAllowed"] if "DogsAllowed" in rec["attributes"] else None)
        Smoking = rec["attributes"] and (rec["attributes"]["Smoking"] if "Smoking" in rec["attributes"] else None)
        if Smoking is not  None:
            if Smoking[0] =="u":
                Smoking = eval(Smoking)
        global_categories.append(categories)
        temp_record = (b_id,name, categories, monday, tuesday, wednesday, thursday, friday, saturday, sunday, state, postal_code, address,
                city, BusinessAcceptsCreditCards, GoodForKids,WheelchairAccessible, DogsAllowed, Smoking)
        final.append(temp_record)
    print("Starting to execute!")
    mycursor.executemany(mysql_query,final)
    print("Executed!")
    cnx.commit()
    cnx.close()
    return global_categories

if __name__ == '__main__':
    # extract()
    pickle_in = open("business.pickle", "rb")
    records = pickle.load(pickle_in)
    connectDb(records)
    # print(records[0])