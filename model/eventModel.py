from common.util import utils
from manager import db_manager

#eventModel
def setGoogleEvents(event_hashkey,calendar_hashkey,event_id,summary,start_date,end_date,created,updated,location):
	return db_manager.query(
								"INSERT INTO EVENT " 
								"(event_hashkey,calendar_hashkey,event_id,summary,start_dt,end_dt,created_dt,updated_dt,location) "
								"VALUES "
								"(%s, %s, %s, %s, %s, %s, %s, %s, %s) ",
								(			
									event_hashkey,calendar_hashkey,event_id,summary,start_date,end_date,created,updated,location
								)
							)
#caldav
def setCaldavEvents(event_hashkey,calendar_hashkey,event_id,summary,start_dt,end_dt,created_dt,updated_dt,location,caldav_event_url,caldav_etag):
	return db_manager.query(
								"INSERT INTO EVENT " 
								"(event_hashkey,calendar_hashkey,event_id,summary,start_dt,end_dt,created_dt,updated_dt,location,caldav_event_url,caldav_etag) "
								"VALUES "
								"(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ",
								(			
									event_hashkey,calendar_hashkey,event_id,summary,start_dt,end_dt,created_dt,updated_dt,location,caldav_event_url,caldav_etag
								)
							)	

def updateEvents(summary,start_date,end_date,created,updated,location,event_id):
	return db_manager.query(
								"UPDATE EVENT set " 								
								"summary = %s, "
								"start_dt = %s, "
								"end_dt = %s, "
								"created_dt = %s, "
								"updated_dt = %s, "
								"location = %s "
								"where event_id = %s",
								(			
									summary,start_date,end_date,created,updated,location,event_id
								)
							)

def deleteEvents(event_id):
	return db_manager.query(
								"DELETE from EVENT " 								
								"where event_id = %s",
								(			
									event_id,
								)
							)
def getEventsBackward(user_hashkey,standard_date,pager,rangee):

	return utils.fetch_all_json(				
				db_manager.query(
					"SELECT * FROM "
					"( " 
					"SELECT CALENDAR.calendar_hashkey,EVENT.created_dt,EVENT.end_dt,CALENDAR.calendar_name,EVENT.event_hashkey,EVENT.recurrance,EVENT.start_dt,EVENT.summary,EVENT.location,EVENT.state " 
					"FROM USERACCOUNT "
					"INNER JOIN CALENDAR ON USERACCOUNT.account_hashkey = CALENDAR.account_hashkey " 
					"INNER JOIN EVENT on CALENDAR.calendar_hashkey = EVENT.calendar_hashkey " 
					"WHERE user_hashkey = %s  AND start_dt < %s " 
					"ORDER BY start_dt DESC LIMIT %s,%s "
					") "
					"AS source "
					"ORDER BY start_dt "
					,
					(			
						user_hashkey,standard_date,pager,rangee
					)
				)

			)	
# def getEventsBackward(user_hashkey,)
def getEventsForward(user_hashkey,standard_date,pager,rangee):

	return utils.fetch_all_json(				
				db_manager.query(
					"SELECT CALENDAR.calendar_hashkey,EVENT.created_dt,EVENT.end_dt,CALENDAR.calendar_name,EVENT.event_hashkey,EVENT.recurrance,EVENT.start_dt,EVENT.summary,EVENT.location,EVENT.state "
					"FROM USERACCOUNT " 							
					"INNER JOIN CALENDAR ON USERACCOUNT.account_hashkey = CALENDAR.account_hashkey "
					"INNER JOIN EVENT on CALENDAR.calendar_hashkey = EVENT.calendar_hashkey " 
					"WHERE user_hashkey = %s AND start_dt >= %s " 					
					"ORDER BY start_dt "
					"limit %s,%s",
					(			
						user_hashkey,standard_date,pager,rangee
					)
				)

			)
#오늘날자부터 과거 3개 미래 4개 가져오는 쿼리
def getEventsFirst(user_hashkey,standard_date,start_range,end_range):

	return utils.fetch_all_json(				
				db_manager.query(
					"( "
					"SELECT CALENDAR.calendar_hashkey,EVENT.created_dt,EVENT.end_dt,CALENDAR.calendar_name,EVENT.event_hashkey,EVENT.recurrance,EVENT.start_dt,EVENT.summary,EVENT.location,EVENT.state FROM USERACCOUNT "
					"INNER JOIN CALENDAR ON USERACCOUNT.account_hashkey = CALENDAR.account_hashkey " 							
					"INNER JOIN EVENT on CALENDAR.calendar_hashkey = EVENT.calendar_hashkey "+
					"WHERE start_dt > (" 
					"SELECT SYNC_END.ctime FROM USERACCOUNT INNER JOIN SYNC_END ON USERACCOUNT.account_hashkey = SYNC_END.account_hashkey ORDER BY SYNC_END.ctime LIMIT 1 " +
					") "
					"AND user_hashkey = %s AND start_dt < %s ORDER BY start_dt DESC LIMIT %s ) "
					"UNION "
					"( "
					"SELECT CALENDAR.calendar_hashkey,EVENT.created_dt,EVENT.end_dt,CALENDAR.calendar_name,EVENT.event_hashkey,EVENT.recurrance,EVENT.start_dt,EVENT.summary,EVENT.location,EVENT.state FROM USERACCOUNT "
					"INNER JOIN CALENDAR ON USERACCOUNT.account_hashkey = CALENDAR.account_hashkey "
					"INNER JOIN EVENT on CALENDAR.calendar_hashkey = EVENT.calendar_hashkey "
					"WHERE start_dt > ("
					"SELECT SYNC_END.ctime FROM USERACCOUNT INNER JOIN SYNC_END ON USERACCOUNT.account_hashkey = SYNC_END.account_hashkey ORDER BY SYNC_END.ctime LIMIT 1"
					") " 
					"AND user_hashkey = %s AND start_dt >= %s ORDER BY start_dt limit %s ) "
					"ORDER BY start_dt "
					  ,
					(			
						user_hashkey,standard_date,start_range,user_hashkey,standard_date,end_range
					)
				)

			)
