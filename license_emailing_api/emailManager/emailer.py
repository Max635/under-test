""" Script to get data from API endpoint and send by Gmail account """
import csv
import smtplib
import sys
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from collections import OrderedDict
from tabulate import tabulate

import requests
import psycopg2

from .config import *


def _get_customer_data_from_csv():
    with open(CONTACT_LIST_CSV_FILE, 'r') as input_file:
        reader = csv.reader(input_file)
        return list(reader)


def _tabulate_html_text(html_msg):
    data = _get_customer_data_from_csv()
    html_message = html_msg.format(
        table=tabulate(data,
                       headers=['Nome do Cliente',
                                'Email',
                                'ID da Licença',
                                'Nome do Pacote',
                                'Tipo de Licença'],
                       tablefmt="html",
                       numalign="center",
                       colalign=("center",),
                       floatfmt=".6f")
    )
    return html_message


def _send_emails():
    """ Drive Gmail account to send emails """
    html_msg = _tabulate_html_text(HTML_MSG)

    message = MIMEMultipart("alternative", None, [MIMEText(html_msg, 'html')])
    message['Subject'] = SUBJECT
    message['From'] = SENDER_EMAIL
    message['To'] = VENDAS_EMAIL

    server = smtplib.SMTP(SERVER)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, PASSWORD_EMAIL)
    server.sendmail(SENDER_EMAIL, VENDAS_EMAIL, message.as_string())
    server.quit()

def _get_data_from_api(current_date):
    payload = {'search': current_date}
    response = requests.get(URL_ENDPOINT, params=payload)
    if response.headers['Content-Length'] == 2:
        sys.exit()
    return response.json()


def _extract_customer_email(response):
    email_list = []
    for data in response:
        email_list.append(data['email'])
    return list(OrderedDict.fromkeys(email_list))


def _execute_psql_copy(date_value, email_value):
    try:
        connection = psycopg2.connect(user=PSQL_USR,
                                      password=PSQL_PWD,
                                      host=PSQL_HOST,
                                      port=PSQL_PORT,
                                      database=PSQL_DB)

        cursor = connection.cursor()
        sql_copy = "COPY (SELECT customerlicense.name, \
                        customerlicense.email, \
                        customerlicense.license_code, \
                        customerlicense.package_name, \
                        customerlicense.license_type \
                        FROM customerlicense \
                        WHERE customerlicense.license_due_date = '{0}' \
                        AND customerlicense.email = '{1}') \
                        TO STDOUT WITH CSV DELIMITER ','".format(date_value, email_value)

        with open(CONTACT_LIST_CSV_FILE, 'w') as file_output:
            cursor.copy_expert(sql_copy, file_output)

    except(Exception, psycopg2.DatabaseError) as error:
        print('Error while connecting to PostgreSQL', error)

    finally:
        if connection:
            cursor.close()
            connection.close()


def _create_csv_and_sendmail(date_value, email_list):
    for email_value in email_list:
        _execute_psql_copy(date_value, email_value)
        _send_emails()


def init_emailing():
    """ Entry point function """
    today = date.today()
    response = _get_data_from_api(today)
    email_list = _extract_customer_email(response)
    _create_csv_and_sendmail(today, email_list)
