from pathlib import Path 
from datetime import datetime
import json
import csv

def load_data():
    DATAFILE = Path("servrar.json")
    if DATAFILE.exists() is False:
        return []
    with DATAFILE.open("r", encoding="utf-8") as file:
            servers = json.load(file)
    if not servers:
        return []
    return servers

def save_data(new_server):
    
    DATAFILE = Path("servrar.json")
    with DATAFILE.open("w", encoding="utf-8") as file:
        json.dump(
            new_server,
            file,
            indent=2,
            ensure_ascii=False
        )
    
def export_report_as_csv():
    servers = load_data()
    rapporter = Path("rapporter")
    rapport = rapporter /(f"inventering_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.csv")
    rapporter.mkdir(exist_ok=True)
    with open(rapport,"w",newline="", encoding="utf-8") as file:
        sk = csv.DictWriter(
                file,
                fieldnames=["name", "address","environment","role","status","last_checked"]
        )
        sk.writeheader()
        sk.writerows(servers)
