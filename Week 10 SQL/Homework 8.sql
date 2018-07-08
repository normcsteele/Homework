use sakila;

select * from actor;

#1a. Display the first and last names of all actors from the table `actor`.

select actor.first_name, actor.last_name from actor;

#1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`. 

select concat(actor.first_name, " ", actor.last_name) as "Actor Name" from actor;

#2a. Find the ID#, first and last name of an actor, with the first name, "Joe." What is one query would you use to obtain this information?

select actor_id, first_name, last_name from actor where first_name = "Joe";
  	
#2b. Find all actors whose last name contain the letters `GEN`:

select first_name, last_name from actor where last_name like "%gen%";
  	
#2c. Find all actors whose last names contain `LI` and order rows by last name and first name, in that order:

select last_name, first_name from actor where last_name like "%li%";

#2d. Using `IN`, display `country_id` and `country` columns for the following: Afghanistan, Bangladesh, and China:

select country_id, country from country where country in ('Afghanistan', 'Bangladesh', 'China');

#3a. Add `middle_name` column to table `actor`. Position between `first_name` & `last_name`. (specify data type)

alter table actor
add column middle_name varchar(50) not null;

select first_name, middle_name, last_name from actor;
  	
#3b. Some of these actors have tremendously long last names. Change data type of the `middle_name` column to `blobs`.

alter table actor
modify column middle_name blob;

#3c. Now delete the `middle_name` column.

alter table actor
drop column middle_name;

#4a. List the last names of actors, as well as how many actors have that last name.

select actor.last_name, count(actor.last_name)
from actor
group by last_name;
	
#4b. List last names of & # of actors who have that last name, but only for names that are shared by at least two actors

select actor.last_name, count(actor.last_name) as 'Number of Occurances'
from actor
group by last_name
having count(last_name) > 1;

#4c. `HARPO WILLIAMS` was accidentally entered in `actor` as `GROUCHO WILLIAMS`. Write a query to fix the record.

update actor
set first_name = 'HARPO'
where first_name = "GROUCHO" and last_name = 'WILLIAMS';

#4d. In a single query, if first name of actor is currently `HARPO`, change it to `GROUCHO`. 
# Otherwise, change first name to `MUCHO GROUCHO`. DO NOT CHANGE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`. 
#(Hint: update the record using a unique identifier.)

update actor
set first_name = 'GROUCHO'
where first_name = 'HARPO' and last_name = 'WILLIAMS';

update actor
set first_name = "MUCHO GROUCHO"
where first_name = "GROUCHO" and not last_name = 'WILLIAMS';

#5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?

show create table address;

select * from address;
select * from staff;

#6a. Use `JOIN` to display first and last names and address of each staff member. Use the tables `staff` and `address`:

select staff.first_name, staff.last_name, address.address
from staff
join address
using (address_id);

# 6b. Use `JOIN` to display total amount rung up by each staff member in August 2005. Use tables `staff` and `payment`. 

select staff.staff_id, staff.first_name, staff.last_name, sum(payment.amount) 
from staff
join payment
using (staff_id)
where payment_date > '2005-7-31' and payment_date < '2005-9-1'
group by staff_id;



#6c. List each film and # of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.

select title, count(actor_id)
from film
inner join film_actor
using (film_id)
group by title;
  	
# 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?

select count(*) from inventory
where film_id
in (
	select film_id from film
    where title = "Hunchback Impossible"
);

# 6e. Using `payment`, `customer` & `JOIN` command, list total paid by each customer & customers alphabetically by last name:

  ```
  	![Total amount paid](Images/total_payment.png)
  ```

* 
7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. 
Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English. 

* 
7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
   
* 
7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. 
Use joins to retrieve this information.

* 
7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
Identify all movies categorized as famiy films.

* 
7e. Display the most frequently rented movies in descending order.
  	
* 
7f. Write a query to display how much business, in dollars, each store brought in.

* 
7g. Write a query to display for each store its store ID, city, and country.
  	
* 
7h. List the top five genres in gross revenue in descending order. 
(**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
  	
* 
8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
  
8b. How would you display the view that you created in 8a?

* 8c. You find that you no longer need the view `top_five_genres`. 
Write a query to delete it.

