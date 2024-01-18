import yaml

def get_data():
    with open("config.yaml", "r") as stream:
        try: 
            data = yaml.safe_load(stream)["database"]
            username = data["username"]
            password = data["password"]
            dbname = data["db_name"]
        except yaml.YAMLError as exc:
            print(exc)
    return username, password, dbname

print(get_data())