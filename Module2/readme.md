# Lab work for DE-101 Module2

## 2.3
#### Sample of query (filling DB)

    DROP TABLE IF EXISTS people;
    CREATE TABLE people(
       Person VARCHAR(17) NOT NULL PRIMARY KEY
      ,Region VARCHAR(7) NOT NULL
    );
    INSERT INTO people(Person,Region) VALUES ('Anna Andreadi','West');
    INSERT INTO people(Person,Region) VALUES ('Chuck Magee','East');
    INSERT INTO people(Person,Region) VALUES ('Kelly Williams','Central');
    INSERT INTO people(Person,Region) VALUES ('Cassandra Brandow','South');

#### SQL (metricks)

Динамика дохода и прибыли
    select extract ('year' From order_date) as yr,
    extract ('month' From order_date) as mn,
    SUM(sales) as s,
    SUM(profit) as p
    from orders
    group by 1,2
    order by 1,2
	
	
Категории товаров(сравнение)
	select category,
	subcategory,
	SUM(sales) as c_sales,
	SUM(profit) as c_profit,
	COUNT(order_id) as c_orders
	from orders
	group by category, subcategory
	order by 1
	
	
Региональные менеджеры(сравнение)	
	select person, SUM(sales), SUM(profit), COUNT(distinct order_id)
	from people inner join orders USING(region)
	group by person
	order by 3
	
	
Сегменты(сравнение)	
	select segment, SUM(sales), SUM(profit), COUNT(distinct order_id)
	from orders
	group by segment
	order by 1
	
	
Динамика по сегментам	
	select segment,
	extract ('year' From order_date) as yr,
	extract ('month' From order_date) as mn,
	SUM(sales) as s,
	SUM(profit) as p
	from orders
	group by 1,2,3
	order by 1,2,3
	
	
Основные показатели	
	select SUM(sales),
	SUM(profit),
	AVG(profit/sales),
	AVG(discount)
	from orders
	
	
По штатам	
select state, SUM(sales), SUM(profit), COUNT(distinct order_id)
from orders
group by state
order by 1
	
	
По регионам(сравнение)	
	select region, SUM(sales), SUM(profit), COUNT(distinct order_id)
	from orders
	group by region
	order by 1


По возвратам в %

	with o(o_row_id, o_order_id, o_sales, o_returned)
	AS
	(select distinct row_id, order_id, sales, returned
	from orders left join returns using(order_id)
	order by 1),
	
	s(s_sum_sales)
	as
	(select SUM(sales)
	from orders)
	
	select coalesce(o_returned, 'No'), ROUND(SUM(o_sales)/s_sum_sales * 100, 2)
	from o, s
	group by o_returned, s_sum_sales;
