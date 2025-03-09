import json
class User:
    def __init__(self, name, password, tasks = None):
        self.__name = name
        self.__password = password
        self.__tasks = [] if tasks is None else tasks

    def getname(self):
        return self.__name
    def getpassword(self):
        return self.__password
    def gettasks(self):
        return self.__tasks

    def addTask(self, task):
        self.__tasks.append(task)

    def removeTask(self, task):
        self.__tasks.remove(task)


    def setTasks(self, tasks):
        self.__tasks = tasks


    def infoToDict(self):
        data = {
            "name": self.__name,
            "password": self.__password,
            "tasks": self.__tasks,
        }
        return data
    @classmethod
    def init_user_byDict(cls,userAsDict):
        return cls(userAsDict["name"], userAsDict["password"], userAsDict["tasks"])