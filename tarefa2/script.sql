CREATE TABLE tabela_consolidada AS
SELECT
    compras.client_id,

    SUM(compras.price * compras.amount * compras.discount_applied) AS total_price,

    MAX(compras.purchase_location) AS most_purchase_location,

    MIN(compras.purchase_datetime) AS first_purchase,

    MAX(compras.purchase_datetime) AS last_purchase,

    MAX(campanhas.type_campaign) AS most_campaign,

    COUNT(CASE WHEN campanhas.return_status = 'error' THEN 1 END) AS quantity_error,

    CURRENT_DATE AS date_today,

    CAST(DATE_FORMAT(CURRENT_DATE, 'MMyyyy') AS INT) AS anomes_today

FROM 
    compras
    
LEFT JOIN 
    campanhas ON compras.client_id = campanhas.client_id

GROUP BY 
    compras.client_id

SELECT * FROM tabela_consolidada LIMIT 10