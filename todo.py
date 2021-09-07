import argparse
from os import path
import sys
import json
import datetime

class fmt:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
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
    write_json(add_task, "tasks", "todo.json")

def list_tasks():
    print("\n"+fmt.BOLD+fmt.HEADER+"Tasks :"+fmt.ENDC)
    with open("todo.json","r") as lists :
        data = json.load(lists)
        for i,j in enumerate(data["tasks"]):
            tasks = j
            if tasks["end"] == "":
                print(fmt.OKGREEN+f'{i+1} : '+fmt.ENDC+tasks["name"])
            else:
                start = datetime.datetime.strptime(tasks["start_date"],"%Y-%m-%d")
                end = datetime.datetime.strptime(tasks["end"],"%Y-%m-%d")
                days = (end-start).days
                if days < 10 :
                    print(fmt.FAIL+f'{i+1} : '+tasks["name"]+fmt.ENDC+f'({days}d)')
                elif days < 30 :
                    print(fmt.WARNING+f'{i+1} : '+tasks["name"]+fmt.ENDC+f'({days}d)')
                else:
                    print(fmt.OKGREEN+f'{i+1} : '+fmt.ENDC+tasks["name"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--add",help="Add a todo",metavar="")
    parser.add_argument("-r","--rem",help="remove todo based on number",type=int,metavar="")
    parser.add_argument("-l","--list",help="list all tasks",action='store_true')
    parse = parser.parse_args()

    if parse.add :
        add_tasks(parse.add)
    elif parse.list :
        list_tasks()