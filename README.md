At this point refer to this links to set up your database user as superuser

http://youtube.com/watch?v=lCNl3QKxgP0

after this run
> sudo -u postgres psql

Login in to db
> sudo -i -u postgres  
> psql -d topalatdb

> CREATE EXTENSION IF NOT EXISTS hstore; 

with the superuser privilege so that the hstore can work on the models requiring it.

This was implement in this commit message "On the database superuser created to allow hstore extension"