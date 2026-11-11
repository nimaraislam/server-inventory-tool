from datetime import datetime
from lagring import load_data,save_data
from kontroller import ping_address

def show_menu():
    print("========== Service Status Tool ==========")
    print("1. Show all servers")
    print("2. View servers in a specific environment")
    print("3. Add a server")
    print("4. Delete a server")
    print("5. Check a server")
    print("6. Check all servers")
    print("7. Export report as CSV")
    print("8. Exit")
    print("========== ========== ========== ==========")

def print_table_header():
    print(f"{'Server Name':<15}{'Address':<20}{'Environment':<14}{'Role':<20}{'Status':<8}"
          f"{'Last checked':<17}")
    print("-" * 95)


def print_data_as_table(server):
    print(f"{server['name'].strip():<15}{server['address'].strip():<20}{server['environment'].strip():<14}"
          f"{server['role'].strip():<20}{server['status'].strip():<8}{server['last_checked'].strip():<17}")
    
def details_of_a_server_by_name(server):
    print()
    print(f"-----------Detail information-----------")
    print("-" * 40)
    print(f"Server Name: {server['name']}\n"
    f"Address: {server['address']}\n"
    f"Environment: {server['environment']}\n"
    f"Role: {server['role']}\n"
    f"Status: {server['status']}\n"
    f"Last Checked: {server['last_checked']}")
    print("-" * 40)
    return server
    
def show_all_server():
    servers = load_data()
    print_table_header()
    for server in servers:
       print_data_as_table(server)
       
def view_servers_in_a_spec_env():
    servers = load_data()
    env = ["prod","dev","test"]
    environment = input("Environment(prod/dev/test): ").lower().strip()
    while environment not in env:
        print(f"Environment '{environment}' is not valid")
        environment = input("Environment(prod/dev/test): ").lower().strip()
    print_table_header()
    for server in servers:
       if server["environment"].lower().strip() == environment:
            print_data_as_table(server)
 
def add_server():
    servers = load_data()
    
    name = input("Server Name: ").lower().strip()
    while name == "":
        print("Server name is empty.")
        name = input("Server Name: ").lower().strip()
    for server in servers:
        if server["name"].lower().strip() == name:
            print("This server name is already existed.Try another one!")
            name = input("Server Name: ").lower().strip()
    address = input("Address: ").lower().strip()
    env = ["prod","dev","test"]
    environment = input("Environment(prod/dev/test): ").lower().strip()
    while environment not in env:
        print(f"Environment '{environment}' is not valid")
        environment = input("Environment(prod/dev/test): ").lower().strip()
    role = input("Role: ").lower().strip()
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
    print("A new server has been successfully added!")

def delete_a_server_by_name():
    name = input("Server Name: ").lower().strip()
    servers=load_data()
        
    found_server = None
    for server in servers:
        if server["name"].lower().strip() == name:
            found_server = server
            details_of_a_server_by_name(found_server)
            break
            
    if found_server == None:
        print(f"This server ({name}) is not in list")
        return
    
    delete_server = input("Are you sure you want to delete this server?[Y/N]: ").upper().strip()
    if delete_server=="Y":
        servers.remove(found_server)
        save_data(servers)
        print("Server has been deleted successfully!")
    elif delete_server == "N":
        return
    else:
        print("Press only Y or N!") 
    
def check_a_server_by_name():
    name = input("Server Name: ").lower().strip()
    servers=load_data()
    
    found_server = None
    for server in servers:
        if server["name"].lower().strip() == name:
            found_server = server
            break
        
    if found_server == None:
        print(f"This server ({name}) is not in list")
        return
            
    is_up = ping_address(found_server["address"].lower().strip())
    if is_up == True:
        found_server["status"] = "up"
    else:
        found_server["status"] = "down"
    found_server["last_checked"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            
    save_data(servers)
    details_of_a_server_by_name(server)
    
def check_all_server():
    print_table_header()
    servers=load_data()
    
    if not servers:
        print("No server found!")
        return
    
    for server in servers:
        is_up = ping_address(server["address"].lower().strip())
        if is_up == True:
            server["status"] = "up"
        else:
            server["status"] = "down"
        server["last_checked"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        print_data_as_table(server)
    save_data(servers)
    
    
    
                
    


                     

        