from connectDatabase import create_table
from checks import *
import re

class TaskManager:
    def __init__(self,mydb) -> None:
        self.mydb = mydb
        if not self.mydb:
            print('Cannot Access the Database...')
            print('Please check if the database is connected or not...')
            return
        create_table(self.mydb)

    def add_task(self) -> str:
        # getting input for title
        task_name = input("Enter task title(25): ")
        task_name = title_check(task_name)
        if not task_name:
            return "Try Again..."

        # getting input for description 
        desc = input("Enter task description(100): (default: desc) ") or "desc"
        desc = description_check(desc)
        if not desc:
            return "Try Again..."

        # getting input for priority
        priority = input("Enter task priority(High/Normal/Low):(default: Normal) ") or "normal" 
        priority = priority_check(priority)
        if not priority:
            return "Try Again..."
        
        # getting input for status
        status = input("Enter task status (Pending/In-Progress/Completed):(default: In-Process)") or "in-process"
        status = status_check(status)
        if not status:
            return "Try Again..."

        query = "INSERT INTO task (title,description,priority,status) values(%s,%s,%s,%s)"
        try:
            self.mydb.cursor().execute(query,(task_name,desc,priority,status))
            self.mydb.commit()
            return ">>> Task added successfully"
        except:
            return ">>> Task cannot added...,Enter the task correctly"

    def edit_task(self) -> str:
        id = input("Enter the task id: ")
        try:
            query = "SELECT * FROM task WHERE id="+id
            mycursor = self.mydb.cursor()
            mycursor.execute(query)
            print(mycursor.fetchall())
            key = 0
            while key<5:
                try:
                    print("1. update title \n2. update description \n3. update priority\n4. update status \n5.exit")
                    key = int(input("Enter the choice (1-5): "))
                    if(key==1):
                        title = input("Enter the updated title(25): ")
                        title = title_check(title)
                        if not title:
                            return "Try Again..."
                        query = "UPDATE task SET title=%s WHERE id=%s"
                        try:
                            mycursor.execute(query,(title,id))
                            self.mydb.commit()
                            return ">>> Title updated successfully"
                        except:
                            return ">>> Title updated failed, Enter the valid Title within 25 words"

                    elif(key==2):
                        desc = input("Enter the updated description(100): ")
                        query = "UPDATE task SET description=%s WHERE id=%s"
                        try:
                            mycursor.execute(query,(desc,id))
                            self.mydb.commit()
                            return ">>> Description updated successfully"
                        except:
                            return ">>> Description update Failed, Enter the valid description within 100 words"
                    
                    elif(key==3):
                        priority = input("Enter task priority(High/Medium/Low):")
                        priority = priority_check(priority)
                        if not priority:
                            return "Try Again..."
                        query = "UPDATE task SET priority=%s WHERE id=%s"
                        try:
                            mycursor.execute(query,(priority,id))
                            self.mydb.commit()
                            return ">>> Priority updated successfully"
                        except:
                            return ">>> priority update Failed"
                        
                    elif(key==4):
                        status = input("Enter task status (Pending/In-Progress/Completed):")
                        status = status_check(status)
                        if not status:
                            return "Try Again..."
                        query = "UPDATE task SET status=%s WHERE id=%s"
                        try:
                            mycursor.execute(query,(status,id))
                            self.mydb.commit()
                            return ">>> Status updated successfully"
                        except:
                            return ">>> Status update failed"
                except:
                    key = 0
                    print(">>> Please enter the valid value!")
        except:
            return ">>> Id not found ..."
    
    def delete_task(self) -> str:
        id = input("Enter the delete id: ")
        query = f"DELETE FROM task WHERE id={id}"
        try:
            mycursor = self.mydb.cursor()
            mycursor.execute(query)
            self.mydb.commit()
            return ">>> Deleted Successfully"
        except Exception as ex:
            return ">>> Enter the correct id"+type(ex).__name__,ex.args
        
    def filter_tasks_by_priority(self):
        query = "SELECT * FROM task"
        mycursor = self.mydb.cursor()
        mycursor.execute(query)
        data = mycursor.fetchall()
        if not data:
            print(">>> Enter the task first...")

        ref = {"high":1,"normal":0,"low":-1}
        temp = sorted(data,key=lambda data:ref[data[3]],reverse=True)
        for task in temp:
            print(f"id: {task[0]}\ttitle: {task[1]}\tdescription: {task[2]}\tpriority: {task[3]}\tstatus: {task[4]}")
    
    def __exit__(self):
        self.mydb.close()
        print("Connection Closed...")