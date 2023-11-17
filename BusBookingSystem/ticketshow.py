#Data Importing section
from passengerinfo import*
import pymysql
import database as d

class TicketShow:

    def ticketShow(self):
        self.host = d.host
        self.user = d.user
        self.passwords = d.password
        self.database = d.database
        connection = pymysql.connect(host=self.host, user=self.user, password=self.passwords, database=self.database)
        curs = connection.cursor()
        print()
        self.id=int(input("                                                                       Enter your Booking ID:"))
        curs.execute("select * from passengers where id=%s",(self.id))
        row=curs.fetchone()
        print()
        print("                                                                       ------------------------------------------------------------------------------")
        print("                                                                                                 Bus Travel Receipt                               ")
        print("                                                                       ------------------------------------------------------------------------------")
        print()
        print("                                                                                            Bus Booking Application  System")
        print()
        print("                                                                       Phone No\Mob No             : 8000800088,8888880000   ")
        print()
        print("                                                                       ",row[3],"------------->",row[4],"            ","        Passenger Id:",row[0])
        print()
        print("                                                                       ","Passenger Name :", row[1],"              ","Number of Passenger :",row[2])
        print("                                                                       ","________________________________________________________________")
        print()
        print("                                                                        Date of Journey :",row[5],"              ","Seat No :",row[6],"              ")
        print()
        print("                                                                        Bus Type :       ",row[7],"                    " ," Bus Fare :",row[8],"            "  )                                            
        print()
        print("                                                                       ------------------------------------------------------------------------------")
                
