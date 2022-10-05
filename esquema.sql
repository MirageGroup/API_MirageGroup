drop table if exists users;
    create table users(
        id integer primary key autoincrement,
        cpf varchar(15),
        email text not null,
        senha text not null
    );
