create  database db;

create table customers(
    id integer unique ,
    full_name varchar(50) not null ,
    timestamp timestamp not null ,
    delivery_address text not null ,
    PRIMARY KEY (id)
);


create table orders(
    code integer unique not null ,
    customer_id integer,
    total_sum double precision not null check ( total_sum>0 ),
    is_paid boolean not null ,
    PRIMARY KEY(code),
    foreign key (customer_id) references customers(id)
);
create table products(
    id varchar(25) unique  not null ,
    name varchar(30)  unique not null ,
    description text,
    price double precision not null  check(price>0),
    primary key(id)
);
create table order_items(
    order_code integer unique not null ,
    product_id varchar(25) unique not null ,
    quantity integer not null check ( quantity>0 ),
    primary key(order_code,product_id),
    foreign key (order_code) references orders(code),
    foreign key (product_id) references products(id)
);
insert into customers values (4,'Beks','2019-03-01 00:00:01-06','Ganushkino');
insert into customers values (6,'Ayalan','2016-02-01 00:00:01-06','Almata');
insert into customers values (7,'Juan','2016-02-01 00:00:03-06','ALmata');

insert into customers values (1,'Mike','2021-03-01 00:00:01-06','New York');
insert into customers values (2,'July','2020-03-01 00:00:01-06','Tokyo');
insert into customers values (3,'Ayalan','2018-03-01 00:00:01-06','Atyrau');


DELETE  from customers where full_name='Beks';

UPDATE Customers
SET full_name = 'Beks', delivery_address= 'Atyrau'
WHERE id = 5;

DELETE FROM Customers WHERE full_name='Ayalan';

UPDATE Customers
SET full_name='Juan'
WHERE delivery_address='Almata';


select *from customers;
