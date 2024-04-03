select a.product_id, COALESCE(round((sum(a.prod)/sum(a.units)),2), 0)  as average_price  from
(SELECT p.product_id, COALESCE(u.units, 0) AS units, p.price, COALESCE(u.units, 0) * p.price AS prod
from Prices p left join UnitsSold u on u.product_id = p.product_id and u.purchase_date between p.start_date and p.end_date) a
group by a.product_id