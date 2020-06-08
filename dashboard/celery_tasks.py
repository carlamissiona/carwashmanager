from celery import task 
import logging 

@task
def agent_activity( userid, stockid, operation ):
     # print("Agent : ",userid, " Has action ongoing")
     # print("stockid : ",   
    str1 = "  Agent : "+ str(userid) +" Has action ongoing "  
    print(str1)
    logging.warning(str1)
 	# logging.warning("stockid : ", stockid ," is traced with operation : ", operation )
 	# logging.warning('From Celery')
    return str1
