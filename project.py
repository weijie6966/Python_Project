import sqlite3
import tkinter
from tkinter import*
from prettytable import PrettyTable

connection=sqlite3.connect("project.db")
c=connection.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS employee(
    e_ID INTEGER,
    e_name TEXT,
    e_status TEXT
    )""")
c.execute("""CREATE TABLE IF NOT EXISTS car_info(
        c_ID INTEGER,
        car_name TEXT,
        start_time TEXT,
        end_time TEXT,
        duration TEXT,
        car_status TEXT
        )""")
c.execute("""CREATE TABLE IF NOT EXISTS work_schedule(
        work_ID INTEGER PRIMARY KEY,
        day TEXT,
        employee_ID integer NOT NULL,
        car_ID integer NOT NULL,
        clock_in TEXT,
        clock_out TEXT,
        FOREIGN KEY (employee_ID) REFERENCES employee (e_ID),
        FOREIGN KEY (car_Id) REFERENCES workshop_car (c_ID)
        )""")
def create_employee():
    c.execute("""CREATE TABLE IF NOT EXISTS employee(
    e_ID INTEGER,
    e_name TEXT,
    e_status TEXT
    )""")
    c.execute("INSERT INTO employee VALUES (1,'weijie','free')")
    c.execute("INSERT INTO employee VALUES (2,'hakim','free')")
    c.execute("INSERT INTO employee VALUES (3,'intan','free')")
    c.execute("INSERT INTO employee VALUES (4,'Ali','free')")
    c.execute("INSERT INTO employee VALUES (5,'Abu','free')")
    c.execute("INSERT INTO employee VALUES (6,'ong','free')")
    c.execute("INSERT INTO employee VALUES (7,'wong','free')")
    c.execute("INSERT INTO employee VALUES (8,'lau','free')")
    c.execute("INSERT INTO employee VALUES (9,'goh','free')")
    c.execute("INSERT INTO employee VALUES (10,'ngu','free')")
    connection.commit()

def create_car():
    c.execute("""CREATE TABLE IF NOT EXISTS car_info(
        c_ID INTEGER,
        car_name TEXT,
        start_time TEXT,
        end_time TEXT,
        duration TEXT,
        car_status TEXT
        )""")
    c.execute("INSERT INTO car_info VALUES (1,'car1','null','null','null','Waiting')")
    c.execute("INSERT INTO car_info VALUES (2,'car2','null','null','null','Waiting')")
    c.execute("INSERT INTO car_info VALUES (3,'car3','null','null','null','Waiting')")
    c.execute("INSERT INTO car_info VALUES (4,'car4','null','null','null','Waiting')")
    c.execute("INSERT INTO car_info VALUES (5,'car5','null','null','null','Waiting')")
    connection.commit()

def create_work():
    c.execute("""CREATE TABLE IF NOT EXISTS work_schedule(
        work_ID INTEGER PRIMARY KEY,
        day TEXT,
        employee_ID integer NOT NULL,
        car_ID integer NOT NULL,
        clock_in TEXT,
        clock_out TEXT,
        FOREIGN KEY (employee_ID) REFERENCES employee (e_ID),
        FOREIGN KEY (car_Id) REFERENCES workshop_car (c_ID)
        )""")
    connection.commit()
    
def new_week():
    c.execute("""DROP TABLE employee""")
    c.execute("""DROP TABLE car_info""")
    c.execute("""DROP TABLE work_schedule""")
    c.execute("""CREATE TABLE IF NOT EXISTS employee(
    e_ID INTEGER,
    e_name TEXT,
    e_status TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS employee(
        e_ID INTEGER,
        e_name TEXT,
        e_status TEXT
        )""")
    c.execute("""CREATE TABLE IF NOT EXISTS car_info(
            c_ID INTEGER,
            car_name TEXT,
            start_time TEXT,
            end_time TEXT,
            duration TEXT,
            car_status TEXT
            )""")
    c.execute("""CREATE TABLE IF NOT EXISTS work_schedule(
            work_ID INTEGER PRIMARY KEY,
            day TEXT,
            employee_ID integer NOT NULL,
            car_ID integer NOT NULL,
            clock_in TEXT,
            clock_out TEXT,
            FOREIGN KEY (employee_ID) REFERENCES employee (e_ID),
            FOREIGN KEY (car_Id) REFERENCES workshop_car (c_ID)
            )""")
    connection.commit()
    
def morning():
    value_e1_id.delete(0,"end")
    value_e2_id.delete(0,"end")
    value_c_id.delete(0,"end")
    #value_day.delete(0,"end")
    value_work1_id.config(state=NORMAL)
    value_work2_id.config(state=NORMAL)
    w1=0
    w2=0
    if(value_day.get()=="Monday"):  
        w1=11
        w2=12
    elif(value_day.get()=="Tuesday"):
        w1=21
        w2=22
    elif(value_day.get()=="Wednesday"):
        w1=31
        w2=32
    elif(value_day.get()=="Thursday"):
        w1=41
        w2=42
    elif(value_day.get()=="Friday"):
        w1=51
        w2=52
    elif(value_day.get()=="Saturday"):
        w1=61
        w2=62
    elif(value_day.get()=="Sunday"):
        w1=71
        w2=72
    value_work1_id.delete(0,"end")
    value_work1_id.insert(0,w1)
    value_work2_id.delete(0,"end")
    value_work2_id.insert(0,w2)
    value_work1_id.config(state=DISABLED)
    value_work2_id.config(state=DISABLED)
    value_e2_id.config(state=NORMAL)
    time_start="7.00 am"
    time_end="11.00 am"
    duration=4
    value_start_time.delete(0,"end")
    value_start_time.insert(0,time_start)
    value_end_time.delete(0,"end")
    value_end_time.insert(0,time_end)
    value_duration.delete(0,"end")
    value_duration.insert(0,duration)
    

def afternoom():
    value_e1_id.delete(0,"end")
    value_e2_id.delete(0,"end")
    value_c_id.delete(0,"end")
    
    value_work1_id.config(state=NORMAL)
    value_work2_id.config(state=NORMAL)
    value_e2_id.config(state=NORMAL)
    w1=0
    w2=0
    if(value_day.get()=="Monday"):
        w1=13
        w2=14
    elif(value_day.get()=="Tuesday"):
        w1=23
        w2=24
    elif(value_day.get()=="Wednesday"):
        w1=33
        w2=34
    elif(value_day.get()=="Thursday"):
        w1=43
        w2=44
    elif(value_day.get()=="Friday"):
        w1=53
        w2=54
    elif(value_day.get()=="Saturday"):
        w1=63
        w2=64
    elif(value_day.get()=="Sunday"):
        w1=73
        w2=74
    value_work1_id.delete(0,"end")
    value_work1_id.insert(0,w1)
    value_work2_id.delete(0,"end")
    value_work2_id.insert(0,w2)
    value_work1_id.config(state=DISABLED)
    value_work2_id.config(state=DISABLED)
    

    time_start="12.00 pm"
    time_end="5.00 pm"
    duration=5
    value_start_time.delete(0,"end")
    value_start_time.insert(0,time_start)
    value_end_time.delete(0,"end")
    value_end_time.insert(0,time_end)
    value_duration.delete(0,"end")
    value_duration.insert(0,duration)
def night():
    value_e1_id.delete(0,"end")
    value_e2_id.delete(0,"end")
    value_c_id.delete(0,"end")
    
    value_work1_id.config(state=NORMAL)
    value_work2_id.config(state=NORMAL)
    w1=0
    if(value_day.get()=="Monday"):
        w1=15
    elif(value_day.get()=="Tuesday"):
        w1=25
    elif(value_day.get()=="Wednesday"):
        w1=35
    elif(value_day.get()=="Thursday"):
        w1=45
    elif(value_day.get()=="Friday"):
        w1=55
    elif(value_day.get()=="Saturday"):
        w1=65  
    elif(value_day.get()=="Sunday"):
        w1=75
        
    value_work1_id.delete(0,"end")
    value_work1_id.insert(0,w1)
    value_work2_id.delete(0,"end")
 
    value_work1_id.config(state=DISABLED)
    value_work2_id.config(state=DISABLED)
    value_e2_id.config(state=DISABLED)
    time_start="6.00 pm"
    time_end="10.00 pm"
    duration=4
    value_start_time.delete(0,"end")
    value_start_time.insert(0,time_start)
    value_end_time.delete(0,"end")
    value_end_time.insert(0,time_end)
    value_duration.delete(0,"end")
    value_duration.insert(0,duration)
def start_work():
    work1_ID=int(value_work1_id.get())
    
    day=value_day.get()
    employee_1_ID=int(value_e1_id.get())
    
    car_ID=int(value_c_id.get())
    clock_in=value_start_time.get()
    e_status="working"
    car_status="Under repair"

    if(value_work2_id.get()!="" and value_e2_id.get()!=""):
        work2_ID=int(value_work2_id.get())
        employee_2_ID=int(value_e2_id.get())
        c.execute("INSERT INTO  work_schedule (work_ID,day,employee_ID,car_ID,clock_in) VALUES(?,?,?,?,?)",(work1_ID,day,employee_1_ID,car_ID,clock_in))
        c.execute("INSERT INTO  work_schedule (work_ID,day,employee_ID,car_ID,clock_in) VALUES(?,?,?,?,?)",(work2_ID,day,employee_2_ID,car_ID,clock_in))
        c.execute("UPDATE employee SET e_status='"+e_status+"' WHERE e_ID='"+str(employee_1_ID)+"'")
        c.execute("UPDATE employee SET e_status='"+e_status+"' WHERE e_ID='"+str(employee_2_ID)+"'")
        c.execute("UPDATE car_info SET car_status='"+car_status+"' WHERE c_ID='"+str(car_ID)+"'")
        c.execute("UPDATE car_info SET start_time='"+clock_in+"' WHERE c_ID='"+str(car_ID)+"'")
        connection.commit()
    else:
        c.execute("INSERT INTO  work_schedule (work_ID,day,employee_ID,car_ID,clock_in) VALUES(?,?,?,?,?)",(work1_ID,day,employee_1_ID,car_ID,clock_in))
        c.execute("UPDATE employee SET e_status='"+e_status+"' WHERE e_ID='"+str(employee_1_ID)+"'")
        c.execute("UPDATE car_info SET car_status='"+car_status+"' WHERE c_ID='"+str(car_ID)+"'")
        c.execute("UPDATE car_info SET start_time='"+clock_in+"' WHERE c_ID='"+str(car_ID)+"'")
        connection.commit()
def end_work():
    employee_1_ID=int(value_e1_id.get())
    duration=value_duration.get()
    car_ID=int(value_c_id.get())
    clock_out=value_end_time.get()
    e_status="free"
    car_status="Complete"
    if(value_e2_id.get()!=""):
        employee_2_ID=int(value_e2_id.get())
        c.execute("UPDATE employee SET e_status='"+e_status+"' WHERE e_ID='"+str(employee_1_ID)+"'")
        c.execute("UPDATE employee SET e_status='"+e_status+"' WHERE e_ID='"+str(employee_2_ID)+"'")
        c.execute("UPDATE car_info SET car_status='"+car_status+"' WHERE c_ID='"+str(car_ID)+"'")
        c.execute("UPDATE car_info SET end_time='"+clock_out+"' WHERE c_ID='"+str(car_ID)+"'")
        c.execute("UPDATE car_info SET duration='"+duration+"' WHERE c_ID='"+str(car_ID)+"'")
        c.execute("UPDATE work_schedule SET clock_out='"+clock_out+"' WHERE car_ID='"+str(car_ID)+"'")
        connection.commit()
    else:
         c.execute("UPDATE employee SET e_status='"+e_status+"' WHERE e_ID='"+str(employee_1_ID)+"'")
         c.execute("UPDATE car_info SET car_status='"+car_status+"' WHERE c_ID='"+str(car_ID)+"'")
         c.execute("UPDATE car_info SET end_time='"+clock_out+"' WHERE c_ID='"+str(car_ID)+"'")
         c.execute("UPDATE car_info SET duration='"+duration+"' WHERE c_ID='"+str(car_ID)+"'")
         c.execute("UPDATE work_schedule SET clock_out='"+clock_out+"' WHERE car_ID='"+str(car_ID)+"'")
         connection.commit()

def monday():
    value_day.config(state=NORMAL)
    value_day.delete(0,"end")
    value_day.insert(0,"Monday")
    value_day.config(state=DISABLED)
def tuesday():
    value_day.config(state=NORMAL)
    value_day.delete(0,"end")
    value_day.insert(0,"Tuesday")
    value_day.config(state=DISABLED)
def wednesday():
    value_day.config(state=NORMAL)
    value_day.delete(0,"end")
    value_day.insert(0,"Wednesday")
    value_day.config(state=DISABLED)
def thursday():
    value_day.config(state=NORMAL)
    value_day.delete(0,"end")
    value_day.insert(0,"Thursday")
    value_day.config(state=DISABLED)
def friday():
    value_day.config(state=NORMAL)
    value_day.delete(0,"end")
    value_day.insert(0,"Friday")
    value_day.config(state=DISABLED)
def saturday():
    value_day.config(state=NORMAL)
    value_day.delete(0,"end")
    value_day.insert(0,"Saturday")
    value_day.config(state=DISABLED)
def sunday():
    value_day.config(state=NORMAL)
    value_day.delete(0,"end")
    value_day.insert(0,"Sunday")
    value_day.config(state=DISABLED)

def check_work():
    date=value_day.get()
    c.execute("SELECT day,employee_ID FROM work_schedule WHERE day='"+date+"'")
    record=c.fetchall()
    print(record)
    table_who_work=PrettyTable()
    table_who_work.field_names=["day","employee ID","name"]
    for data in record:
        c.execute("SELECT e_name FROM employee WHERE e_ID='"+str(data[1])+"'")
        table_e=c.fetchall()
        for name in table_e:
            table_who_work.add_row([data[0],data[1],name[0]])#add data
    print(table_who_work)
    lbl_show_tabel_work.config(text=table_who_work)

def check_work_car():
    car=value_c_id.get()
    c.execute("SELECT car_ID,employee_ID FROM work_schedule WHERE car_ID='"+car+"'")
    record=c.fetchall()
    print(record)
    table_who_work=PrettyTable()
    table_who_work.field_names=["car_id","employee ID","name"]
    for data in record:
        c.execute("SELECT e_name FROM employee WHERE e_ID='"+str(data[1])+"'")
        table_e=c.fetchall()
        for name in table_e:
            table_who_work.add_row([data[0],data[1],name[0]])#add data
    print(table_who_work)
    lbl_show_tabel_work_car.config(text=table_who_work)

def check_work_duration():
    employee=value_e1_id.get()
    c.execute("SELECT employee_ID,car_ID FROM work_schedule WHERE employee_ID='"+employee+"'")
    record=c.fetchall()
    print(record)
    
    table_who_work_duration=PrettyTable()
    table_who_work_duration.field_names=["employee ID","name","car id","car name","start_time","end time","duration time"]
    for data in record:
        c.execute("SELECT c_ID,car_name,start_time,end_time,duration FROM car_info WHERE c_ID='"+str(data[1])+"'")
        table_c=c.fetchall()
        for carinfo in table_c:
            print(carinfo)
            c.execute("SELECT e_name FROM employee WHERE e_ID='"+str(data[0])+"'")
            table_e=c.fetchall()
            print(table_e)
            for e_name in table_e:
                table_who_work_duration.add_row([data[0],e_name[0],carinfo[0],carinfo[1],carinfo[2],carinfo[3],carinfo[4]])#add data
    
    print(table_who_work_duration)
    lbl_show_tabel_work_duration.config(text=table_who_work_duration)

def check_work_free():
    status="free"
    c.execute("SELECT * FROM employee WHERE e_status='"+status+"'")
    record=c.fetchall()
    print(record)
    table_who_work_free=PrettyTable()
    table_who_work_free.field_names=["employee ID","name","status"]
    for data in record:
        table_who_work_free.add_row([data[0],data[1],data[2]])#add data
    print(table_who_work_free)
    lbl_show_tabel_work_free.config(text=table_who_work_free)

window=Tk()
window.geometry("1200x700")
window.minsize(width=1200,height=800)

lbl_welcome=Label(text="Welcome",font=(10))
#lbl_welcome.grid(columnspan=2,column=0,row=0)


lf_operation=LabelFrame(window,text="Database operation" ,fg="blue",width=250, height=180)
lf_operation.pack_propagate(0)
lf_operation.grid(column=0,row=0)

btn_create_employee=Button(lf_operation,text="Create Employee" ,command=create_employee)
btn_create_employee.grid(column=0,row=0)

btn_create_car=Button(lf_operation,text="Create car" ,command=create_car)
btn_create_car.grid(column=1,row=0)
btn_create_work=Button(lf_operation,text="Create work table" ,command=create_work)
btn_create_work.grid(column=0,row=1)

btn_new_week=Button(lf_operation,text="New Week" ,command=new_week)
btn_new_week.grid(column=1,row=1)

#lf_table_work=LabelFrame(window,text="table_employee" ,fg="blue",width=250, height=180)
#lf_table_work.pack(fill="none", expand="no", padx=10, pady=10)
#lf_table_work.pack_propagate(0)
#lf_table_work.pack()

lf_work=LabelFrame(window,text="worker operation" ,fg="blue",width=250, height=180)
lf_work.pack_propagate(0)
lf_work.grid(column=0,row=1)

lbl_work1_id=Label(lf_work,text="First Work ID")
lbl_work1_id.grid(column=0,row=0)
lbl_work2_id=Label(lf_work,text="Second Work ID")
lbl_work2_id.grid(column=2,row=0)
lbl_e1_id=Label(lf_work,text="First Employee  ID")
lbl_e1_id.grid(column=0,row=1)
lbl_e2_id=Label(lf_work,text="Second Employee ID")
lbl_e2_id.grid(column=2,row=1)
lbl_c_id=Label(lf_work,text="Car ID")
lbl_c_id.grid(column=0,row=2)
lbl_start_time=Label(lf_work,text="Start time")
lbl_start_time.grid(column=0,row=3)
lbl_end_time=Label(lf_work,text="End time")
lbl_end_time.grid(column=0,row=4)
lbl_duration=Label(lf_work,text="Duration time")
lbl_duration.grid(rowspan=2,column=2,row=3)
lbl_day=Label(lf_work,text="Day")
lbl_day.grid(column=0,row=5)

value_work1_id=Entry(lf_work)
value_work1_id.grid(column=1,row=0)
value_work2_id=Entry(lf_work)
value_work2_id.grid(column=3,row=0)
value_e1_id=Entry(lf_work)
value_e1_id.grid(column=1,row=1)
value_e2_id=Entry(lf_work)
value_e2_id.grid(column=3,row=1)
value_c_id=Entry(lf_work)
value_c_id.grid(column=1,row=2)
value_start_time=Entry(lf_work)
value_start_time.grid(column=1,row=3)
value_end_time=Entry(lf_work)
value_end_time.grid(column=1,row=4)
value_duration=Entry(lf_work)
value_duration.grid(rowspan=2,column=3,row=3)
value_day=Entry(lf_work)
value_day.grid(column=1,row=5)


btn_submit=Button(lf_work,text="strat work" ,command=start_work)
btn_submit.grid(column=0,row=6)
btn_submit=Button(lf_work,text="end work" ,command=end_work)
btn_submit.grid(column=1,row=6)
btn_morning=Button(lf_work ,text="morning" ,command=morning)
btn_morning.grid(column=0,row=7)
btn_afternoon=Button(lf_work ,text="afternoon",command=afternoom)
btn_afternoon.grid(column=1,row=7)
btn_night=Button(lf_work ,text="night",command=night)
btn_night.grid(column=2,row=7)

btn_monday=Button(lf_work,text="Monday" ,command=monday)
btn_monday.grid(column=0,row=8)
btn_tuesday=Button(lf_work,text="Tuesday" ,command=tuesday)
btn_tuesday.grid(column=1,row=8)
btn_wednesday=Button(lf_work,text="Wednesday" ,command=wednesday)
btn_wednesday.grid(column=2,row=8)
btn_thursday=Button(lf_work,text="Thursday" ,command=thursday)
btn_thursday.grid(column=3,row=8)
btn_friday=Button(lf_work,text="Friday" ,command=friday)
btn_friday.grid(column=4,row=8)
btn_saturday=Button(lf_work,text="Saturday" ,command=saturday)
btn_saturday.grid(column=5,row=8)
btn_sunday=Button(lf_work,text="Sunday" ,command=sunday)
btn_sunday.grid(column=6,row=8)


lf_who_work_day=LabelFrame(window,text="who work in specific day" ,fg="blue",width=250, height=180)
lf_who_work_day.pack_propagate(0)
lf_who_work_day.grid(column=0,row=2)
btn_check_who_work_day=Button(lf_who_work_day,text="check in day who work",command=check_work)
btn_check_who_work_day.grid(column=0,row=0)
lbl_show_tabel_work=Label(lf_who_work_day,font=("Courier",10,"bold"))
lbl_show_tabel_work.grid(column=0,row=1)

lf_who_work_car=LabelFrame(window,text="who work on specific car" ,fg="blue",width=250, height=180)
lf_who_work_car.pack_propagate(0)
lf_who_work_car.grid(column=1,row=2)
btn_check_who_work_car=Button(lf_who_work_car,text="check who work on specific car",command=check_work_car)
btn_check_who_work_car.grid(column=0,row=0)
lbl_show_tabel_work_car=Label(lf_who_work_car,font=("Courier",10,"bold"))
lbl_show_tabel_work_car.grid(column=0,row=1)

lf_who_work_duration=LabelFrame(window,text="who work duration time" ,fg="blue",width=250, height=180)
lf_who_work_duration.pack_propagate(0)
lf_who_work_duration.grid(column=0,row=4)
btn_check_who_work_duration=Button(lf_who_work_duration,text="check who work duration time",command=check_work_duration)
btn_check_who_work_duration.grid(column=0,row=0)
lbl_show_tabel_work_duration=Label(lf_who_work_duration,font=("Courier",10,"bold"))
lbl_show_tabel_work_duration.grid(column=0,row=1)

lf_who_work_free=LabelFrame(window,text="who work free" ,fg="blue",width=250, height=180)
lf_who_work_free.pack_propagate(0)
lf_who_work_free.grid(column=2,row=2)
btn_check_who_work_free=Button(lf_who_work_free,text="check who work free",command=check_work_free)
btn_check_who_work_free.grid(column=0,row=0)
lbl_show_tabel_work_free=Label(lf_who_work_free,font=("Courier",10,"bold"))
lbl_show_tabel_work_free.grid(column=0,row=1)

window.mainloop()