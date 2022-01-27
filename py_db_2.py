#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlalchemy


# In[2]:


# создаем engine
engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/postgres')
engine


# In[3]:


con = engine.connect()


# Агрегирующие функции

# In[4]:


# найдем максимальную стоимость проката
con.execute("""
SELECT MAX(rental_rate) FROM film
""").fetchall()


# In[5]:


# посчитаем среднюю продолжительность фильма
con.execute("""
SELECT AVG(length) FROM film
""").fetchall()


# In[6]:


# сколько уникальных имен актеров?
con.execute("""
SELECT COUNT(DISTINCT first_name) FROM actor
""").fetchall()


# In[7]:


# посчитаем сумму и средние продажи по конкретному продавцу
con.execute("""
SELECT SUM(amount), AVG(amount) FROM payment
WHERE staff_id = 1;
""").fetchall()


# In[ ]:





# Вложенные запросы

# In[8]:


# найдем все фильмы с продолжительностью ваше среднего

# так работать не будет
con.execute("""
SELECT title, length  FROM film
WHERE length >= AVG(length)
""").fetchall()


# In[9]:


con.execute("""
SELECT title, length FROM film
WHERE length >= (
    SELECT AVG(length) FROM film);
""").fetchmany(10)


# In[10]:


# найдем названия фильмов, стоимость проката которых не максимальная
con.execute("""SELECT title, rental_rate FROM film
WHERE rental_rate < (SELECT MAX(rental_rate) FROM film)
ORDER BY rental_rate DESC;
""").fetchall()


# Группировки

# In[12]:


# посчитаем количество актеров в разрезе фамилий (найдем однофамильцев)
con.execute("""
SELECT last_name, COUNT(*) FROM actor
GROUP BY last_name
ORDER BY COUNT(*) DESC;
""").fetchmany(10)


# In[14]:


# посчитаем количество фильмов в разрезе рейтингов (распределение рейтингов)
con.execute("""
SELECT rating, COUNT(title) FROM film
GROUP BY rating
ORDER BY COUNT(title) DESC;
""").fetchall()


# In[15]:


# найдем максимальные продажи в разрезе продавцов
con.execute("""
SELECT staff_id, MAX(amount) FROM payment
GROUP BY staff_id;
""").fetchall()


# In[24]:


# найдем средние продажи каждого продавца каждому покупателю
con.execute("""
SELECT staff_id, customer_id, AVG(amount) FROM payment
GROUP BY staff_id, customer_id
ORDER BY AVG(amount) DESC;
""").fetchall()


# In[25]:


# найдем среднюю продолжительность фильма в разрезе рейтингов в 2006 году
con.execute("""
SELECT rating, AVG(length) FROM film
WHERE release_year = 2006
GROUP BY rating;
""").fetchall()


# Оператор HAVING

# In[27]:


# отберем только фамилий актеров, которые не повторяются
con.execute("""
SELECT last_name, COUNT(*) FROM actor
GROUP BY last_name
HAVING COUNT(*) = 1;
""").fetchall()


# In[29]:


# отберем и посчитаем только фамилии актеров, которые повторяются
con.execute("""
SELECT last_name, COUNT(*) FROM actor
GROUP BY last_name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;
""").fetchall()


# In[30]:


# найдем фильмы, у которых есть SUPER в названии и они сдавались в прокат суммарно более, чем на 5 дней
con.execute("""
SELECT title, SUM(rental_duration) FROM film
WHERE title LIKE '%%Super%%'
GROUP BY title
HAVING SUM(rental_duration) > 5;
""").fetchall()


# ALIAS

# In[33]:


# Предыдущий запрос с псевдонимами
con.execute("""
SELECT title t, SUM(rental_duration) sum_t FROM film f
WHERE title LIKE '%%Super%%'
GROUP BY t
HAVING SUM(rental_duration) > 5;
""").fetchall()


# Объединение таблиц

# In[34]:


# выведем имена, фамилии и адреса всех сотрудников
con.execute("""
SELECT first_name, last_name, address FROM staff s
LEFT JOIN address a ON s.address_id = a.address_id;
""").fetchall()


# In[35]:


# определим количество продаж каждого продавца
con.execute("""
SELECT s.last_name, COUNT(amount) FROM payment p
LEFT JOIN staff s ON p.staff_id = s.staff_id
GROUP BY s.last_name;
""").fetchall()


# In[36]:


# посчитаем, сколько актеров играло в каждом фильме
con.execute("""
SELECT title, COUNT(actor_id) actor_q FROM film f
JOIN film_actor a ON f.film_id = a.film_id
GROUP BY f.title
ORDER BY actor_q DESC;
""").fetchall()


# In[ ]:





# In[ ]:





# In[38]:


# сколько копии фильмов со словом SUPER в названии есть в наличии
con.execute("""
SELECT title, COUNT(inventory_id) FROM film f
JOIN inventory i ON f.film_id = i.film_id
WHERE title LIKE '%%Super%%'
GROUP BY title;
""").fetchall()


# In[39]:


# выведем список покупателей с количеством их покупок в порядке убывания
con.execute("""
SELECT c.last_name ls, COUNT(p.amount) amount FROM customer c
LEFT JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.last_name
ORDER BY amount DESC;
""").fetchall()


# In[40]:


# выведем имена и почтовые адреса всех покупателей из России
con.execute("""
SELECT c.last_name, c.first_name, c.email FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ON a.city_id = city.city_id
JOIN country co ON city.country_id = co.country_id
WHERE country = 'Russian Federation';
""").fetchall()


# In[41]:


# фильмы, которые берут в прокат чаще всего
con.execute("""
SELECT f.title, COUNT(r.inventory_id) count FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY count DESC;
""").fetchall()


# In[42]:


# суммарные доходы магазинов
con.execute("""
SELECT s.store_id, SUM(p.amount) sales FROM store s 
JOIN staff st ON s.store_id = st.store_id
JOIN payment p ON st.staff_id = p.staff_id
GROUP BY s.store_id;
""").fetchall()


# In[43]:


# найдем города и страны каждого магазина
con.execute("""
SELECT store_id, city, country FROM store s 
JOIN address a ON s.address_id = a.address_id
JOIN city ON a.city_id = city.city_id
JOIN country c ON city.country_id = c.country_id;
""").fetchall()


# In[44]:


# выведем топ-5 жанров по доходу
con.execute("""
SELECT c.name, SUM(p.amount) revenue FROM category c 
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY revenue DESC 
LIMIT 5;
""").fetchall()


# In[ ]:





# In[ ]:





# In[ ]:




