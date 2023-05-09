import psycopg2, sshtunnel
from decouple import config

POSTGRES_CURSOR = ''
POSTGRES_CONNECTION = ''

USER_POSTGRES_CURSOR = ''
USER_POSTGRES_CONNECTION = ''

# Connect with Admin(Used for New Accounts Registration)
def database_connect():

    global POSTGRES_CURSOR
    global POSTGRES_CONNECTION

    LINUX_USERNAME = config('LINUX_USERNAME')
    LINUX_PASSWORD = config('LINUX_PASSWORD')
    LINUX_ADDRESS = config('LINUX_IP_ADDRESS')

    DB_USERNAME = config('DB_USERNAME')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_NAME = config('DB_NAME')
    DB_PORT = config('DB_PORT')

    tunnel = sshtunnel.SSHTunnelForwarder(
            (str(LINUX_ADDRESS), 22),
            ssh_username = str(LINUX_USERNAME),
            ssh_password = str(LINUX_PASSWORD),
            remote_bind_address = ('127.0.0.1', 5432)
            )
    tunnel.start()

    db_client = psycopg2.connect(
            user = str(DB_USERNAME),
            password = str(DB_PASSWORD),
            host = str(LINUX_ADDRESS),
            port = DB_PORT,
            dbname = str(DB_NAME)
            )
    cursor = db_client.cursor()

    POSTGRES_CURSOR = cursor
    POSTGRES_CONNECTION = db_client



# Connect with Player
def user_connect(user_name, user_passwd):
    
    global USER_POSTGRES_CURSOR
    global USER_POSTGRES_CONNECTION
    
    LINUX_USERNAME = config('LINUX_USERNAME')
    LINUX_PASSWORD = config('LINUX_PASSWORD')
    LINUX_ADDRESS = config('LINUX_IP_ADDRESS')
    

    DB_USERNAME = user_name + "_rpsuser"
    DB_PASSWORD = user_passwd
    DB_NAME = config('DB_NAME')
    DB_PORT = config('DB_PORT')

    tunnel = sshtunnel.SSHTunnelForwarder(
            (str(LINUX_ADDRESS), 22),
            ssh_username = str(LINUX_USERNAME),
            ssh_password = str(LINUX_PASSWORD),
            remote_bind_address = ('127.0.0.1', 5432)
            )
    tunnel.start()

    db_client = psycopg2.connect(
            user = str(DB_USERNAME),
            password = str(DB_PASSWORD),
            host = str(LINUX_ADDRESS),
            port = DB_PORT,
            dbname = str(DB_NAME)
            )
    cursor = db_client.cursor()

    USER_POSTGRES_CURSOR = cursor
    USER_POSTGRES_CONNECTION = db_client

#database_connect()
