
Ram-Mandir
school project
February 12, 2021
Banega to Ram Mandir hi !!!!
import os,time,math,mysql.connector as myconn ,random,datetime
from getpass import getpass
q=myconn.connect(user="root", passwd="", host="localhost")
cur=q.cursor()
login=False
def login():
    global nm , login, user_name
    print("Welcome to the regestration portal of Temples ")
    print("please provide us with your User name and password")
    user_name=input("Please enter your User Name \n--> ")
    user_password=getpass.getpass(prompt="Please enter your corresponding Password \n --> ")
    qry="SELECT `name` FROM `user` WHERE `id`= {} AND `password`='{}'".format(user_name,user_password)
    # changes are left to be done
    try:
        cur.execute(qry)
        r=cur.fetchone()
        login = False
        if r == None :
            print("Invalid User-ID OR Password ")
            time.sleep(1)
            print("Please Try Again to login")
        else:
            nm=r[0]
            login = True
            time.sleep(3)
            print('Login Successful')
    except:
        login==False
        print("Please Enter Valid User-ID & Password ")

    while login == True :
        appoint()

# CHANGE IN MAXIMUM CAPACITY OF MEMBERS BY TEMPLE
def temple_login():
    print("\n\t**TEMPLE LOGIN**")
    print("Please enter the registered details")
    usr=int(input("Enter Your registered Trust Identification Number -->"))
    pas=getpass.getpass(prompt="Please Entered your Registered Password-->")
    qry="SELECT `name`,contact,address,Capacity FROM `temple` WHERE `Trust Identification Number`={} AND `password` ={}".format(usr,pas)
    cur.execute(qry)
    r=cur.fetchone()
    temple_name=r[0]

    if r == None:
        print("Sorry Record not found")
        time.sleep(1)
        print("Please check your T-I-N and Password \n and Try Again ")
    else:
        print("Login Successful")
        temple()
def temple():
    while True:
        print("\n"*100,"\t\tTemple Management ")
        print('\n\t\t HOME PAGE')
        time.sleep(1)
        print("\n \n 1 -> Summary For last 10 Days")
        time.sleep(1)
        print("\n \n 2-> Change in Address ")
        time.sleep(1)
        print("\n \n 3-> Change in Maximum Capacity Of Visiting Peoples")
        time.sleep(1)
        print("\n \n 4-> Change in Temple Name")
        time.sleep(1)
        print("\n \n 5-> View Visitors details as per specified Date")
        time.sleep(1)
        print("\n  6-> Home Page")
        inp=int(input("Enter the choice \n\t--> "))
        if inp==1:
            av_visit()
        elif inp==2:
            temple_change_address()           
        elif inp==3:
            temple_change_capacity()
        elif inp==4:
            temple_reg()
        elif inp==5:
            forgot()
        elif inp==6:
            break
        else:
            print("SORRY !! WRONG INPUT ENTERED")
       
def av_visit():
        print("****LAST 10 DAYS SUMMERY**** ")
        time.sleep(1)
        e=datetime.date.today()-datetime.timedelta(days=11)
        dt=e.strftime('%Y%m%d')
        qry="SELECT `user_id`,`f_members` FROM `{}` WHERE  date > {}".format(temple_name,dt)
        cur.execute(qry)
        visit_count=cur.fetchall()
        visitors=0
        for i in visit_count:
            visitors+=i[1]
        no_of_reg=cur.rowcount
        print("\n\tAverage Regestration Of last 10 Days--> ",no_of_reg/10)
       
        time.sleep(2)
        print("\n\tNumber of people visited  ",temple_name," are -->",visitors)
        ## WANT TO PRINT SUMMERY FOR MORE LAST 10 DAYS (20 DAY OLDER TO 10 DAY OLDER)

def temple_change_address():
    print("\n"*10)
    time.sleep(2)
    print("UPDATION FOR TEMPLE ADDRESS")
    time.sleep(2)
    print("Please Enter Validated address")
    address=input(" -->")
    qry="UPDATE `User` SET `password`='{}'".format(address,)
    cur.execute(qry)
    q.commit()
    print("New Address is ")
    time.sleep(1)
    print(address)
    time.sleep(1)
    print("Address updated ")
    time.sleep(1)
   
