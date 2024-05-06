from task import Task
import re

class TaskManager:
    def __init__(self) -> None:
        self.task_list = []
        self.exportInd = -1
        self.importFlag = False
        self.isChanged = False

    def add_task(self) -> str:
        task_name = input("Enter task title: ")
        tchance = 3

        while not bool(re.match('^[a-zA-Z]+$',task_name)) and tchance!=0:
            print(f'you have only {tchance} left !')
            print("Enter only alpha character only")
            task_name = input("Enter task title: ")
            tchance -=1 

        if(tchance==0) and not bool(re.match('^[a-zA-Z]+$',task_name)):
            print("you attain the maximum chance")
            return 
        
        desc = input("Enter task description: (default: desc) ") or "desc"
        priority = input("Enter task priority(High/Medium/Low):(default: Medium) ") or "medium" 
        
        pchance = 3
        while priority.lower() != "low" and priority.lower() != "medium" and priority.lower() != "high" and pchance!=0:
            print(f">>> Enter correct value, you have only {pchance} left")
            priority = input("Enter task priority (High/Medium/Low): ")
            pchance -= 1
        
        if(pchance==0) and priority.lower() != "low" and priority.lower() != "medium" and priority.lower() != "high":
            print("you attain the maximum chance")
            return 
        
        schance = 3
        status = input("Enter task status (Pending/Progress/Completed):(default: Progress)") or "Progress"
        while status.lower() != "pending" and status.lower() != "progress" and status.lower() != "completed" and schance!=0: 
            print(f">>> Enter correct value, you have only {schance} left")
            status = input("Enter task status (Pending/Progress/Completed):(default: Progress)") or "Progress"
            schance -= 1

        if(schance==0) and status.lower() != "pending" and status.lower() != "progress" and status.lower() != "completed":
            print("you attain the maximum chance")
            return 
        
        self.task_list.append(Task(task_name,desc=desc,priority=priority,status=status))
        return ">>> Task added successfully"

    def edit_task(self) -> str:
        self.isChanged = True
        id = int(input("Enter the task id: "))
        while task:=self.get_task_by_id(id):
            key = 0
            while key<5:
                try:
                    print("1. update title \n2. update description \n3. update priority\n4. update status \n5.exit")
                    key = int(input("Enter the choice (1-5): "))
                    if(key==1):
                        title = input("Enter the updated title: ")
                        tchance = 3
                        while not bool(re.match('^[a-zA-Z]+$',title)) and tchance!=0:
                            print(f'you have only {tchance} left !')
                            print("Enter only alpha character only")
                            title = input("Enter task title: ")
                            tchance -=1 
                        if(tchance==0) and not bool(re.match('^[a-zA-Z]+$',title)):
                            print("you attain the maximum chance")
                            return
                        task.title = title
                        return ">>> Title updated successfully"

                    elif(key==2):
                        desc = input("Enter the updated description: ")
                        task.desc = desc
                        return ">>> description updated successfully"
                    
                    elif(key==3):
                        priority = input("Enter task priority(High/Medium/Low):") 
                        pchance = 3

                        while priority.lower() != "low" and priority.lower() != "medium" and priority.lower() != "high" and pchance!=0:
                            print(f">>> Enter correct value, you have only {pchance} left")
                            priority = input("Enter task priority (High/Medium/Low): ")
                            pchance -= 1

                        if(pchance==0) and task.priority.lower() != "low" and task.priority.lower() != "medium" and task.priority.lower() != "high":
                            print("you attain the maximum chance")
                            return 
                        
                        task.priority = priority
                        return ">>> priority updated successfully"
                    elif(key==4):

                        schance = 3
                        status = input("Enter task status (Pending/Progress/Completed):(default: Progress)") or "Progress"
                        while status.lower() != "pending" and status.lower() != "progress" and status.lower() != "completed" and schance!=0: 
                            print(f">>> Enter correct value, you have only {schance} left")
                            status = input("Enter task status (Pending/Progress/Completed):(default: Progress)") or "Progress"
                            schance -= 1

                        if(schance==0) and status.lower() != "pending" and status.lower() != "progress" and status.lower() != "completed":
                            print("you attain the maximum chance")
                            return  
                        
                        task.status = status
                        return ">>> Status updated successfully"
                except:
                    key = 0
                    print(">>> Please enter the valid value!")
                    
        return "Id not found"
    
    def delete_task(self) -> str:
        id = int(input("Enter the delete id"))
        if task := self.get_task_by_id(id):
            self.task_list.remove(task)
            self.isChanged = True
            return 'Deleted Successfully'
    
        return "Task is not Founded"
        
    def get_task_by_id(self,id:int) -> Task:
        left,right=0,len(self.task_list)-1
        mid = (left+right)//2
        while(left<=right):
            if(self.task_list[mid].id == id):
                return self.task_list[mid]
            elif self.task_list[mid].id < id:
                left = mid+1
                mid = (left+right)//2
            else:
                right = mid-1
                mid = (left+right)//2
        return None

    def view_all_tasks(self) ->None:
        if not len(self.task_list):
            print("Add the Taskes first")
        for task in self.task_list:
            print(task)

    def filter_tasks_by_priority(self):
        if(len(self.task_list)==0):
            print("\n>>>Add the Task First\n")
        
        ref = {"high":1,"medium":0,"low":-1}
        temp = sorted(self.task_list,key=lambda task:ref[task.priority],reverse=True)
        for task in temp:
            print(task)

    def Import(self):
        if(self.importFlag):
            print("Imported Successfully")
            return
        
        f = open("db.txt","r")
        for line in f:
            line = line[:-1] #trim last part
            line = line.split(',')
            values = []
            for j in line:
                j = j.split(':')
                values.append(j[1])
            self.task_list.append(Task(values[1],values[2],values[3],values[4]))
        f.close()
        self.exportInd = len(self.task_list)
        self.importFlag = True

    def Export(self):
        if(self.isChanged):
            f = open("db.txt","w")
            for i in self.task_list:
                f.write(str(i)+'\n')
            print(">>> Tasks Saved Successfully")
            return

        f = open("db.txt","a")
        for i in range(self.exportInd,len(self.task_list)):
            f.write(str(self.task_list[i])+'\n')
        print(">>> Tasks Saved Successfully")
        f.close()


