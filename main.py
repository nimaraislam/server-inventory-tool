from meny import show_menu
from lagring import add_server
from query import check_a_server_by_name,delete_a_server_by_name,show_all_server,view_servers_in_a_spec_env



def main():
    
   
     show_menu()
     #add_server()
     #check_a_server_by_name()
     #delete_a_server_by_name()
     show_all_server()
     view_servers_in_a_spec_env()
     
     
    
if __name__ == "__main__":
    main()