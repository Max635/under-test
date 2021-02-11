""" Configurações """

URL_ENDPOINT = 'http://0.0.0.0:8080/due-date/'
CONTACT_LIST_CSV_FILE = 'contact_list.csv'

# Postgresql
PSQL_USR = 'postgres'
PSQL_PWD = 'admin'
PSQL_HOST = 'db'
PSQL_PORT = '5432'
PSQL_DB = 'licenses'

# Gmail account
SERVER = 'smtp.gmail.com:587'
PASSWORD_EMAIL = 'license.test'
SENDER_EMAIL = 'license.emailing@gmail.com'
VENDAS_EMAIL = ''
SUBJECT = 'Vencimento de Licenças'

# Mensagem do email em formato HTML
HTML_MSG = """
    <html>
        <body>
            <p>Bom dia time de vendas!</p>
            <p>As seguintes licenças têm vencem hoje.</p>
            <br/>
                {table}
            <br/>
            <p>Muito obrigado pela sua atenção.</p>
            <p>License Bot ;)</p>
        </body>
    </html>
    """
