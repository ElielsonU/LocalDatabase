from app.utils.gerador import New_name
from app.work import Name_exist
from app.work.backend import Add_name

def main():
    while True:
        name = New_name()
        if not Name_exist(name):
            Add_name(name)
            print(f'A new word has saved: "{name}"')
            break
        else: 
            print("That name already exists!")
            break
if __name__ == "__main__":
    main()