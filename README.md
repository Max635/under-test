## Licenses Emailing App

O projeto __"Licenses Emailing"__ visa disponibilizar uma ferramenta automâtica de notificações, por meio de email, dos vencimentos das licenças adquiridas pelos clientes.
Diariamente é feita uma requisição ao endpoint, consultando pelas licenças com a data atual de vencimento. Caso existirem, o sistema as informara ao time de vendas. Apenas um email por usuario sera enviado, contendo as informações da(s) licença(s) vencida(s).

O serviço oferece uma interface para adicionar licenças. Além de ingressar os dados nome e email do cliente, também deverá ser indicado o nome do pacote e o tipo de licenciamento.
Dependendo da licença escolhida; quadrimensal, mensal ou semanal, será feito o calculo do tempo de vencimento. A contagem do prazo e feita a partir da carga da licença. Baseados nesses dados;

1. __Quadrimensal__ = _data de carga + 4 meses_
2. __Mensal__ = _data de carga + 1 mês_
3. __Semanal__ = _data de carga + 1 semana_

Uma vez atingido o período de uso, o sistema informará ao endereço de correo eletrônico configurado.

-----

### Configurações iniciais

O arquivo __config.py__ ubicado em __/license_emailing_api/emailManager/__ contêm as principais configurações.
Atualmente o sistema utiliza uma conta de Gmail exclusiva para o envio dos emails.
As configurações,


- PASSWORD_EMAIL = 'license.test'
- SENDER_EMAIL = 'license.emailing@gmail.com'
- VENDAS_EMAIL = ''

A constante __VENDAS_EMAIL__ deberá ser configurada com o endereço de recebimento desejado para o recebimento dos correios eletrônicos.

## Execução programada da consulta

A pasta __emailerManager__ contém os arquivos para a execução automatizada da extração e envio dos correios eletrônicos. Diariamente é executada uma consulta ao endpoint solicitando as datas de vencimiento do dia. Na configuração atual, a consulta é feita às oito horas.

- __emailerManager__
    - _config.py_
    - _emailer.py_
    - _updater.py_

O script de Python __updater.py__ contém a configuração do parámetro horário.
Caso seja necessário mudar o horario de consulta é preciso alterar na seguinte linha o valor de __hour__:

- scheduler.add_job(emailer.init_emailing, 'cron', hour='__8__')

## Alteração de data de consulta para teste

__emailer.py__ contém as configurações para o envio dos emails. A data atual para consulta é obtida por meio da execução do método __date.today()__
Para testar com otra data de vencimento é preciso alterar o valor da variável __today__ para uma data específica (formato 'yyyy-mm-dd')

- > linha 111:  __today__ = date.today()

Para consultar o endpoint com data '2021-06-15':

__today__ = '2021-06-15'

Feitas as alterações o sistema consultará pela data inserida manualmente e, caso tiver vencimentos, será gerado o email com o relatório dos mesmos.

## Cálculo dos prazos de vencimento

Baseado no Tipo de Licença escolhida, o sistema calculará o período de vigência das licenças.
As configurações encontram-se no arquivo __models.py__ do aplicativo.
Como mencionado anteriormente, o início do período é obtido assim que é gerado uma nova licença.
Definições para o cálculo dos prazos possuen o formato da seguinte expresão:

- __self.license_due_date = self.license_init_date + relativedelta(months=+4)__

- license_due_date = _data de vencimento da licença_
- license_init_date = _data de início do período da licença_

- relativedelta(months=+4) _para tipo de licença Quadrimensal._
- relativedelta(months=+1) _para tipo de licença mensal._
- relativedelta(weeks=1) _para tipo de licença semanal._

-----

### Requisitos do sistema

O arquivo requirements.txt contêm os frameworks, livrarias e pacotes necessários para a executar o sistema. Foi utilizado, entre outros, os seguientes:

- Django,
- Django Rest Framework,
- Django filter,
- Swagger,
- Postgresql,
- Psycopg2

Caso não seja utilizada a imagem do Docker disponibilizada, os pacotes deverão ser instalados com o seguinte comando:

```sh
$ pip install -r requirements.txt
```

### Estrutura

Criou-se um repositório Git contendo arquivos e configurações necessarias para rodar o aplicativo desde zero.
O aplicativo pode ser executado desde uma imagem conteinerizada Docker ou utilizando a estrutura de pastas e arquivos do Django.
As pastas principais,

__Front-end__
- license_emailing (_Django project_)

__Back-end__
- license_emailing_api (_Django app_)
- license_emailing_api/emailManager (_Lógica para o envio de emails_)


### Endereços e endpoints

- http://0.0.0.0:8080/license
- http://0.0.0.0:8080/admin
- http://0.0.0.0:8080/api-docs/
- http://0.0.0.0:8080/licenses/
- http://0.0.0.0:8080/due-date/


### Front-End

Por meio do seguinte endereço pode se agregar licenças no sistema:

- http://0.0.0.0:8080/license

De forma similar, por meio da interface do administrador fornecida pelo Django:

- http://0.0.0.0:8080/admin

Para acessar a documentação dos endpoints, foi configurado o seguinte endereço:

- http://0.0.0.0:8080/api-docs/


### Endpoints

Para acessar a listagem de usuarios e as suas licenças:

http://0.0.0.0:8080/licenses/

Existe um endpoint para realzar uma busca por data de vencimento de licença. Esse é utilizado de forma automâtica pela lógica de consulta de vencimentos. Também pode ser acessado manualmente em :

- http://0.0.0.0:8080/due-date/

Para indicar uma data de vencimento debe ser inserido o argumento __search=__ junto com a data com formato yyyy-mm-dd.
Para buscar as licenças com vencimento na data _2021-06-10_

- http://0.0.0.0:8080/due-date/?search=2021-06-10


### Banco de Dados

Para persistir os dados,o sistema utiliza Postgresql.
O arquivo __models.py__ contém a estrutura das tabelas e tipos de dados do banco.


### Execução do sistema por meio da imagem Docker

Os arquivos __Dockerfile__ e __docker-compose.yml__ contêm as configurações necessárias para a execução da sistema conteineirizada
Para iniciar a imagem de Docker:

```sh
$ docker-compose up
```
Após execução, o sistema ficará disponível em __http://0.0.0.0:8080/__

-----

## Requisitos

1. [x] Sitema desenvolvido utilizando __Python v3.x__
2. [x] __Framework Django__ e __Django Rest Framework__
3. [x] _O projeto pode ser iniciado com um único comando_, __docker-compose up__ 
4. [x] _O projeto em execução pode ser acessado no navegador em_ __[docker host]:8080__
5. [x] _O projeto deve ter o módulo administrador acessível em_ __[docker host]:8080/admin__
6. [x] Uso de __Swagger__ para documentação da API.

-----

<details>
  <summary> maxi635@hotmail.com </summary>
    Maximiliano Hugo Chaile
</details>
