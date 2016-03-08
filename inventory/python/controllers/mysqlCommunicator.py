import MySQLdb

class MySQLCommunicator(object):
  def __init__(self):
     self.con = MySQLdb.connect('localhost', 'root','','inventory')

  def executeQuery(self, stmt, parameters=None):
      try: 
        cur = self.con.cursor()
        if parameters is None:
          cur.execute(stmt)
        else:
          cur.execute(stmt,parameters)
        return cur.fetchall()
      except MySQLdb.IntegrityError as e:
	return "integrityError"

      except AttributeError, MySQLdb.OperationalError:
        self.connect()
        cur = self.conn.cursor()
        if parameters is None:
          cur.execute(stmt)
        else:
          cur.execute(stmt,parameters)
        return cur.fetchall() 
    
  def closeCursor():
     cur = self.con.cursor()
     cur.close();
         
