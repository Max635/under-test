## Licenses Emailing App

Front-end
- license_emailing

Back-end
- license_emailing_api (Django app)
- emailManager (Script de Python)



### Instalação
```sh
$ pip install -r requirements.txt

```
emailer.py
PASSWORD_EMAIL = 'license.test'
SENDER_EMAIL = 'license.emailing@gmail.com'
VENDAS_EMAIL = ''

init_emailing()
response = _get_data_from_api('2021-06-10')

updater.py
start()
scheduler.add_job(emailer.init_emailing, 'cron', hour='8')

http://0.0.0.0:8080/api-docs/

http://0.0.0.0:8080/licenses/

http://0.0.0.0:8080/due-date/
http://0.0.0.0:8080/due-date/?search=2021-06-10
