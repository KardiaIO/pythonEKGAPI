## this code sets up a simple python server that awaits instructions from
## our Node.js server using Zerorpc

import zerorpc
import psycopg2
import os
import json
from RWaveAnalysis import RWaveAnalysis

# Connect to Postgres.  Use Foreman to get Environment Variables (foreman start in terminal). 
POSTGRES_DBNAME = os.getenv('POSTGRES_DBNAME')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PASS = os.getenv('POSTGRES_PASS')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

try:
  conn = psycopg2.connect("dbname=" + POSTGRES_DBNAME + " user=" + POSTGRES_USER + " host=" + POSTGRES_HOST + " password=" + POSTGRES_PASS + " port=" + POSTGRES_PORT)
except:
  print "I am unable to connect to the database"

def connectToPG():  
  cursor = conn.cursor()
  try:
    print "DO YOUSE WORK?"
    cursor.execute(" " "SELECT * from users" " ")
  except:
    print "Can't select from users"

  rows = cursor.fetchall()
  return rows

# Create Analyzer
rWaveNotch = 4.8 # amplitude
thresholdForFeatureCount = 3 # total number of features in buffer that indicate abnormality
timeSpan = .83 # seconds in between r-wave peaks that would indicate abnormality 
bufferLength = 10 # number of records to check for features
RWaveAnalyzer = RWaveAnalysis(rWaveNotch, thresholdForFeatureCount, timeSpan, bufferLength)
 
class RPC():
    print "Python server ENGAGE!"

    # receives confirmation from Node server 
    def hello(self, name):
      # print "Node greeting request received, response sending..."
      return "This is python. Hello, %s" % name

    def crunch(self, data):
      dataObj = json.loads(data)
      return RWaveAnalyzer.analyze(dataObj)

    # Used for Postgres Connection
    # def nodeRequest(self):
    #   print "Node data request received, response sending..."
    #   return connectToPG() 

server = zerorpc.Server(RPC())
server.bind("tcp://*:8000")
server.run()