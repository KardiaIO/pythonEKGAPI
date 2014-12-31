## this code sets up a simple python server that awaits instructions from
## our Node.js server using Zerorpc

import zerorpc
import psycopg2
import os
# from mssql import connect
dbname = os.getenv('POSTGRES_DBNAME')
user = os.getenv('POSTGRES_USER')
host = os.getenv('POSTGRES_HOST')
password = os.getenv('POSTGRES_PASS')
port = os.getenv('POSTGRES_PORT')

try:
  conn = psycopg2.connect("dbname=" + dbname + " user=" + user + " host=" + host + " password=" + password + " port=" + port)
except:
  print "I am unable to connect to the database"

def connect():  
  cursor = conn.cursor()

  try:
    print "DO YOUSE WORK?"
    cursor.execute(" " "SELECT * from users" " ")
  except:
    print "Can't select from users"

  rows = cursor.fetchall()
  return rows

class rpc(object):
    print "Python server ENGAGE!"

    # receives confirmation from Node server 
    def hello(self, name):
        print "Node greeting request received, response sending..."
        return "This is python. Hello, %s" % name

    def nodeRequest(self):
        print "Node data request received, response sending..."
        return connect()   

server = zerorpc.Server(rpc(), heartbeat=None)
server.bind("tcp://*:5000")
server.run()