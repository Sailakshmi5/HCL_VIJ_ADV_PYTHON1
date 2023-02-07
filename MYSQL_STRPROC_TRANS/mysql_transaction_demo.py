from hcl_database_connection import MyDatabaseConnection
class HclPythonTransaction(MyDatabaseConnection):
    def execute_transaction_query(self):
        custid=2
        sql="delete from customer where cust_id=%s"
        try:
            self.cursor.execute(sql,(custid,))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("something goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connect_obj=HclPythonTransaction()
connect_obj.connect("localhost","root","root@123","hcl_vijayawada")
connect_obj.execute_transaction_query()