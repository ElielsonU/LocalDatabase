def Name_exist(inputName): 
    with open("app\database.txt") as dat4base:
        nameIs = False
        for name_bank in dat4base.read().split(", "):
            if inputName == name_bank:
                nameIs = True
        return nameIs
        
        
