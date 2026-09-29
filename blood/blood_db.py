import mysql.connector

class BloodDonation():
    def __init__(self):
        self.con=mysql.connector.connect(user='root',password='aiswarya',host='localhost',database='blooddb')
        self.c=self.con.cursor()

    def create(self,name,bloodgroup,phone,city,last_donation):
        query='insert into donor(name,bloodgroup,phone,city,last_donation) values(%s,%s,%s,%s,%s)'
        data=(name,bloodgroup,phone,city,last_donation)
        self.c.execute(query,data)
        self.con.commit()
        print('data inserted successfully')

    def read(self):
        query='select * from donor'
        self.c.execute(query)
        record=self.c.fetchall()
        if record:
            # for row in record:
            #     print(row)
            return record
        else:
            #print('no records found')
            return None

    def retrieve(self,id):
        query='select * from donor where id=%s'
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            return record
        else:
            return None

    def update(self,name,bloodgroup,phone,city,last_donation,id):
        query='update donor set name=%s,bloodgroup=%s,phone=%s,city=%s,last_donation=%s where id=%s'
        data=(name,bloodgroup,phone,city,last_donation,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False

    def delete(self,id):
        query='delete from donor where id=%s'
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False


b=BloodDonation()
#b.create('Raghu','A+',9867453422,'ekm','2026-09-23')
#b.create('Anu', 'B+', 9876543210, 'Kochi', '2026-08-15')
b.read()
b.retrieve(5)
b.update('ashi','O+ve','8907654321','tvm','2025-07-19',2)
b.delete(2)