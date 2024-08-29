import datetime
attendance = {}
def mark_present(name):
    attendance[name] = datetime.datetime.now()

def remove_student(name):
    attendance.pop(name)

def is_present(name):
    print(name in attendance)

def display_attendance():
    for key,value in attendance.items():
        print(f"name: {key}, time: {value}")

mark_present('sambhav')
display_attendance()
