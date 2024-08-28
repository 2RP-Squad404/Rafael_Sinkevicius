# Relatório

#### Criação da tabela consolidada:
    
    CREATE TABLE tabela_consolidada

#### Seleção das colunas (SELECT compras.client_id):
    
    AS
    SELECT
        compras.client_id,

#### Calcula o preço total com a soma(SUM) do resultado da multiplicação entre price, amount e discount_applied, com o valor sendo renomeado como total_price:
    
    SUM(compras.price * compras.amount * compras.discount_applied) AS total_price,

#### Determina o local com mais compras utlizando MAX() na coluna purchase_location com o resultado renomeado para most_purchase_location:
    
    MAX(compras.purchase_location) AS most_purchase_location,

#### Obtém data e hora da primeira compra do cliente com MIN() na coluna purchase_datetime com o resultado renomeado para first_purchase:
    
    MIN(compras.purchase_datetime) AS first_purchase,

#### Obtém data e hora da última compra do cliente com MAX() na coluna purchase_datetime com o resultado renomeado para last_purchase:
    
    MAX(compras.purchase_datetime) AS last_purchase,

#### Determina a campanha mais recebida pelo cliente com MAX() na coluna type_campaign com o resultado renomeado para most_campaign:
    
    MAX(compras.type_campaign) AS most_campaign,

#### Conta quantas camapanhas enviadas ao cliente tiveram error como status, com COUNT() e uma condição CASE na coluna return_status, verificando se é igual a error com o resultado renomeado para quantity_error:
    
    COUNT(CASE WHEN compras.return_status = 'error' THEN 1 ELSE NULL END) AS quantity_error,

#### Insere a data atual para cada registro na coluna date_today sendo obtida por CURRENT_DATE:
    
    CURRENT_DATE AS date_today,

#### Formata a data atual como MMYYYY usando DATE_FORMAT(CURRENT_DATE, 'MMyyyy'), Em seguida, converte o resultado para um número inteiro e renomeia como anomes_today:
    
    CAST(DATE_FORMAT(CURRENT_DATE, 'MMyyyy') AS INT) AS anomes_today

#### Especifica a extração da tabela compras, realizando uma junção a esquerda com LEFT JOIN com a tabela campanhas baseado na coluna client_id, agrupando os resultados pelo mesmo, com cada linha da tabela representando um cliente e todos os cálculos sendo realizados dentro de cada grupo de cliente:
    
    FROM compras
    
    LEFT JOIN 
        campanhas ON compras.client_id = campanhas.client_id
    
    GROUP BY
        compras.client_id

#### Exibe a tabela criada com um limite de 10 linhas:
    
    SELECT * FROM tabela_consolidada LIMIT 10