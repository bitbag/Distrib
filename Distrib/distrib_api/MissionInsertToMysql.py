__author__ = 'Administrator'
import MySQLdb as mysqldb

def MissionInsertToMysql(host,playbook,status):
    conn = mysqldb.connect()