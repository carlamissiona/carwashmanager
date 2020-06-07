from django.db import connection



def getsales_sql():
    cursor = connection.cursor()
    cursor.execute("""Select * from dashboard_sales
                    where date_part('month', pub_date) 
                    = (SELECT date_part('month',now()))""")
    row = cursor.fetchall()
    return row


    
	 # logging.warning("------------inner method------") 
     #    sales = User.objects.raw("""Select * from dashboard_sales
     #                                where date_part('month', pub_date) = 
     #                                (SELECT date_part('month',now()))""")
     #    logging.warning(" ,,,,,,,,,,,inner method,,,,,,,,,,,,") 
     #    logging.warning(sales) 
        
  
     