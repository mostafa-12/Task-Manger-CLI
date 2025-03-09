import json


class Task:
    def __init__(self, name, discrib, priorityLevels, deadline,status = False):
        self.__name = name
        self.__discrib = discrib
        self.__priorityLevels = priorityLevels
        self.__status = status
        self.__deadline = deadline

    def getstatus(self):
        return self.__status
    def getpriorityLevels(self):
        return self.__priorityLevels
    def getdeadline(self):
        return self.__deadline
    def getname(self):
        return self.__name
    def getdiscrib(self):
        return self.__discrib

    def makeDone(self):
        self.__status = True

    def toDict(self):
        return {
            "name": self.__name,
            "discrib": self.__discrib,
            "priorityLevels": self.__priorityLevels,
            "status": self.__status,
            "deadline": self.__deadline

        }
    def toJson(self):
        data = json.dumps(self.toDict())
        return data
    @classmethod
    def fromJson(cls, data):
        data = json.loads(data)
        return cls(data["name"], data["discrib"], data["priorityLevels"], data["deadline"], data["status"])


