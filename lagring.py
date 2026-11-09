import json
def add_server():
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
    
    server=  {
        "name": name ,
        "address": address ,
        "environment": environment ,
        "role": role ,
        "status": status ,
        "last_checked": last_checked
  }
    
    with open("servrar.json", "w", encoding="utf-8") as file:
        json.dump(
            server,
            file,
            indent=2,
            ensure_ascii=False
        )
    