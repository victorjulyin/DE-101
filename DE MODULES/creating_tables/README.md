# SQL-queries to create tables
### A map

1) [Table "region"](#Region)
2) [Table "customer"](#Customer)
3) [Table "category"](#Category)
4) [Table "sub_category"](#sub_category)
5) [Table "product"](#product)
6) [Table "shipping"](#shipping)
7) [Table "date"](#date)
8) [Table "the_order"](#the_order)



### Region

    CREATE TABLE "region"
    (
     "region_id"   int NOT NULL,
     "region_name" varchar(15) NOT NULL,
     "person"      varchar(20) NOT NULL,
     CONSTRAINT "PK_5" PRIMARY KEY ( "region_id" )
    );


### Customer

    CREATE TABLE "customer"
    (
     "customers_id"  int NOT NULL,
     "customer_name" varchar(30) NOT NULL,
     "segment"       varchar(15) NOT NULL,
     "country"       varchar(15) NOT NULL,
     "region_id"     int NOT NULL,
     "state"         varchar(30) NOT NULL,
     "city"          varchar(20) NOT NULL,
     "postal_code"   int NULL,
     CONSTRAINT "PK_4" PRIMARY KEY ( "customers_id" ),
     CONSTRAINT "FK_2" FOREIGN KEY ( "region_id" ) REFERENCES "region" ( "region_id" )
    );

    CREATE INDEX "FK_1" ON "customer"
    (
     "region_id"
    );


### Category

    CREATE TABLE "category"
    (
     "category_id"   int NOT NULL,
     "category_name" varchar(15) NOT NULL,
     CONSTRAINT "PK_9" PRIMARY KEY ( "category_id" )
    );

### Sub_category

    CREATE TABLE "sub_category"
    (
     "sub_category_id"   int NOT NULL,
     "category_id"       int NOT NULL,
     "sub_category_name" varchar(15) NOT NULL,
     CONSTRAINT "PK_8" PRIMARY KEY ( "sub_category_id" ),
     CONSTRAINT "FK_4" FOREIGN KEY ( "category_id" ) REFERENCES "category" ( "category_id" )
    );

    CREATE INDEX "FK_8" ON "sub_category"
    (
     "category_id"
    );


### Product

    CREATE TABLE "product"
    (
     "product_id"      int NOT NULL,
     "sub_category_id" int NOT NULL,
     "product_name"    varchar(150) NOT NULL,
     CONSTRAINT "PK_7" PRIMARY KEY ( "product_id" ),
     CONSTRAINT "FK_5" FOREIGN KEY ( "sub_category_id" ) REFERENCES "sub_category" ( "sub_category_id" )
    );

    CREATE INDEX "FK_7" ON "product"
    (
     "sub_category_id"
    );


### Shipping


    CREATE TABLE "shipping"
    (
     "shipping_id"   int NOT NULL,
     "shipping_type" varchar(15) NOT NULL,
     CONSTRAINT "PK_2" PRIMARY KEY ( "shipping_id" )
    );


### Date


    CREATE TABLE "date"
    (
     "date_id"   int NOT NULL,
     "year"      int NOT NULL,
     "full_date" date NOT NULL,
     "month"     int NOT NULL,
     "day"       int NOT NULL,
     CONSTRAINT "PK_1" PRIMARY KEY ( "date_id" )
    );


### The_order


    CREATE TABLE "the_order"
    (
     "the_order_id" int NOT NULL,
     "date_id"      int NOT NULL,
     "product_id"   int NOT NULL,
     "ship_date"    date NOT NULL,
     "shipping_id"  int NOT NULL,
     "customers_id" int NOT NULL,
     "returned"     varchar(3) NOT NULL,
     "sales"        decimal NOT NULL,
     "profit"       decimal NOT NULL,
     "discount"     int NULL,
     "quantity"     int NOT NULL,
     CONSTRAINT "PK_3" PRIMARY KEY ( "the_order_id" ),
     CONSTRAINT "FK_9" FOREIGN KEY ( "product_id" ) REFERENCES "product" ( "product_id" ),
     CONSTRAINT "FK_1" FOREIGN KEY ( "shipping_id" ) REFERENCES "shipping" ( "shipping_id" ),
     CONSTRAINT "FK_3" FOREIGN KEY ( "customers_id" ) REFERENCES "customer" ( "customers_id" ),
     CONSTRAINT "FK_8" FOREIGN KEY ( "date_id" ) REFERENCES "date" ( "date_id" )
    );

    CREATE INDEX "FK_10" ON "the_order"
    (
     "product_id"
    );

    CREATE INDEX "FK_2" ON "the_order"
    (
     "shipping_id"
    );

    CREATE INDEX "FK_3" ON "the_order"
    (
     "customers_id"
    );

    CREATE INDEX "FK_4" ON "the_order"
    (
     "date_id"
    );