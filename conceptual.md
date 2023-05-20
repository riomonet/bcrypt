### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
It is a relational Database Managment system

- What is the difference between SQL and PostgreSQL?
SQL is a declarative programming language designed to interact
with Relational Databases. SQL can be use across many database managmeny systems
of which Postgresql is only one

- In `psql`, how do you connect to a database?
psql -d NameOfDatabase
or
\c NameOfDatabase

- What is the difference between `HAVING` and `WHERE`?
WHERE is a filter that modifies any SELECT statement. while HAVING  necessarily is
used after and in relation to a GROUPBY command.

- What is the difference between an `INNER` and `OUTER` join?
Inner join returns only the rows from two tables where the foreign keys align.

Outer Join will include all the rows from one of the tables and the matching rows
from the other table, an FULL OUTER JOIN will include all rows from two tables

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
left outer means include all the rows from the table referenced by the FROM
statement. RIGHT OUTER  includes all the rows from the table referenced by the  .JOIN statement.

- What is an ORM? What do they do?
	ORM stands for Object Relational Mapping and it's function is to build an Object oriented framework to interact with a relational database


- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  client side is async while request is syncronous
  client side is from the browser, requests happen in the server

- What is CSRF? What is the purpose of the CSRF token?
CSRF stands for Cross Sight Request Forgery. It is a method for hacking a database from outside
the system by hacking a form.  The CSRF token is a security measure that ensures the client submitting the form is a authorized and validated client.

- What is the purpose of `form.hidden_tag()`?
the purpose is to embed the CSRF token in the page. So when the form is submitted the token  will be submitted with the form. which allows for client form verification by the server
