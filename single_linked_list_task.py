class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Task(description, priority)
        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            if new_task.priority > current.priority:
                new_task.next = current
                self.head = new_task
            else:
                while current.next is not None and new_task.priority < current.next.priority:
                    current = current.next
                new_task.next = current.next
                current.next = new_task

    def remove_task(self, description):
        if self.head is None:
            return

        if self.head.description == description:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.description == description:
                current.next = current.next.next
                return
            current = current.next

    def print_tasks(self):
        if self.head is None:
            print("Task list is empty.")
        else:
            current = self.head
            print("Task List:")
            while current is not None:
                print(f"Priority: {current.priority}, Description: {current.description}")
                current = current.next

task_list = TaskList()

task_list.add_task("Mengerjakan tugas", 2)
task_list.add_task("membeli bahan makanan", 1)
task_list.add_task("Memeriksa email", 3)

task_list.print_tasks()

print("---")

task_list.remove_task("membeli bahan makanan")

task_list.print_tasks()
