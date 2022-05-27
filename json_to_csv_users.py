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
    users = []

    for file in os.listdir(v.get_string('DATA_PATH')):
        path = v.get_string('DATA_PATH') + file
        with open(path) as f:
            user =json.load(f)
            users.append(user)

    users_df = pd.DataFrame(users)

    filepath = Path(v.get_string('CSV_PATH') + v.get_string('CSV_NAME'))
    users_df.to_csv(filepath, index=False)

if __name__ == '__main__':
    main()
