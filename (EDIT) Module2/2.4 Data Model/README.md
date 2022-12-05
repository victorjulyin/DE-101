# Data Model (SuperStore dataset) 
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/(EDIT)%20Module2/2.4%20Data%20Model/data_model.png"></p>


# Queries to create and fill tables

## CREATING TABLES:

category

	DROP TABLE IF EXISTS category cascade;
	
	CREATE TABLE category
	(
	category_id   int NOT NULL,
	category_name varchar(15) NOT NULL,
	CONSTRAINT PK_9 PRIMARY KEY ( category_id )
	);




sub_category
	DROP TABLE IF EXISTS sub_category cascade;
	
	CREATE TABLE sub_category
	(
	sub_category_id   int NOT NULL,
	category_id       int NOT NULL,
	sub_category_name varchar(15) NOT NULL,
	CONSTRAINT PK_8 PRIMARY KEY ( sub_category_id ),
	CONSTRAINT FK_4 FOREIGN KEY ( category_id ) REFERENCES category ( category_id )
	);
	
	CREATE INDEX FK_8 ON sub_category
	(
	category_id
	);




product
	DROP TABLE IF EXISTS product cascade;
	
	CREATE TABLE product
	(
	product_id      int NOT NULL,
	sub_category_id int NOT NULL,
	product_name    varchar(150) NOT NULL,
	CONSTRAINT PK_7 PRIMARY KEY ( product_id ),
	CONSTRAINT FK_5 FOREIGN KEY ( sub_category_id ) REFERENCES sub_category ( sub_category_id )
	);
	
	CREATE INDEX FK_7 ON product
	(
	sub_category_id
	);




region
	DROP TABLE IF EXISTS region cascade;
	
	CREATE TABLE region
	(
	region_id   int NOT NULL,
	region_name varchar(15) NOT NULL,
	person      varchar(20) NOT NULL,
	CONSTRAINT PK_5 PRIMARY KEY ( region_id )
	);




customer
	DROP TABLE IF EXISTS customer cascade;
	
	CREATE TABLE customer
	(
	customers_id   int NOT NULL,
	customer_name varchar(30) NOT NULL,
	segment       varchar(15) NOT NULL,
	country       varchar(15) NOT NULL,
	region_id     int NOT NULL,
	state         varchar(30) NOT NULL,
	city          varchar(20) NOT NULL,
	postal_code   int,
	CONSTRAINT PK_4 PRIMARY KEY ( customers_id ),
	CONSTRAINT FK_2 FOREIGN KEY ( region_id ) REFERENCES region ( region_id )
	);
	
	CREATE INDEX FK_1 ON customer
	(
	region_id
	);




date
	DROP TABLE IF EXISTS date cascade;
	
	CREATE TABLE "date"
	(
	date_id   int NOT NULL,
	year      int NOT NULL,
	full_date date NOT NULL,
	month     int NOT NULL,
	day       int NOT NULL,
	CONSTRAINT PK_1 PRIMARY KEY ( date_id )
	);




shipping
	DROP TABLE IF EXISTS shipping cascade;
	
	CREATE TABLE shipping
	(
	shipping_id   int NOT NULL,
	shipping_type varchar(15) NOT NULL,
	CONSTRAINT PK_2 PRIMARY KEY ( shipping_id )
	);




the_order
	DROP TABLE IF EXISTS the_order cascade;

	CREATE TABLE the_order
	(
	the_order_id int NOT NULL,
	date_id      int NOT NULL,
	product_id   int NOT NULL,
	ship_date    date NOT NULL,
	shipping_id  int NOT NULL,
	customers_id int NOT NULL,
	returned     varchar(3) NOT NULL,
	sales        decimal NOT NULL,
	profit       decimal NULL,
	discount     decimal NULL,
	quantity     int NULL,
	CONSTRAINT PK_3 PRIMARY KEY ( the_order_id ),
	CONSTRAINT FK_9 FOREIGN KEY ( product_id ) REFERENCES product ( product_id ),
	CONSTRAINT FK_1 FOREIGN KEY ( shipping_id ) REFERENCES shipping ( shipping_id ),
	CONSTRAINT FK_3 FOREIGN KEY ( customers_id ) REFERENCES customer ( customers_id ),
	CONSTRAINT FK_8 FOREIGN KEY ( date_id ) REFERENCES "date" ( date_id )
	);
	
	CREATE INDEX FK_10 ON the_order
	(
	product_id
	);
	
	CREATE INDEX FK_2 ON the_order
	(
	shipping_id
	);
	
	CREATE INDEX FK_3 ON the_order
	(
	customers_id
	);
	
	CREATE INDEX FK_4 ON the_order
	(
	date_id
	);



## FILLING TABLES:

--UPDATING date
    insert into date
    with e(e_year, e_date, e_month, e_day)
    AS
    (select extract('year' from order_date),
    order_date,
    extract('month' from order_date),
    extract('day' from order_date)
    from orders
    group by 1,2,3,4
    order by 2)

    select row_number() over(),
    e_year,
    e_date,
    e_month,
    e_day
    from e;





--UPDATING category
    insert into category
    select row_number() over(),
    category
    from (select distinct category
    from orders
    order by 1) as in_query
    ;





--UPDATING sub_category
    insert into sub_category
    select row_number() over(),
    one,
    two
    from(select category_id as one,
    subcategory as two
    from orders
    inner join category on orders.category = category.category_name
    group by 1,2
    order by 1,2) as in_query;





--UPDATING product
    insert into product
    select row_number() over(),
    one,
    two
    from(select sub_category_id as one,
    product_name as two
    from orders s
    inner join sub_category s_c on s.subcategory = s_c.sub_category_name
    group by 1, 2
    order by 1, 2) as in_query;





--UPDATING shipping
    insert into shipping
    select row_number() over(),
    one
    FROM
    (select distinct ship_mode as one
    from orders
    order by 1) as in_query;






--UPDATING region
    insert into region
    select row_number() over(),
    one,
    two
    FROM
    (select region as one, person as two
    from people left join orders USING(region)
    group by 1,2
    order by 1) as in_query;






--UPDATING customer
    insert into customer
    select row_number() over(), one, two, three, four, five, six, seven
    FROM
    (select customer_name as one,
    segment as two,
    country as three,
    region_id as four,
    state as five,
    city as six,
    postal_code as seven
    from orders o inner join region r on o.region = r.region_name
    group by 1,2,3,4,5,6,7
    order by 1) as in_query;






--UPDATING the_order
    insert into the_order
    select row_number() over(), one, two, three, four, five, six, seven, eight, nine, ten
    FROM
    (select date_id one,
    pr.product_id two,
    ship_date three,
    shipping_id four,
    cs.customers_id five,
    returned six,
    sales seven,
    profit eight,
    discount nine,
    quantity ten
    from returns ret
    inner join orders ord USING(order_id)
    inner join date dt on ord.order_date = dt.full_date
    inner join shipping sh on ord.ship_mode = sh.shipping_type
    inner join customer cs on ord.customer_name = cs.customer_name
    inner join product pr on ord.product_name = pr.product_name
    order by 1) as in_query;