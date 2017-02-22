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
CALENDAR_SYNC = 2

#구글 만기 예정 safe time
EXPIRE_SAFE_RANGE = 180

 
#일정 리스트 보여줄 갯수
EVENTS_FORWARD_CNT = 6
EVENTS_BACKWARD_CNT = 6
EVENTS_ITEM_CNT = 6


MSG_LOGIN_AUTO = 'auto login success'
MSG_LOGIN_SIGNUP = 'first sign up'
MSG_LOGIN_COMPLUSION_UPDATE = 'need compulsion update'

MSG_INVALID_TOKENKEY = 'invalid token key'
MSG_EVENTS_END = 'data end'