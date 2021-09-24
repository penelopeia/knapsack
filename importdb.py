import psycopg2
import json
import os


# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI = 'postgres+psycopg2://kblau:pwd@localhost:5432/instructions'

user = "kblau"
host = "127.0.0.1"
port = "5432"
database = "knapsack"

# want to confirm connection and existance
try:
    print("test connection to PostGreSQL \nuser: {}, host: {}:{}, database: {}".format(user, host, port, database))
    connection = psycopg2.connect(user = "kblau",
                                  password = "pwd",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "knapsack")

    cursor = connection.cursor()
    print("Connection to PostGreSQL success")

except:
    print("Connection to PostGreSQL error")

this_dir = os.getcwd()
recipe_data = os.path.join(this_dir, r"\data")
print("Path to data: {}".format(recipe_data))
if os.path.exists(recipe_data):
    #grab data from local directory
    with open(os.path.join(recipe_data, "ex2.json")) as f:
        recipe = f.read()
        recipe_dict = json.load(recipe)

    # import data into the table
    try:
        # insert_data_query = '''INSERT INTO recipes (ID, TITLE, DESCRIPTION) VALUES ({id}, {title}, {description})'''.format(id = 1, title = "'recipe'", description = "'description'")
        insert_data_query = '''INSERT INTO recipes (ID, TITLE, DESCRIPTION) VALUES ({id}, {title}, {description})'''.format(id = 5, title = recipe_dict["title"], description = recipe_dict["description"])
        print(insert_data_query)
        cursor.execute(insert_data_query)
        connection.commit()
        print("data successfully inserted into table")
    except Exception as e:
        print("failed to push data into table, error {}".format(e))