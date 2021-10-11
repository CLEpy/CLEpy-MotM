
-- name: bulk_publish*!
-- Insert many blogs at once
insert into blogs (userid, title, content, published)
values (:userid, :title, :content, :published);

-- name: publish_blog!
-- Insert a blog into the database
insert into blogs(userid, title, content) values (:userid, :title, :content);

-- name: publish_blog2<!
-- Insert a blog into the database and return id of blog 
insert into blogs(userid, title, content) values (:userid, :title, :content);

-- name: remove_blog!
-- Remove a blog from the database
delete from blogs where blogid = :blogid;

-- name: get_blog_count$
-- Counts number of blogs in the database
select count(*) from blogs;

--name: get_blogs
select * from blogs;
