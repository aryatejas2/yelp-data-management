SELECT tab1.name from  (
SELECT b1.name, b1.business_id ,count(rev1.r_id) as count1 from businessTable as b1 join restaurantTable as r1 on b1.business_id = r1.business_id join reviewTable as rev1 on b1.business_id = rev1.b_id where b1.postal_code='89121' group by b1.business_id,b1.name) as tab1

join

( SELECT b2.name, b2.business_id ,count(rev2.r_id) as count2 from businessTable as b2 join restaurantTable as r2 on b2.business_id = r2.business_id join reviewTable as rev2 on b2.business_id = rev2.b_id where b2.postal_code='89121' and rev2.stars>3 group by b2.business_id,b2.name) as tab2

ON tab1.business_id=tab2.business_id WHERE count2/count1 >0.5;