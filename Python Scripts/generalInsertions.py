import json
import pandas
import mysql.connector
import pyodbc
import pymssql
import pickle

def extract():
    records=[]
    for line in open("C:\\KaranManghi\\RIT\\Semester 4\\Big Data\\Project\\user.json",encoding="utf8",mode='r'):

        records.append(json.loads(line))
    # print(records)
    pickle_out=open("user.pickle","wb")
    pickle.dump(records,pickle_out)
    pickle_out.close()
    # return records


    # return records

def connectDB(records):
    mydb = pymssql.connect(host='DESKTOP-3BKTPOD', user='sa',password='helloworld',database='yelp')

    mycursor = mydb.cursor()

    # print(records)
    val = []
    # count_i=1
    for i in records:
        # print(count_i)
        # count_i+=1
        # dates=i["friends"].split(",")
        # for j in range(len(dates)):
        val.append((i["review_id"],i["user_id"],i["business_id"],i["text"],i["date"],i["stars"]))

    print("exiting for")
    print(len(val))
    # val=(records["user_id"],records["name"],records["average_stars"])
    # print(val)
    sql = "INSERT INTO reviewTable(r_id,u_id,b_id,text,date,stars) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def insertDummyBusiness(records):
    global_categories = []
    print("Entered connectDb function ! ")
    cnx = pymssql.connect(host='DESKTOP-3BKTPOD', user='sa',password='helloworld',database='yelp')
    mycursor = cnx.cursor()
    mysql_query = "insert into business_table_allattri(business_id ,categories ,BusinessAcceptsCreditCards ,GoodForKids ,WheelchairAccessible ,DogsAllowed,Smoking,RestaurantsTableService,RestaurantsAttire,RestaurantsReservations ,RestaurantsDelivery ,RestaurantsTakeOut,RestaurantsPriceRange2 ,RestaurantsCounterService,BYOB,GoodForDancing,HairSpecializesIn,ByAppointmentOnly ,BusinessAcceptsBitcoin,BusinessParking) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    final = []
    for rec in records:
        b_id = rec["business_id"]
        temp = []
        cat = rec["categories"].split(",") if rec["categories"] else None
        # print("categories! ",cat)
        if cat is not None:
            for x in cat:
                temp.append(x.strip())
            cat = temp
        if cat is not None:
            categories = ",".join(cat)
        else:
            categories = None
        # print("categories! =",categories)
        BusinessAcceptsCreditCards = rec["attributes"] and (
            rec["attributes"]["BusinessAcceptsCreditCards"] if "BusinessAcceptsCreditCards" in rec[
                "attributes"] else None)
        GoodForKids = rec["attributes"] and (
            rec["attributes"]["GoodForKids"] if "GoodForKids" in rec["attributes"] else None)
        WheelchairAccessible = rec["attributes"] and (
            rec["attributes"]["WheelchairAccessible"] if "WheelchairAccessible" in rec["attributes"] else None)
        DogsAllowed = rec["attributes"] and (
            rec["attributes"]["DogsAllowed"] if "DogsAllowed" in rec["attributes"] else None)
        Smoking = rec["attributes"] and (rec["attributes"]["Smoking"] if "Smoking" in rec["attributes"] else None)
        if Smoking is not None:
            if Smoking[0] == "u":
                Smoking = eval(Smoking)
        RestaurantsTableService = rec["attributes"] and (rec["attributes"]["RestaurantsTableService"] if "RestaurantsTableService" in rec["attributes"] else None)
        RestaurantsAttire = rec["attributes"] and (rec["attributes"]["RestaurantsAttire"] if "RestaurantsAttire" in rec["attributes"] else None)
        RestaurantsReservations = rec["attributes"] and (rec["attributes"]["RestaurantsReservations"] if "RestaurantsReservations" in rec["attributes"] else None)
        RestaurantsDelivery =  rec["attributes"] and (rec["attributes"]["RestaurantsDelivery"] if "RestaurantsDelivery" in rec["attributes"] else None)
        RestaurantsTakeOut =rec["attributes"] and (rec["attributes"]["RestaurantsTakeOut"] if "RestaurantsTakeOut" in rec["attributes"] else None)
        RestaurantsPriceRange2 = rec["attributes"] and (rec["attributes"]["RestaurantsPriceRange2"] if "RestaurantsPriceRange2" in rec["attributes"] else None)
        RestaurantsCounterService= rec["attributes"] and (rec["attributes"]["RestaurantsCounterService"] if "RestaurantsCounterService" in rec["attributes"] else None)
        BYOB =rec["attributes"] and (rec["attributes"]["BYOB"] if "BYOB" in rec["attributes"] else None)
        GoodForDancing =rec["attributes"] and (rec["attributes"]["GoodForDancing"] if "GoodForDancing" in rec["attributes"] else None)
        HairSpecializesIn = rec["attributes"] and (rec["attributes"]["HairSpecializesIn"] if "HairSpecializesIn" in rec["attributes"] else None)
        ByAppointmentOnly= rec["attributes"] and (rec["attributes"]["ByAppointmentOnly"] if "ByAppointmentOnly" in rec["attributes"] else None)
        BusinessAcceptsBitcoin = rec["attributes"] and (rec["attributes"]["BusinessAcceptsBitcoin"] if "BusinessAcceptsBitcoin" in rec["attributes"] else None)
        BusinessParking = rec["attributes"] and (rec["attributes"]["BusinessParking"] if "BusinessParking" in rec["attributes"] else None)
        BusinessParking = str(BusinessParking)
        global_categories.append(categories)
        temp_record = (
        b_id, categories,BusinessAcceptsCreditCards, GoodForKids, WheelchairAccessible, DogsAllowed, Smoking,RestaurantsTableService,RestaurantsAttire,RestaurantsReservations ,RestaurantsDelivery ,RestaurantsTakeOut,RestaurantsPriceRange2 ,RestaurantsCounterService,BYOB,GoodForDancing,HairSpecializesIn,ByAppointmentOnly ,BusinessAcceptsBitcoin,BusinessParking)
        final.append(temp_record)
    print("Starting to execute!")
    mycursor.executemany(mysql_query,final)
    print("Executed!")
    cnx.commit()
    cnx.close()

if __name__ == '__main__':
    # extract()
    pickle_in = open("business.pickle", "rb")
    records = pickle.load(pickle_in)

    # connectDB(records)

    insertDummyBusiness(records)
    # print(records[0])