def temple_change_capacity():
    print("Update capacity of people ")
    qry="SELECT `Capacity` FROM `temple` WHERE `name` = '{}'".format(temple_name,)
    cur.execute(qry)
    old_capacity=cur.fetchone()[0]
    time.sleep(2)
    print("\n\n\tCapacity for Temple\n\t\t-->",temple_name,"\n\tis currently set at \n\t\t-->",old_capacity)
    new_capacity=int(input("\n\tEnter New capacity (Number of People ) for the Temple \n\t\t-->"))
    qry="UPDATE `temple` WHERE `name` = '{}' AND `Capacity` = {}".format(temple_name,old_capacity)
    cur.execute(qry)
    q.commit()
    time.sleep(1)
    print("Temple CApacity updated  ")
    time.sleep(1)
    print("From ",old_capacity,"To ",new_capacity)
    time.sleep(2)
   
   
def appoint():
    print("\n\n please enter your choice \n",nm)
    time.sleep(1)
    print('\t1 -> Temple visit Registration')
    time.sleep(1)
    print('\t2 -> Change Registration')
    print("Can only change no of members OR Time")
    time.sleep(1)
    print('\t3 -> Cancel Registraition')
    time.sleep(1)
    print('\t4 -> Get Current Registraton Details')
    time.sleep(1)
    print('\t5 -> Change Password')
    time.sleep(1)
    print('\t6 -> Logout')
    choice=int(input("Please Enter your Choice \n\t --> "))
    if choice == 1 :
        temple_appoint()
    elif choice == 2 :
        tmpl_change()
    elif choice == 3:
        tmpl_cancel()
    elif choice == 4:
        tmpl_current()
    elif choice == 5 :
        change_password()
    elif choice == 6:
        out_app()
    else:
        print("Sorry Invalid Input Please Enter it Again ")
       
def temple_appoint():
    qry='SELECT `name` FROM `temple`'
    cur.execute(qry)
    r=cur.fetchall()
    t_name=[]
    for i in range(0,len(r)):
        t_name.append(r[i][0])
    print("Registration of Following tepmles is availabe -->")
    for i in range(0,len(t_name)):
        print(i+1,"-->",t_name[i])
    inp=int(input("Please enter the Corresponding number of the Temple\n\t-->"))
    f=int(input("Please Enter the number of members \n going to visit the temple with you *INCLUDING YOU* \n-->"))
    print("Time For Visiting is as follows ->\n 1 --> 9:00 AM to 12:00 PM \n 2 --> 12:15 PM to 3:00 PM \n 3 --> 3:15 PM to 6:00 PM \n 4 --> 6:15 PM to 9:00 PM")
    ti=int(input("Please enter time slot choice"))
    dt=int(input("Please enter Date of Visit of registration in format of [yyyymmdd]"))
    qry="SELECT SUM(`f_members`) FROM `{}` WHERE `time_slot`={} AND date ={}".format(t_name[inp-1],ti,dt)
    cur.execute(qry)
    cur.fetchall()
    already_reg=cur.rowcount
    qry="SELECT `capacity` FROM `tepmle` WHERE `name`={}".format(t_name[inp-1],)
    cur.execute(qry)
    cur.fetchall()
    maxm=cur.rowcount
    R=(maxm - already_reg)
    if R == 0:
        print("Sorry Registration is done at its maximum capacity ")
        time.sleep(2)
        print("No more regestration can occur at the selected Date and Time slot\n TRY WITH DIFFERENT DATE AND TIME SLOT OR PLEASE TRY AGAIN LATER ")
    elif R < f and r != 0 :
        print("Regestration of ",f," persons not possible \n *ONLY",R,"REGESTRATIONS LEFT*")
    else:
        print("Would you like to register under VIP category")
        vip=input("Please enter (y/n)\nY -> YES \nN -> NO ").lower()
        qry="INSERT INTO {}(`user_id`,`time_slot`,`f_members`,`date`,`vip`) VALUES ({},{},{},{},'{}')".format(t_name[inp-1],user_name,ti,f,dt,vip)
        cur.execute(qry)
        q.commit()
        print("Regestration  successful\n\t*Thank you for regestering with us*")
       
