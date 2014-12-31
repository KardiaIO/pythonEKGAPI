## this code sets up a simple python server that awaits instructions from
## our Node.js server using Zerorpc

import zerorpc
import psycopg2
# from mssql import connect
try:
    conn = psycopg2.connect("dbname='ddkcjaloac929s' user='jtxtmxsnjirunx' host='ec2-54-83-23-169.compute-1.amazonaws.com' password='q8ojXZQTlVDqQSPy3y48CIRK0S' port='5432'")
except:
    print "I am unable to connect to the database"

def connect():  
  cursor = conn.cursor()

  try:
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

    def nodeRequest(self, startTime, endTime):
        print "Node data request received, response sending..."
        return connect()   

server = zerorpc.Server(rpc())
server.bind("tcp://0.0.0.0:4242")
server.run()