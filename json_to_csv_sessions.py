import os
import json
import pandas as pd
from pathlib import Path
from vyper import v

def set_config(path):
    v.set_config_type("json")
    v.set_config_name('config')
    v.add_config_path(path)
    v.read_in_config()

def main():
    set_config('./config')
    all_session_data = []

    for folder in os.listdir(v.get_string('DATA_PATH')):
        path = v.get_string('DATA_PATH') + folder + v.get_string('SESSION_FOLDER')        
        session_type = folder.split("-")[1]
        
        try:
            for file in os.listdir(path):
                file_path = path + "/" + file
                print(file_path)
                user_id = file.split(".")[0].split("-")
                user_id = user_id[1] + "-" + user_id[2]
                with open(file_path) as f:                
                    session_data = json.load(f)
                    for data in session_data:
                        data['session_type'] = session_type
                        data['user_id'] = user_id
                    all_session_data += session_data
        except FileNotFoundError:
            print("NO EXISTE SESION " + v.get_string('SESSION_FOLDER') + " PARA EL USUARIO " + folder.split("-")[0])
  

    users_df = pd.DataFrame(all_session_data)

    filepath = Path(v.get_string('CSV_PATH') + v.get_string('CSV_NAME'))
    users_df.to_csv(filepath, index=False)

if __name__ == '__main__':
    main()
