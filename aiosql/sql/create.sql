-- name: create_schema#
-- Create table schema of users and blog in db
create table users (
    userid integer primary key autoincrement,
    username text not null,
    firstname integer not null,
    lastname text not null
);

create table blogs (
    blogid integer primary key autoincrement,
    userid integer not null,
    title text not null,
    content text not null,
    published date not null default CURRENT_DATE,
    foreign key(userid) references users(userid)
);
