
#E-CHALLAN AND VEHICLE RECORD SYSTEM
#USERNAME OF POLICE IS ANUJPATEL  #USERNAME OF USER IS ALSO ANUJPATEL
#PASSWORD OF POLICE IS 123456          #PASSWORD OF USER IS ALSO 123456
import mysql.connector as sqltor,csv,time
mycon=sqltor.connect(host="localhost",user="root",passwd="30092002",database="ENTERTHENAMEOFDATABASE")
def TOLL():
    x=input("ENTER DAY:")
    a="E:\\"
    c=x
    d=".csv"
    b="w"
    f=open(a+c+d,b,newline="")
    w= csv.writer(f)
    head=["VEHICLE TYPE","MANUFACTURER","MODEL","RC","REGESTRATION NUMBER","CHALLAN AMOUNT","DATE-TIME","PLACE","REASON"]
    w.writerow(head)
    while True:  
        VEHICLE=input("  VEHICLE TYPE       *(eg. car,bike,truck,bus)*           :")
        MANUFACTURER=input("   MANUFACTURER       *(eg. maruti,honda,tata,hyundai)*       :")
        MODEL=input("    MODEL    :")
        RC=input("       REGESTRATION CERTIFICATE **(COMMERCIAL/PRIVATE)**          :")
        while True:
            
            REGESTRATION=input("REGESTRATION NUMBER    *(UP70XX0000)*        :")
            if len(REGESTRATION)<10:
                print("ENETR VALID NUMBER")
            elif len(REGESTRATION)>10:
                print("ENETR VALID NUMBER")
            else:
                break
        while True:    
            try:
                TOLL=float(input("   CHALLAN AMOUNT    *(in rupees)*     :"))
                if type (TOLL)==float:
                    break
            except ValueError:
                print("!!!Wrong Entry, Enter Again!!!")
        t=time.asctime(time.localtime(time.time()))
        DATETIME=t
        ROUTE=input("   PLACE     :")
        REASON=input("   REASON FOR CHALLAN      :")
        insert=[VEHICLE,MANUFACTURER,MODEL,RC,REGESTRATION,TOLL,DATETIME,ROUTE,REASON]
        w.writerow(insert)
        tup=(VEHICLE,MANUFACTURER,MODEL,RC,REGESTRATION,TOLL,DATETIME,ROUTE,REASON)
        if mycon.is_connected():
            print("--------------------------CHALLAN DONE------------------------------")
        cursor=mycon.cursor()
        st="INSERT INTO CHALLAN(VEHICLE_TYPE,MANUFACTURER,MODEL,RC,REGESTRATION_NUMBER,CHALLAN_AMOUNT,DAY_DATE_TIME,PLACE,REASON) VALUES ('{}','{}','{}','{}','{}',{},'{}','{}','{}')".format(VEHICLE,MANUFACTURER,MODEL,RC,REGESTRATION,TOLL,DATETIME,ROUTE,REASON)
        cursor.execute(st)
        mycon.commit()
        print("DO YOU WANT TO CLOSE YES/NO")
        while True:
            s=input("MAKE CHOICE:")
            
            if s.lower()=='yes':
                break
            elif s.lower()=='no':
                break
            else:
                print("Invalid Entery, Make Correct Choice.")
        if s.lower()=='yes':
            print('''WELCOME TO  E-CHALLAN AND VEHICLE RECORD SYSTEM''')
            print('''***PRESS (1) FOR POLICE LOGIN***
***PRESS (2) FOR USER LOGIN***
***PRESS (3) TO CLOSE APPLICATION***''')
            while True:    
                        try:
                            ch=int(input("MAKE CHOICE:"))
                            if ch==1:
                                login()
                                break
                            elif  ch==2:
                                loginuser()
                                break
                            elif ch>3:
                                print("INVALID ENTRY!!!!!!!TRY AGAIN")
                            elif ch==3:
                                print('''*******************THANKS FOR USING OUR APPLICATION***********************''')
                                break
                                
                            else:
                                print("!!!Wrong Choice, Enter Again!!!")
                        except ValueError:
                            print("!!!Wrong Choice, Enter Again!!!")
            break
        elif s.lower()=='no':
            print('''**************************************************
*********************NEW CHALLAN**************************''')
            pass
        
    f.close()
