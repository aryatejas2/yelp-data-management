SELECT tab1.name from

(SELECT b1.name, b1.business_id,count(rev1.r_id) as count1 from friendsTable as f1 join userTable as u1 on f1.u_id=u1.u_id join reviewTable as rev1 on f_id=rev1.u_id join businessTable as b1 on rev1.b_id=b1.business_id join restaurantTable as r1 on b1.business_id=r1.business_id where rev1.stars>4  and u1.u_id='ZMQPf4ip21H6IYWSzBiwgQ' group by b1.business_id,b1.name) as tab1

join

(SELECT b2.name,b2.business_id,count(rev2.r_id) as count2 from friendsTable as f2 join userTable u2 on f2.u_id=u2.u_id join reviewTable as rev2 on f_id=rev2.u_id join businessTable as b2 on rev2.b_id=b2.business_id join restaurantTable as r2 on b2.business_id=r2.business_id where rev2.stars<3 and u2.u_id='ZMQPf4ip21H6IYWSzBiwgQ'  group by b2.business_id,b2.name) as tab2

ON tab1.business_id=tab2.business_id WHERE count1>count2 ;