
from lagring import export_report_as_csv
from meny import show_menu, add_server, check_a_server_by_name,delete_a_server_by_name,show_all_server,view_servers_in_a_spec_env,check_all_server

def main():
    show_menu()
    while True:
          select_option = input("Select option(1-8): ").strip()
          if select_option == "1":
              show_all_server()
          elif select_option == "2":
               view_servers_in_a_spec_env()
          elif select_option == "3":
               add_server()
          elif select_option == "4":
               delete_a_server_by_name()
          elif select_option == "5":
               check_a_server_by_name()
          elif select_option == "6":
               check_all_server()
          elif select_option == "7":
               export_report_as_csv()
          elif select_option == "8":
               break
          else:
               print("Invalid option has been selected!")
          
     
if __name__ == "__main__":
    main()