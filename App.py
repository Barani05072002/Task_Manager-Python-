from taskmanager import TaskManager 
if __name__ == '__main__':
    dashboard  = TaskManager()
    dashboard.Import()
    sure = 0
    while sure<2:
        try:
            select = 0
            while select<5:
                try:
                    print("1. Add Task\n2. Edit Task\n3. Delete Task\n4. View All(By Priority)\n5. Exit")
                    select = int(input("Enter your choice (1-6): "))
                    if select == 1:
                        print(dashboard.add_task())
                    elif select == 2:
                        print(dashboard.edit_task())
                    elif select == 3:
                        print(dashboard.delete_task())
                    elif select == 4:
                        dashboard.filter_tasks_by_priority()
                except:
                    print(">>>Enter the correct choice...\n")
            else:
                print("Are you sure want to Exit?\n1. No\n2. Yes")
                sure = int(input("Enter the choice 1 or 2: "))
        except:
            print("Enter the correct choice...\n")
    else:
        dashboard.Export()
        print("Thank you\n")

