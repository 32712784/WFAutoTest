#coding:utf-8
#------------------------------------------------------------------------------------------------------------------------------
#登陆工作流URL
wf_url = "http://27.17.30.140:11053/backend/processlist/center.aspx?classname=handlelist&type=ProcessTodoList&activeNav=ProcessTodoList"

#------------------------------------------------------------------------------------------------------------------------------
#数据库连接字符串，sqlserver连接字符串参考：http://www.asp101.com/articles/john/connstring/default.asp
conStr = "Provider=MSDASQL; Driver={SQL Server}; Server=10.5.11.4\\MSSQLSERVER2014; Database=hnqcddc_600sp3_Upgrade; UID=sa; PWD=95938;"

#------------------------------------------------------------------------------------------------------------------------------
'''
流程模板1:
步骤：A发起-A审批-A手动归档
用例范围：流程中心-场景1、流程中心-场景2、流程中心-场景3
'''
ProcessModule_1 = u"三步手动归档"

#------------------------------------------------------------------------------------------------------------------------------
'''
流程模板2:
步骤：A发起-A手动归档
用例范围：流程中心-场景4
'''
ProcessModule_2 = u"两步手动归档"

#------------------------------------------------------------------------------------------------------------------------------
#Cc:用于设定设定抄送人
Cc = u"王胜成"

#------------------------------------------------------------------------------------------------------------------------------
#HandlerName:用于设定重置责任人
HandlerName = u"王胜成"

#------------------------------------------------------------------------------------------------------------------------------
#Watcher:用于设定监控人
Watcher = u"王胜成"

#------------------------------------------------------------------------------------------------------------------------------
#Circulator:用于设定传阅人
Circulator = u"王胜成"