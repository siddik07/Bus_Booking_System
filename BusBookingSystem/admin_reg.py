import pymysql
import database as d
class Admin:
    def __init__(self):
        self.username = None
        self.password = None

        self.host = d.host
        self.user = d.user
        self.passwords = d.password
        self.database = d.database

    def adminRegistration(self):
        print("                                                                       ----------------------------------------------------------------")
        print()
        self.username = input("                                                                       Enter and set username      :")
        self.password = input("                                                                       Enter and set your password :")
        #saving a data into database
        connection = pymysql.connect(host=self.host, user=self.user, password=self.passwords, database=self.database)
        curs = connection.cursor()
        curs.execute("insert into admins (name,passwords) values(%s,%s)", (self.username,self.password))
        connection.commit()
        connection.close()
        print("                                                                       Registration successfully")
        print()
        print("                                                                       ----------------------------------------------------------------")
            
    def adminLogin(self):
        while(True):
            print("                                                                       ----------------------------------------------------------------")
            print()
            self.username = input("                                                                       Enter  username  :")
            self.password = input("                                                                       Enter  password  :")
            connection = pymysql.connect(host=self.host, user=self.user, password=self.passwords,database=self.database)
            curs = connection.cursor()
            curs.execute("select * from admins where name=%s and passwords=%s",( self.username,self.password))
            login=curs.fetchone()
            if  login:
                print()
                print("                                                                       Login successfully")
                break
            else:
                print("                                                                       InValid!!!....Enter correct username and password")
            print()
            print("                                                                       ---------------------------------------------------------------")
