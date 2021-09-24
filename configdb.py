import psycopg2


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

create a table or check if it already exists, get error (psycopg2.errors.DuplicateTable: relation "nonsense" already exists)
try:
    create_table_query = '''CREATE TABLE recipes
            (ID INT PRIMARY KEY,
            TITLE           TEXT,
            DESCRIPTION         TEXT); '''
    cursor.execute(create_table_query)

    create_table_query = '''CREATE TABLE recipe_ingredients
            (RECIPE_ID           TEXT,
            INGREDIENT_ID         TEXT); '''
    cursor.execute(create_table_query)

    create_table_query = '''CREATE TABLE ingredients
            (INGREDIENT_ID           TEXT,
            NAME         TEXT); '''
    cursor.execute(create_table_query)

    create_table_query = '''CREATE TABLE recipe_steps
            (STEP_NUM           INT,
            RECIPE_ID           TEXT,
            INSTRUCTION         TEXT); '''
    cursor.execute(create_table_query)

    connection.commit()
    print("Table created successfully in PostgreSQL ")

    # maybe check that the table is empty or not? If empty then import
except:
    print("failed to create table nonsense")
