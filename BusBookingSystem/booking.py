import pymysql
import database as d
import random as r

class TicketBooking():
    #constructor
    def __init__(self):
        self.id=r.randint(1001,9999)
        

        self.host = d.host
        self.user = d.user
        self.passwords = d.password
        self.database = d.database
        
    def getPassengerInfo(self):
        self.passengerName= input("                                                                       Enter Passenger Name          :")
        self.noOfPassenger= int(input("                                                                       Enter Number Of Passenger :"))
        print("1:Chennai")
        print("2: Trichy")
        print("3: Bangalore")
        print("4: Coimbatore")
        
    def location(self):
        # Enter departure Location Name START
        self.dl = int(input("                                                                       Enter Departure Location: "))
        if self.dl == 1:
            self.departureLocation = "Chennai"
        elif self.dl == 2:
            self.departureLocation = "Trichy"
        elif self.dl == 3:
            self.departureLocation = "Bangalore"
        elif self.dl == 4:
            self.departureLocation = "Coimbatore"
        else:
            print("                                                                       Please Enter correct choice  :")
        # departure Location Name END
        
        print("1: Madurai")
        print("2: Vellore")
        print("3: Tirunelveli")
        print("4: Tanjore")
        # Enter destination Location Name START
        self.dpl = int(input("                                                                       Enter Destination Location  :"))
        if self.dpl == 1:
            self.destinationLocation = "Madurai"
        elif self.dpl == 2:
            self.destinationLocation = "Vellore"
        elif self.dpl == 3:
            self.destinationLocation = "Tirunelveli"
        elif self.dpl == 4:
            self.destinationLocation = "Tanjore"
        # Enter destination Location Name END

    def date(self):
        self.date = input("                                                                       Enter Date of Joiurney Like 2023-08-27 :")  #Date of Journey

    def seatbook(self):
        #Booking Seat Start 
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList=[]
    
        for i in range(self.noOfPassenger):
                self.seatNo = int(input("                                                                       Choose a Seat Number From Above list:"))
                if self.seatNo <=30:
                    if  self.seatNo in seatNoList:
                        self.bookingList.append(self.seatNo)
                        seatNoList.remove(self.seatNo)
                        count = len(seatNoList)      
                    else:
                        print()
                        print("Ticket Allready Booked")
                else:
                    print()
                    print("                                                                       Don't Choose a Seat Number Which is Not Available")
        self.bookingList=str(self.bookingList)
        # Booking Seat END

    def bustype(self):
        print()
        print("                                                                        1. AC BUS     = 500 Fare")
        print()
        print("                                                                        2. NON AC BUS = 300 Fare")
        print()
        self.busType = int(input("                                                                       Select Bus Type  :"))
        
        if self.busType == 1:
            self.selectBusType = "AC BUS"
            self.busFare = self.noOfPassenger*500
        elif self.busType == 2:
            self.selectBusType = "NON AC BUS"
            self.busFare = self.noOfPassenger*300
           
        # Booking Seat END

    def final(self):
        self.getPassengerInfo()
        self.location()
        self.date()
        self.seatbook()
        self.bustype()
        
#saving Passenger Data into databases
        
class PassengerData(TicketBooking):
    def saveInfo(self):
        super().__init__()
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.passwords, database=self.database)
            curs = connection.cursor()
            curs.execute("insert into passengers values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.id,self.passengerName,self.noOfPassenger, self.departureLocation, self.destinationLocation, self.date, self.bookingList, self.selectBusType, self.busFare))
            connection.commit()
            connection.close()
            print()
            print("                                                                       Booking Successfull")
            print()
            print("                                                                       Your Booking ID is",self.id)     

        except:
            print()
            print("Data not saved!!!!")
        

