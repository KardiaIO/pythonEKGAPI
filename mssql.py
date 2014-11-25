import pypyodbc

def connect(self, startTime, endTime):
  # fill this in
  conn = pypyodbc.connect('Driver=FreeTDS;Server=ekgsql.cloudapp.net;port=1433;uid=ekgwebapp;pwd=ekgsqlserver1MSSS;database=SampleData')
  # send queries along this connection - this sample query grabs the first row of data from the table
  print 'Returning query results...'
  results = conn.cursor().execute('SELECT x, y FROM SampleData.dbo.sampleekg WHERE x >= ' + startTime + ' AND x < ' + endTime).fetchall()
  return results