import re

def title_check(task_name):
    tchance = 3   
    while not bool(re.match('^[a-zA-Z]+$',task_name)) and tchance!=0:
        print(f'you have only {tchance} left !')
        print("Enter only alphabet character with in 25 charaters")
        task_name = input("Enter task title: ")
        tchance -=1 
    if(tchance==0) and not bool(re.match('^[a-zA-Z]+$',task_name)):
        print("you attain the maximum chance")
        return None
    return task_name

def description_check(desc):
    chance = 3
    while len(desc)>99 and chance!=0:
        print(f'you hava only {chance} left !')
        print("Enter the desciption with in 100 words...")
        desc = input("Enter task description(100): ")
        chance -=1
    if(chance==0) and len(desc)>99:
        print("you attain the maximun chance")
        return None
    return desc

def priority_check(priority):
    pchance = 3
    while priority.lower() != "low" and priority.lower() != "normal" and priority.lower() != "high" and pchance!=0:
        print(f">>> Enter correct value, you have only {pchance} left")
        priority = input("Enter task priority (High/Normal/Low): ")
        pchance -= 1
    
    if(pchance==0) and priority.lower() != "low" and priority.lower() != "normal" and priority.lower() != "high":
        print("you attain the maximum chance")
        return None
    return priority

def status_check(status):
    schance = 3
    while status.lower() != "pending" and status.lower() != "in-process" and status.lower() != "completed" and schance!=0: 
        print(f">>> Enter correct value, you have only {schance} left")
        status = input("Enter task status (Pending/In-Progress/Completed): ")
        schance -= 1
    if(schance==0) and status.lower() != "pending" and status.lower() != "in-process" and status.lower() != "completed":
        print("you attain the maximum chance")
        return None
    return status
    