def tmpl_change():
    print("\n"*100)
    print("CHANGE IN  REGESTRATION")
    print("CHANGE DATE & TIME CAN BE MADE")
    qry='SELECT `name` FROM `temple`'
    cur.execute(qry)
    r=cur.fetchall()
    t_name=[]
    for i in range(0,len(r)):
        t_name.append(r[i][0])
    print("Please select the temple whose regestration you want to update -->")
    for i in range(0,len(t_name)):
        print(i+1,"-->",t_name[i])
    inp=int(input("Please enter the Corresponding number of the Temple\n\t--> "))
    time.sleep(2)
    qry="SELECT `time_slot`,f_members,date FROM {} WHERE `user_id`={} ".format(t_name[inp-1],user_name)
    cur.execute(qry)
    det=cur.fetchall()[-1]
    print("Do you want to Alter your Date")
    inp=input("Please enter your choice (Y/N) \n\t--> ").lower()
    if inpk=="y":
        dt=int(input("Please enter the new date \n in format of[yyyymmdd]\n-->"))
    else:
        dt=(str(det[2].year)+str(det[2].month)+str(det[2].day))
    print("Do you want to Alter your Time ")
    inpk=input("Please enter your choice (Y/N) \n\t--> ").lower()
    if inpk =="y":
        print("Time For Visiting is as follows ->\n 1 --> 9:00 AM to 12:00 PM \n 2 --> 12:15 PM to 3:00 PM \n 3 --> 3:15 PM to 6:00 PM \n 4 --> 6:15 PM to 9:00 PM")
        tm=int(input("Please Enter your new Time Choice\n(1 / 2 / 3 / 4) --> "))
        if tm<det[0]:
            date_error=True
    else:
        tm=det[0]
    if date_error== False:
        qry="SELECT MAX(reg_no) FROM `{}` WHERE `user_id`={}".format(t_name[inp-1],user_name)
        cur.execute(qry)
        r=cur.fetchone()[0]
        qry="UPDATE `{}` SET `time_slot`={}, `date`={} WHERE `reg_no`={}".format(t_name[inp-1],tm,dt.r)
        cur.execute(qry)'
        q.commit()
        time.sleep(1)
        print("Regestration  Change Successful ")
          
def  tmpl_cancel():
    print("Cancelation of Temple regestration")
    qry='SELECT `name` FROM `temple`'
    cur.execute(qry)
    r=cur.fetchall()
    t_name=[]
    for i in range(0,len(r)):
        t_name.append(r[i][0])
    print("Please select the Temple name --> ")
    for i in range(0,len(t_name)):
        print(i+1,"-->",t_name[i])
    inp=int(input("Please enter the Corresponding number of the Temple \n\t--> "))
    print("\n\tFinding Record")
    time.sleep(3)
    qry="delete from`{}` where `user_id`={} ".format(t_name[inp-1],user_name)
    cur.execute(qry)
    print("\n\tValidating Delete")
    time.sleep(3)
    qry="SELECT MAX(`reg_no`) FROM {} WHERE `user_id`={} ".format(t_name[inp-1],user_name)
    cur.execute(qry)
    r=cur.fetchone()[-1]
    qry="DELETE FROM `{}` WHERE `reg_no`={} AND `user_id`={} ".format(t_name[inp-1],r,user_id)
    cur.execute(qry)
    qry="SELECT `user_id` FROM  `{}` WHERE `reg_no`={} AND `user_id`={} ".format(t_name[inp-1],r,user_id)
    cur.execute(qry)
    ret=cur.fetchall()[0]
    if ret == None:
        print("Regestration Cancelled Successfully")
    else:
        print("Sorry !  error occured \n**PLEASE TRY AGAIN LATER**")
   

def tmpl_current():
    qry='SELECT `name` FROM `temple`'
    cur.execute(qry)
    r=cur.fetchall()
    t_name=[]
    for i in range(0,len(r)):
        t_name.append(r[i][0])
    print("Please select the Temple name --> ")
    for i in range(0,len(t_name)):
        print(i+1,"-->",t_name[i])
    inp=int(input("Please enter the Corresponding number of the Temple \n\t--> "))
    qry="SELECT `time_slot`,`f_members`,`date`,`VIP` FROM {} WHERE `user_id`={} ".format(t_name[inp-1],user)
    cur.execute(qry)
    r=cur.fetchall()[-1]
    print("Your last regestration details is as follows --> ")
    if r[0] == 1:
        print("Time Slot --> 1 9:00 AM -- 12:00 PM")
    elif r[0] == 2:
        print("Time Slot --> 1 12:15 AM -- 3:00 PM")
    elif r[0] == 3:
        print("Time Slot --> 1 3:15 AM -- 6:00 PM")
    elif r[0] == 4:
        print("Time Slot --> 1 6:15 AM -- 9:00 PM")
    print("Number of family members regestration ",r[1])
    print("date is",r[2])
    if r[3]== 'y':
        print("The regestration is done in VIP Quota")
    else:
        print("The regestration is done in General quota")


