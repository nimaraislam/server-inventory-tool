from lagring import load_data,save_data

def details_of_aserver_by_name(name):
    servers = load_data()
    print()
    print(f"*********Detail information*********")
    print("-----------------------------------------")
    for server in servers:
            if server["name"] == name:
                print(f"Server Name: {server['name']},\n"
                      f"Address: {server['address']},\n"
                      f"Environment: {server['environment']},\n"
                      f"Role: {server['role']},\n"
                      f"Status: {server['status']},\n"
                      f"Last Checked: {server['last_checked']}")
                print("-------------------------------------\n")
                return server
    
    print(f"This server ({name}) is not in list")
    return None
    
    
def check_a_server_by_name():
    name = input("Server Name: ").lower().strip()
    details_of_aserver_by_name(name)
    
def delete_a_server_by_name():
    name = input("Server Name: ").lower().strip()
    delete_server = details_of_aserver_by_name(name)
    if delete_server is None:
        return
    flag = input("Are you sure you want to delete this server?[Y/N]: ").upper().strip()
    
    if flag=="Y":
        servers = load_data()
        servers.remove(delete_server)
        save_data(servers)
        print("Server has been deleted successfully!")
    elif flag == "N":
        return
    else:
        print("Press only Y or N!")

def print_table_header():    
    print(f"Server Name\t\tAddress\t\tEnvironment\t\tRole\t\tStatus")
    print("---------------------------------------------------------------------------------------")
def print_data_as_table(server):
    print(f"{server["name"]}\t\t\t{server["address"]}\t\t\t{server["environment"]}\t\t{server["role"]}\t\t{server["status"]}")
                     
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
       if server["environment"] == environment:
            print_data_as_table(server)
        

    
    
    

    