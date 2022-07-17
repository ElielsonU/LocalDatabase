def Add_name(name):
    with open("app\database.txt", "a") as dat4base:
        print(f"{name}", file=dat4base, end=", ")
