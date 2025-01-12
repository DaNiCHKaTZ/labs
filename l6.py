import time
import random

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

class Deque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        return None

    def remove_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        return None

    def peek_front(self):
        if not self.is_empty():
            return self.deque[0]
        return None

    def peek_rear(self):
        if not self.is_empty():
            return self.deque[-1]
        return None

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

# Создаем экземпляры классов Stack, Queue и Deque
students_queue = Queue()
tickets_stack = Deque()  
problems_deque = Deque()
answering_queue = Queue()

# Заполняем стек билетов и дек задач
for i in range(1, 11):
    tickets_stack.add_rear(f"Ticket {i}")  
   

    problems_deque.add_rear(f"Problem {i}")

# Бесконечный цикл моделирования операций
while True:
    # Добавление студентов в очередь на пересдачу
    if random.random() < 0.3:
        student_id = random.randint(1, 100)
        students_queue.enqueue(f"Student {student_id}")
        print(f"Student {student_id} joined the queue.")

    # Если есть студенты в очереди
    if not students_queue.is_empty():
        # Студент берет билет и задачу
        student = students_queue.dequeue()

        if random.random() < 0.5:
            ticket = tickets_stack.remove_front()
        else:
            ticket = tickets_stack.remove_rear()

        problem = problems_deque.remove_front()
        answering_queue.enqueue(student)

        print(f"Student {student} took ticket {ticket} and problem {problem}.")
        time.sleep(random.randint(1, 3))

      
        if random.random() < 0.5:
            print(f"Student {student} passed the exam!")
        else:
            students_queue.enqueue(student)
            print(f"Student {student} failed the exam and joined the end of the queue.")

        
        tickets_stack.add_rear(ticket) 
       

        problems_deque.add_rear(problem)
        time.sleep(random.randint(1, 3))