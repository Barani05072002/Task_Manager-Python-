class Task:
    total_task = 0
    def __init__(self,title,desc,priority,status) -> None:
        Task.total_task +=1
        self.id = Task.total_task
        self.title = title
        self.desc = desc
        self.priority = priority
        self.status = status

    def __str__(self) -> str:
        return f'Task ID: {self.id}, Title:{self.title}, Description:{self.desc}, Priority:{self.priority}, status:{self.status}'
        