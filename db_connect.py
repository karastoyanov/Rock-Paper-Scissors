import psycopg2, sshtunnel
from decouple import config



def database_connect():
    LINUX_USERNAME = config('LINUX_USERNAME')
    LINUX_PASSWORD = config('LINUX_PASSWORD')

    DB_USERNAME = config('DB_USERNAME')
    DB_PASSWORD = config('DB_PASSWORD')

    tunnel = sshtunnel.SSHTunnelForwarder(
            ('139.144.178.197', 22),
            ssh_username = str(LINUX_USERNAME),
            ssh_password = str(LINUX_PASSWORD),
            remote_bind_address = ('127.0.0.1', 5432)
            )
    tunnel.start()

    db_client = psycopg2.connect(
            user = str(DB_USERNAME),
            password = str(DB_PASSWORD),
            host = '139.144.178.197',
            port = '5432',
            dbname = 'rps'
            )
    cursor = db_client.cursor()


database_connect()
