import psycopg2, sshtunnel

def database_connect():
    LINUX_USERNAME = 'rps-user'
    LINUX_PASSWORD = 'rpsuser'

    DB_USER_NAME = 'rpsuser'
    DB_PASSWORD = 'Parola12345'

    tunnel = sshtunnel.SSHTunnelForwarder(
            ('139.144.178.197', 22),
            ssh_username = str(LINUX_USERNAME),
            ssh_password = str(LINUX_PASSWORD),
            remote_bind_address = ('127.0.0.1', 5432)
            )
    tunnel.start()

    db_client = psycopg2.connect(
            user = str(DB_USER_NAME),
            password = str(DB_PASSWORD),
            host = '139.144.178.197',
            port = '5432',
            dbname = 'rps'
            )
    cursor = db_client.cursor()


#database_connect()
