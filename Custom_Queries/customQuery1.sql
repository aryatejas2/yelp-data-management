SELECT userTable.name,reviewTable.text,reviewTable.stars FROM businessTable join reviewTable on businessTable.business_id=reviewTable.b_id join userTable on reviewTable.u_id=userTable.u_id where businessTable.name='Arizona Biltmore Golf Club' and businessTable.postal_code='85016' ;