def change_password():
    print("Password Change module")
    pasd=getpass.getpass(prompt="Please enter your NEW password")
    qry="UPDATE `USER` SET `password`='{}' WHERE ID={}".format(pasd,user_name)
    
def signin():
    print("\n"*100)
    u_name=input("Please enter the your Name \nwithout Surmname\nWith Designation (Mr,Miss) \n\t-->  ")
    u_ln=input("Enter your last name")
    c_no=int(input("Please enter your Contact Number"))
    add=input("Please enter your Address")
    id_no=input("Please enter your valid ID-Proof number")
    dob=int(input("Please enter your Date of Birth in format of [yyyymmdd]"))
    password=getpass.getpass(prompt="Please set your Password --> ")
    if 'mr' in u_name.lower():
        gender="M"
    elif 'miss' in u_name.lower():
        gender="F"
    else:
        print("User not specified Mr/Miss please specify your gender \n m->Male , f->Female")
        gender=input("-->").lower()
    qry="INSERT INTO `user` (`name`,`password`,`l_name`,`Gender`,`contact`,`address`,`id_number`,`DOB`) VALUES ('{}','{}','{}','{}',{},'{}','{}',{}).format(u_name,password,u_ln,gender,c_no,add,id_no,dob)"
    cur.execute(qry)
    q.commit()
    print("Successfully User Added")
    time.sleep(5)
   
def temple_reg():
    t_name=input("Please enter the your Name of the Trust \n\t->  ")
    c_no=int(input("Please enter Trust's Contact Number\n\t"))
    add=input("Please Address of Temple")
    cap=int(input("Please enter the Capacity of temple \n i.e. Maximum number of people in temple in 3 hour time-slot\n -->"))
    id_no=input("Enter your Trust Identification Number \n\t-->")
    password=getpass.getpass(prompt="Please set your Password --> ")
    qry=("INSERT INTO `temple` (`name`,`contact`,`address`,`TIN`,`password`,`capacity`) VALUES ('{}',{},'{}',{},'{}',{})".format(t_name,c_no,add,id_no,password,cap))
    cur.execute(qry)
    q.commit()
    qry="CREATE TABLE {}(S_No int(10) auto_increment PRIMARY KEY,name varchar(100),user_id int(8),f_members int(3),date date,v_time varchar(50))"
    cur.execute(qry)
    q.commit()
    print("Temple Registration Successful")
    time.sleep(5)
def forgot():
    #
    #    *************
    #           Temple ka password reset yaha dalna hai.
    #
    print("\n"*100,'\t\tPASSWORD RESET ')
    user_id=int(input("Please enter your User id \n\t--> "))
    id_no=input("Please enter your ID-Number regestered woth us\n\t-> ")
    try:
        qry=("SELECT `password` FROM `user` WHERE id={} AND id_number='{}' ".format(user_id,id_no))
        cur.execute(qry)
        r=cur.fetchone()
        if r == None:
            time.sleep(2)
            print("Sorry User-ID & Unique ID Record not found")
            time.sleep(5)
        else:
            time.sleep(2)
            print("\nUser Id & Unique Id Record found \n")
            password=getpass.getpass(prompt="Enter New Password\n\t-->")
            qry="UPDATE `user` SET `password`='{}' WHERE id={}".format(password,id_no)
            cur.execute(qry)
            q.commit()
            print(" Password Changed Successfully ")
           
def home():
    while True:
        print("\n"*100,"\t\tTemple Registration Portal")
        print('\n\t\t HOME PAGE')
        time.sleep(1)
        print("\n \n 1-> Login  ")
        time.sleep(1)
        print("\n \n 2-> Login for emple authorities ")
        time.sleep(1)
        print("\n  3-> New User Sign in  ")
        time.sleep(1)
        print("\n  4-> Temple Registration  for Online Management")
        time.sleep(1)
        print("\n  5-> Forgot Password  ")
        time.sleep(1)
        print("\n  6-> Exit  ")
        inp=int(input("Enter the choice \n\t--> "))
        if inp==1:
            login()
        elif inp==2:
            temple_login()           
        elif inp==3:
            signin()
        elif inp==4:
            temple_reg()
        elif inp==5:
            forgot()
        elif inp==6:
            break
        else:
            print("SORRY !! WRONG INPUT ENTERED")
