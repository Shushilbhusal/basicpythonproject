print("***************** SIMPLE TO DO LIST *****************\n")
list=[]
print("Enter the number according to given menu\n")
print("1. Add task")
print("2. View all tasks")
print("3. Remove task")
print("4. Exit")

user_choice=int(input("what do you want to do ?  "))




def Add_task():
    task=input("Enter the task : ")
    list.append(task)
    print("Task added successfully")
def View_all_tasks():
    for _ in range(len(list)):
        print(list)
def Remove_task():
    task=input("Enter the task you want to remove : ")
    list.remove(task)
    print("Task removed successfully")
def Exit():
    pass


if(user_choice==1):
    Add_task()
elif(user_choice==2):
    View_all_tasks()
elif(user_choice==3):
    Remove_task()
elif(user_choice==4):
    exit()
