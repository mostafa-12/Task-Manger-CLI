import json
import os
import shutil
class FileManager:
    @staticmethod
    def save(data):
        PATH = os.path.dirname(__file__)
        dataFile = os.path.join(os.path.dirname(PATH), 'data', 'users.json')
        if not os.path.exists(dataFile):
            os.makedirs(os.path.dirname(dataFile))
            with open(dataFile, 'w') as file:
                json.dump({"users" : []}, file)

        with open(dataFile) as file:
            importedData = json.load(file)


        for user in importedData["users"]:
            if user["name"] == data["name"]:
                importedData["users"].remove(user)

        importedData["users"].append(data)
        with open(dataFile, 'w') as file:
            json.dump(importedData, file,indent=4)

    @staticmethod
    def load():
        PATH = os.path.dirname(__file__)
        dataFile = os.path.join(os.path.dirname(PATH), 'data', 'users.json')
        if not os.path.exists(dataFile):
            return
        with open(dataFile, "r") as file:
             return json.load(file)


class BackupRestore:
    @staticmethod
    def backup():
        PATH = os.path.dirname(__file__)
        dataFile = os.path.join(os.path.dirname(PATH), 'data', 'users.json')
        backupPath = os.path.join("C:", 'backup')
        if not os.path.exists(backupPath):
            os.makedirs(backupPath)
        if os.path.exists(dataFile):
            shutil.copy(dataFile, backupPath)
            return True
        else:
            return False            

    @staticmethod
    def restore():
        PATH = os.path.dirname(__file__)
        dataFile = os.path.join(os.path.dirname(PATH), 'data', 'users.json')
        backupPath = os.path.join("C:", 'backup')
        backupFile = os.path.join(backupPath, 'users.json')
        if os.path.exists(backupFile):
            shutil.copy(dataFile, backupPath)
            return True
        else:
            return False 


