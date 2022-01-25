#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlalchemy


# In[3]:


# создаем engine
engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/postgres')
engine


# In[4]:


# установим соединение
connection = engine.connect()


# SELECT

# In[5]:


# выберем все поля из таблицы film
sel = connection.execute("""
SELECT * FROM film;
""").fetchone()
print(sel)


# In[6]:


print(type(sel))


# In[7]:


# выберем столбец title таблицы film
print(connection.execute("""SELECT title FROM film;
""").fetchmany(10))


# In[8]:


# выберем 2 столбца из таблицы film
print(connection.execute("""SELECT title, release_year FROM film;
""").fetchmany(10))


# In[11]:


# Практика. Напишите запрос, который отберет имена и фамилии актеров из соотвествующей таблицы
print(connection.execute("""SELECT first_name, last_name from actor;
""").fetchmany(10))


# In[12]:


# как работает DISTINCT
# выведем столбец rating из film
res = connection.execute("""SELECT rating FROM film;
""").fetchmany(10)
print(res)


# In[13]:


# найдем, какие рейтинги бывают
print(connection.execute("""SELECT DISTINCT rating FROM film;
""").fetchall())


# Примеры с арифметикой

# In[14]:


# переведем цены в условные рубли
connection.execute("""SELECT amount * 77 FROM payment;
""").fetchmany(10)


# In[15]:


# узнаем время аренды по позициям
connection.execute("""SELECT return_date - rental_date FROM rental;
""").fetchmany(10)


# WHERE

# In[16]:


# найдем фильмы, вышедшие после 2000
print(connection.execute("""SELECT title, release_year FROM film
WHERE release_year >= 2000;
""").fetchall())


# In[17]:


# найдем сотрудников, которые сейчас работают
print(connection.execute("""SELECT first_name, last_name, active FROM staff
WHERE active = true;
""").fetchmany(10))


# In[19]:


# критерий не обязательно должен входить в выборку
print(connection.execute("""SELECT first_name, last_name FROM staff
WHERE active = true;
""").fetchmany(10))


# In[21]:


# Практика. найдем ID, имена, фамилии актеров, которых зовут Joe
print(connection.execute("""SELECT actor_id, first_name, last_name FROM actor WHERE first_name = 'Joe'
""").fetchmany(10))


# In[22]:


# найдем всех сотрудников, которые работают не во втором магазине
connection.execute("""SELECT first_name, last_name FROM staff
WHERE store_id != 2;
""").fetchmany(10)


# In[23]:


# найдем только работающих сотрудников из всех магазинов, кроме 1
connection.execute("""SELECT first_name, last_name FROM staff
WHERE active = true AND NOT store_id = 1;
""").fetchmany(10)


# In[24]:


# найдем фильмы, цена проката которых меньше 0.99, а цена возмещения меньше 9.99
connection.execute("""SELECT title, rental_rate, replacement_cost FROM film
WHERE rental_rate <= 0.99 AND replacement_cost <= 9.99;
""").fetchmany(10)


# In[25]:


# найдем фильмы аналогичные предыдущему примеру или продолжительностью меньше 30 минут
connection.execute("""SELECT title, length, rental_rate, replacement_cost FROM film
WHERE length <= 30 OR rental_rate <= 0.99 AND replacement_cost <= 9.99;
""").fetchmany(10)


# IN / NOT IN

# In[26]:


# найдем фильмы с рейтингом R, NC-17
connection.execute("""SELECT title, description, rating FROM film
WHERE rating IN ('R', 'NC-17');
""").fetchmany(10)


# In[27]:


# найдем недетские фильмы
connection.execute("""SELECT title, description, rating FROM film
WHERE rating NOT IN ('G', 'PG');
""").fetchmany(10)


# BETWEEN

# In[28]:


connection.execute("""SELECT title, rental_rate FROM film
WHERE rental_rate BETWEEN 0.99 AND 3;
""").fetchall()


# LIKE

# In[34]:


# Найдем фильм, в описании которого есть Scientist
connection.execute("""SELECT title, description FROM film
WHERE description LIKE '%%Scientist%%';
""").fetchall()


# In[35]:


# Практика. найдем ID, имена, фамилии актеров, фамилия которых содержит gen
connection.execute("""SELECT first_name, last_name FROM actor WHERE last_name LIKE '%%gen%%';
""").fetchall()


# ORDER BY

# In[36]:


# Отсортируем фильмы по цене проката
connection.execute("""SELECT title, rental_rate FROM film
ORDER BY rental_rate;
""").fetchall()


# In[37]:


# по убыванию
connection.execute("""SELECT title, rental_rate FROM film
ORDER BY rental_rate DESC;
""").fetchall()


# In[38]:


# сортируем по нескольким столбцам: продолжительности и цене проката
connection.execute("""SELECT title, length, rental_rate FROM film
ORDER BY length DESC, rental_rate DESC;
""").fetchall()


# In[39]:


# найдем ID, имена, фамилии актеров, чья фамилия содержит LI, отсортируем в алфавитном порядке по фамилии, затем по имени
connection.execute("""SELECT actor_id, first_name, last_name FROM actor 
WHERE last_name LIKE '%%li%%' 
ORDER BY last_name, first_name;
""").fetchmany(10)


# LIMIT

# In[41]:


# Выведем первые 15 записей
connection.execute("""SELECT film_id, title, length, rental_rate FROM film
WHERE rental_rate > 2.99
ORDER BY length DESC, rental_rate
LIMIT 15;
""").fetchall()


# INSERT/DELETE/UPDATE

# In[42]:


#  insert delete update
connection.execute("""SELECT * FROM rental;
""").fetchmany(10)


# In[43]:


# INSERT. добавим новый прокат
connection.execute("""INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id) 
           VALUES(NOW(), 1, 3, 2);
""")


# In[45]:


# пример с нарушением внешнего ключа
# connection.execute("""INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id) 
#            VALUES(NOW(), 1, 3, 3);
# """)


# In[44]:


# проверим
connection.execute("""SELECT * FROM rental
WHERE staff_id = 2 and inventory_id = 1;
""").fetchall()


# In[46]:


# UPDATE. добавим возврат из проката
connection.execute("""UPDATE rental
           SET return_date = NOW()
           WHERE rental_id = 16058;
""")


# In[47]:


# проверим
connection.execute("""SELECT * FROM rental
WHERE staff_id = 2 and inventory_id = 1;
""").fetchall()


# In[ ]:


# insert можно кобминировать с Select, чтобы копировать данные из одной таблицы в другую
# INSERT INTO table2
# SELECT * FROM table1
# WHERE condition;


# In[48]:


# DELETE
connection.execute("""DELETE FROM rental
           WHERE rental_id = 16058
""")


# In[49]:


# проверим
connection.execute("""SELECT * FROM rental
WHERE rental_id = 16058;
""").fetchall()


# In[55]:


res = connection.execute("""SELECT * FROM film
ORDER BY length DESC, rental_rate DESC;
""").fetchall()
import pandas as pd
pd.DataFrame(res)


# In[ ]:





# In[ ]:




