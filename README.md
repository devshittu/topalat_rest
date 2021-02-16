At this point refer to this links to set up your database user as superuser

http://youtube.com/watch?v=lCNl3QKxgP0

after this run
> sudo -u postgres psql \
> drop database topalatdb;\
> create database topalatdb; \
> GRANT ALL PRIVILEGES ON DATABASE topalatdb TO topalatdbuser; \
> exit;

Exit out of the postgre poweruser and login to the created db with below.
> sudo -i -u postgres  
> psql -d topalatdb

> CREATE EXTENSION IF NOT EXISTS hstore; \
> exit

with the superuser privilege so that the hstore can work on the models requiring it.

This was implement in this commit message "On the database superuser created to allow hstore extension"

> docker-compose build \
> docker-compose up \
> docker-compose up -d --build
> docker-compose up --build