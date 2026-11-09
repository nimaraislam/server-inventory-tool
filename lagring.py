import json
import os

def load_data():
    if not os.path.exists("servrar.json"):
        return []
    with open("servrar.json", "r", encoding="utf-8") as file:
            servers = json.load(file)
    if not servers:
        return []
    return servers

def save_data(new_server):
        with open("servrar.json", "w", encoding="utf-8") as file:
            json.dump(
                new_server,
                file,
                indent=2,
                ensure_ascii=False
            )

def add_server():
    servers = load_data()
    
    name = input("Server Name: ").lower().strip()
    address = input("Address: ").lower().strip()
    env = ["prod","dev","test"]
    environment = input("Environment(prod/dev/test): ").lower().strip()
    while environment not in env:
        print(f"Environment '{environment}' is not valid")
        environment = input("Environment(prod/dev/test): ").lower().strip()
    role = input("Role: ").lower().strip()
    valid_status = ["running","stopped"]
    status = input("Status: ").lower().strip()
    if status not in valid_status:
        status = "unknown"
    last_checked = ""
    
    new_server=  {
        "name": name ,
        "address": address ,
        "environment": environment ,
        "role": role ,
        "status": status ,
        "last_checked": last_checked
    }
    servers.append(new_server)
    save_data(servers)
    
    