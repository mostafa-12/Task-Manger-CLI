import user
import task
import managing
import encryption

def main():
    while True:
        print("Hello everyone!")
        print("1-create a new user\n2-login\n3-backup\n4-restore\n5-exit : ",end="")
        choice = input()
        updata = False
        if choice == "1":
            print("Creating a new user, please enter username-password")
            userInfo = (input(" : ")).split("-")
            _user = user.User(userInfo[0], userInfo[1])
            print("do you want to add tasks? (y,n) : ",end="")
            choice = input()
            while choice != "y" and choice != "n":
                print("invalid input, enter y or n : ",end="")
                choice = input()
            if choice == "y":
                print("creating new task :), pleas enter =>task name-discrib-priority Levels('high,medium,low priority')-deadline")
                taskInfo = (input(" : ")).split("-")
                _task = task.Task(taskInfo[0], taskInfo[1], taskInfo[2], taskInfo[3])
                _user.addTask(_task)
            elif choice == "n":
                    pass

        elif choice == "2":
            updata = True
            usersAtJson = managing.FileManager.load()
            if usersAtJson == None:
                print("there is not any users to login , creat one first and then login pro :)")
                return

            usersAtJson = managing.FileManager.load()["users"]
            users = [user.User.init_user_byDict(_user) for _user in usersAtJson]
            while True:
                print("please enter username-password")
                userInfo = (input(" : ")).split("-")
                _user = getUser(users, userInfo[0], userInfo[1])
                if _user == None:
                    print("username or password is incorrect")
                    continue
                _user.setTasks(convertTasks(_user.gettasks()))
                while True:
                    print(f"hello {_user.getname()}, welcome back")
                    print("what would you like to do?")
                    print("1-show all tasks\n2-add task\n3-select tasks\n4-exit : ",end="")
                    choice = input()
                    if choice == "1":
                        for _task in _user.gettasks():
                            print(f"{_task.getname()}, {_task.getdiscrib()}, {_task.getpriorityLevels()}, {_task.getstatus()}, {_task.getdeadline()}")
                    elif choice == "2":
                        print("enter task details as => name-discrib-priorityLevels-deadline-status(False as default) : ",end="")
                        taskInfo = (input(" : ")).split("-")
                        _task = task.Task(*taskInfo)
                        _user.addTask(_task)
                        print(f"{taskInfo} added successfully👌😁")
                    elif choice == "3":
                        print("enter task name : ",end="")
                        taskName = input()
                        for _task in _user.gettasks():
                            if _task.getname() == taskName:
                                print("task exists")
                                print(f"{_task.getname()}, {_task.getdiscrib()}, {_task.getpriorityLevels()}, {_task.getstatus()}, {_task.getdeadline()}")
                                print("do you achive this task? (y,n) : ",end="")
                                answer = input()
                                if answer == "y":
                                    _task.makeDone()
                                elif answer == "n":
                                    print(f"harry you can do it at the dead line{_task.getdeadline()}")
                                    

                            else:
                                print(f"there is no task with this name {taskName}, please try again")
                                continue
                    elif choice == "4":
                        break
                    else:
                        print("invalid input,please try again")
                break

        elif choice == "3":
            backupResulte = managing.BackupRestore.backup()
            if backupResulte :
                print("backuped succesfuly to C:\\backup\\users.json")
            else:
                print("there is not data to backup it")
                return
        elif choice == "4":
            restoreResulte = managing.BackupRestore.backup()
            if restoreResulte :
                print("restored succesfuly from C:\\backup\\users.json")
            else:
                print("there is not data to restore it")
                return
        elif choice == "5":
            exit()
        else:
            print("Wrong choice")

        saveAndUpdata(_user,updata=updata)

def encrypting(userAsDict,updata = False):
    hashedPassword = userAsDict["password"]
    if updata == False:
        hashedPassword = encryption.Auth.hashing(userAsDict["password"])
    tasks = userAsDict["tasks"]
    encryptedTasks = []
    for _task in tasks:
        encryptedTasks.append(encryption.Encrypt.encrypt(_task))
    userAsDict = {
        "name" : userAsDict["name"],
        "password" : hashedPassword,
        "tasks" : encryptedTasks
    }
    return user.User.init_user_byDict(userAsDict)


def getUser(users, name, password):
    for _user in users:
        if encryption.Auth.check(_user, name, password):
            return _user
    return None




def convertTasks(tasks):
    tasks = [encryption.Encrypt.decrypt(Task) for Task in tasks]
    tasks = [task.Task.fromJson(Task) for Task in tasks]
    return tasks

def saveAndUpdata(_user,updata = False):
    tasks = []
    for _task in _user.gettasks():
        tasks.append(_task.toJson())
    _user.setTasks(tasks)
    _user = encrypting(_user.infoToDict(),updata=updata)
    managing.FileManager.save(_user.infoToDict())


if __name__ == '__main__':
    main()