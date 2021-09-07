import argparse
import getpass
from os import path
import sys
import json
import datetime

user = getpass.getuser()

class fmt:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def write_json(info, key, filename):
    if not path.exists(filename):
        make = {"tasks": []}
        with open(filename, "w") as uwu:
            uwu.write(json.dumps(make, indent=4))

    with open(filename) as json_file:
        data = json.load(json_file)
    data[key].append(info)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def add_tasks(task):
    date_time = str(datetime.datetime.today()).split()
    end_date  = input("Ending date in DD/MM/YEAR (optional) : ")

    add_task = {
    	"name"       : task,
    	"start_date" : date_time[0],
    	"status"     : "Not Finished",
    	"end"		 : end_date
    }
    write_json(add_task, "tasks", f'/home/{user}/.todo.json')

def remove_tasks(index):
    with open(f'/home/{user}/.todo.json') as file:
        data = json.load(file)
    data["tasks"].pop(index-1)
    with open(f'/home/{user}/.todo.json','w') as f:
        json.dump(data,f,indent=4)

def list_tasks():
    print("\n"+fmt.BOLD+fmt.HEADER+"Tasks :"+fmt.END+"\n")
    with open(f'/home/{user}/.todo.json',"r") as lists :
        data = json.load(lists)
        for i,j in enumerate(data["tasks"]):
            tasks = j
            if tasks["end"] == "":
                print(fmt.GREEN+f'{i+1} : '+fmt.END+tasks["name"])
            else:
                start = datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%d'),"%Y-%m-%d")
                end = datetime.datetime.strptime(tasks["end"],"%Y-%m-%d")
                days = (end-start).days
                if days < 10 :
                    print(fmt.FAIL+f'{i+1} : '+tasks["name"]+fmt.END+f'({days}d)')
                elif days < 30 :
                    print(fmt.WARNING+f'{i+1} : '+tasks["name"]+fmt.END+f'({days}d)')
                else:
                    print(fmt.GREEN+f'{i+1} : '+fmt.END+tasks["name"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--add",help="Add a todo",metavar="")
    parser.add_argument("-r","--rem",help="remove todo based on index",type=int,metavar="")
    parser.add_argument("-l","--list",help="list all tasks",action='store_true')
    parse = parser.parse_args()

    if parse.add :
        add_tasks(parse.add)
    elif parse.rem :
        remove_tasks(parse.rem)
    elif parse.list :
        list_tasks()