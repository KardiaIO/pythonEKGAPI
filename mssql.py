import pypyodbc

# fill this in
conn = pypyodbc.connect('Driver=FreeTDS;Server=0.0.0.0;port=0000;uid=username;pwd=pw;database=db_name')

# send queries along this connection - this sample query grabs the first row of data from the table
print conn.cursor().execute('SELECT * FROM TABLE').fetchall()