def check():
    print("PLEASE ENTER THE REGESTRATION NUMBER (eg. UP70XX0000) OF VEHICLE TO CHECK STATUS")
    while True:
        r=input("ENTER HERE:")
        a="E:\\"
        c=r.upper()
        d=".csv"
        b="w"
        f=open(a+c+d,b,newline="")
        w= csv.writer(f)
        head=["VEHICLE TYPE","MANUFACTURER","MODEL","RC","REGESTRATION NUMBER","CHALLAN AMOUNT","DATE-TIME","PLACE","REASON"]
        w.writerow(head)
        t=r.upper()
        if len(t)<10:
            print("ENETR VALID NUMBER")
        elif len(t)>10:
            print("ENETR VALID NUMBER")
        else:
            break
    cursor=mycon.cursor()
    st="SELECT * FROM CHALLAN WHERE REGESTRATION_NUMBER= '{}' ".format(t)
    cursor.execute(st)
    data=cursor.fetchall()
    print('''
***************************************************************************************************
                                                                 REPORT
***************************************************************************************************''')
    for row in data:
        print(row)
    for i in data:
        k=list(i)
        w.writerow(k)
    print('''
***************************************************************************************************
***************************************************************************************************''')
    print("A FILE CONTAINING THE ABOVE INFORMATION IS SAVED IN",a,"DRIVE ,HAVING NAME AS",r.upper())

    f.close()
    print('''WELCOME TO  E-CHALLAN AND VEHICLE RECORD SYSTEM''')
    print('''***PRESS (1) FOR POLICE LOGIN***
***PRESS (2) FOR USER LOGIN***
***PRESS (3) TO CLOSE APPLICATION***''')
    while True:    
                try:
                    ch=int(input("MAKE CHOICE:"))
                    if ch==1:
                        login()
                        break
                    elif  ch==2:
                        loginuser()
                        break
                    elif ch>3:
                        print("INVALID ENTRY!!!!!!!TRY AGAIN")
                    elif ch==3:
                        print('''*******************THANKS FOR USING OUR APPLICATION***********************''')
                        break
                        
                    else:
                        print("!!!Wrong Choice, Enter Again!!!")
                except ValueError:
                    print("!!!Wrong Choice, Enter Again!!!")
    
def login():
    x = "ANH"
    y = "123"
    loop=1
    while loop==1:
        username =input("Please enter your username: ")
        if username==x:
            password =input("Please enter your password: ")
            if password == y:
                print ("Logged in successfully as " ,username)
                print("****************************************************************")
                print('''***********WELCOME TO E-CHALLAN  SYSTEM*************''')
                TOLL()
                loop=2
            else:
                print ("Password incorrect!")
        else:
            print ("Username incorrect!")
def loginuser():
    x = "ANH"
    y = "123"
    loop=1
    while loop==1:
        username =input("Please enter your username: ")
        if username==x:
            password =input("Please enter your password: ")
            if password == y:
                print ("Logged in successfully as " ,username)
                print("****************************************************************")
                print('''***********WELCOME TO E-CHALLAN  SYSTEM*************''')
                check()
                loop=2
            else:
                print ("Password incorrect!")
        else:
            print ("Username incorrect!")

print('''WELCOME TO E-CHALLAN AND VEHICLE RECORD SYSTEM ''')
print('''***PRESS (1) FOR POLICE LOGIN***
***PRESS (2) FOR USER LOGIN***
***PRESS (3) TO CLOSE APPLICATION***''')
while True:    
            try:
                ch=int(input("MAKE CHOICE:"))
                if ch==1:
                    login()
                    break
                elif  ch==2:
                    loginuser()
                    break
                elif ch>3:
                    print("INVALID ENTRY!!!!!!!TRY AGAIN")
                elif ch==3:
                    print('''*******************THANKS FOR USING OUR APPLICATION***********************''')
                    break
                    
                else:
                    print("!!!Wrong Choice, Enter Again!!!")
            except ValueError:
                print("!!!Wrong Choice, Enter Again!!!")

