#-*- coding: utf-8 -*-
# author : yenos
# descript : static 변수선언.

#로그인 상태관리
LOGIN_STATE_FIRST = 'LOGIN_STATS_SIGNUP'
LOGIN_STATE_AUTO = 'LOGIN_STATE_AUTO'
LOGIN_STATE_OTHERDEVICE = 'LOGIN_STATE_OTHERDEVICE'
LOGIN_STATE_RELOGIN = 'LOGIN_STATE_RELOGIN'

#로그인 에러상황
LOGIN_ERROR_INVALID = 'inValid sessionkey!'
LOGIN_ERROR = 'LOGIN_ERROR'

#캘린더 완료 일경우.
CALENDAR_PUSH_STATE_BEFORE = "1"
CALENDAR_PUSH_STATE_AFTER = "2"
CALENDAR_PUSH_SYNC_END = "3"

#구글 만기 예정 safe time
EXPIRE_SAFE_RANGE = 180

 
#일정 리스트 보여줄 갯수
EVENTS_FORWARD_CNT = 6
EVENTS_BACKWARD_CNT = 6
EVENTS_ITEM_CNT = 6

#싱크 이넘관리
SYNC_CALDAV_SUCCESS = "SYNC_STATE_CALDAV_SUCCES"
SYNC_CALDAV_ERR_SET_CALENDAR = "SYNC_STATE_CALDAV_ERR_SET_CALENDAR"
SYNC_CALDAV_ERR_SET_EVENTS = "SYNC_STATE_CALDAV_ERR_SET_EVENTS"
SYNC_CALDAV_ERR_SET_SYNC_TIME = "SYNC_STATE_CALDAV_ERR_SET_SYNC_TIME"
SYNC_CALDAV_ERR_SET_SYNC_END = "SYNC_CALDAV_ERR_SET_SYNC_END"


SYNC_GOOGLE_SUCCES = "SYNC_GOOGLE_SUCCES"
SYNC_GOOGLE_ERR_SET_CALENDAR = "SYNC_GOOGLE_ERR_SET_CALENDAR"



#응담 메시지들
MSG_LOGIN_AUTO = 'auto login success'
MSG_LOGIN_SIGNUP = 'first sign up'
MSG_LOGIN_COMPLUSION_UPDATE = 'need compulsion update'

MSG_INVALID_TOKENKEY = 'invalid token key'
MSG_EVENTS_END = 'data end'

MSG_SUCCESS_ADD_ACCOUNT = 'success add account'
MSG_FAILE_ADD_ACCOUNT_REGISTERD = 'already registerd'
MSG_LOGOUT_SUCCESS = 'log out success'

#구글 아직 로딩중. 정확한 결과는 푸시
MSG_SUCCESS_GOOLE_SYNC_LOADING = 'success sync loading'
#캘대브 성공
MSG_SUCCESS_CALDAV_SYNC = 'Caldav Sync Success'




