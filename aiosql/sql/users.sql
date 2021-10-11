
-- name: add_user!
-- Insert a user into the database
insert into users(username, firstname, lastname) values (:username, :firstname, :lastname);

-- name: add_user2<!
-- Insert a user into the database
insert into users(username, firstname, lastname) values (:username, :firstname, :lastname);

-- name: remove_user!
-- Remove a remove from the database
delete from users where userid = :userid;

-- name: get_user_count$
-- Counts number of users in the database
select count(*) from users;

--name: get_users
select * from users;
