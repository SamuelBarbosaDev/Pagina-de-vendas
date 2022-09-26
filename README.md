<h1>Pagina De Vendas Django</h1>
<h3>Objetivo:</h3>
    <p>
    Criar uma página de vendas focando no siglepage aplications (SPA), onde contenha em uma única página todo o conteúdo do site, 
    com o intuito que depois do primeiro carregamento do site nenhuma outra requisição precise ser feita 
    por parte do servidor.
        Meu objetivo técnico na criação desse site é criar uma api restfull, que irá fazer o meio de campo entre 
        o back-end feito utilizando o django, e front-end onde usaremos o angular material, meu público alvo, 
        são os vendedores de curso da hotmart e outras plataformas.</p>
    
- As Vantagens do siglepage aplications (SPA) são:
    - Uma das maiores vantagens, que engloba as outras, é a renderização ser no lado do cliente.
    - Há melhor experiência geral para o usuário, principalmente a latência até a renderização final é extremamente reduzida.
    - Há redução de tráfego até o servidor e isso obviamente é ótimo.


<h3>Regra de negócios:</h3>
    <p>
        Meu cliente deve conseguir alterar textos, imagens, redes socias e alguns objetos, por outro lado, ele não poderá mudar o layout do site.
    <p>
<h3>Como Funciona:</h3>
    <p>
        Para rodando o projeto localmente, você precisara realizar os seguintes passos:
    </p>
    
   * Crie um ambiente virtual dentro da pasta /Meu-Portfolio `python3 -m venv venv`
   * Acesse a pasta /apps `cd apps/`
   * Execute o comando `pip install -r requirements.txt` para instalar as dependências
   * Execute o comando `python manage.py migrate` para gerar o banco de dados sqlite3
   * Execute o comando `python manage.py createsuperuser` e informe usuário e senha para criar um administrador
   * Acesse a pasta /apps/apps `cd apps/apps` e crie um arquivo .env
   * Dentro arquivo .env defina `DEBUG=True` e configure a SECRET_KEY `SECRET_KEY='COLOQUE_AQUI_SUA_SECRET_KEY'`.
   * Execute o comando `python manage.py runserver` para inicar o projeto
   * Acesse o endereço `localhost:8000` para ver o projeto rodando.
   * Acesse o endereço `localhost:8000/samueloficial@protonmail.com` para fazer as configurações no site.
   

<h3> O que aprendi:</h3>
    <p>
    </p>

<h3>Tecnologias utilizadas:</h3>

  - Linguagens:
    - python==3.10.4
    - typescript
  
  - Libs:
    - asgiref==3.5.2
    - autopep8==1.7.0
    - dj-database-url==1.0.0
    - Django==4.1
    - django-crispy-forms==1.14.0
    - django-filter==22.1
    - django-on-heroku==1.1.2
    - gunicorn==20.1.0
    - Pillow==9.2.0
    - psycopg2-binary==2.9.3
    - pycodestyle==2.9.1
    - python-decouple==3.6
    - sqlparse==0.4.2
    - toml==0.10.2  
    - whitenoise==6.2.0
  - Framework:
    - Django==4.1
    - Angular
