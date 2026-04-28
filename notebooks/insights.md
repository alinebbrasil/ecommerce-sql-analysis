# Insights - Análise E-commerce

## 1. Qualidade dos Dados

Antes da análise, foi feita uma verificação da qualidade dos dados.

Resultados encontrados:

- Total de registros brutos: 541.909
- Registros sem identificação de cliente: 135.080
- Registros sem descrição do produto: 1.454
- Registros com quantidade negativa: 10.624
- Registros com preço inválido: 2.517
- Registros de cancelamento: 9.288

Insight:

A base original contém registros que não são adequados para análise direta de clientes e receita, como clientes sem identificação, preços inválidos e transações de cancelamento.

Por isso, foi criada uma tabela final com regras de limpeza para manter apenas transações válidas, com cliente identificado, preço positivo e quantidade positiva.

Após a limpeza, a base final ficou com 397.884 registros.

---

## 2. Métricas Gerais

Resultados encontrados:

- Receita total: 8.911.407,90
- Ticket médio por pedido: 480,87

Insight:

A receita total indica um volume relevante de vendas na base analisada.

O ticket médio de aproximadamente 480,87 sugere que os pedidos podem envolver múltiplos itens ou compras em maior volume, indicando um comportamento mais próximo de compras recorrentes ou em quantidade do que compras unitárias simples.

---

## 3. Receita por País

Resultados encontrados (Top 10):

- United Kingdom: 7.308.391,55
- Netherlands: 285.446,34
- EIRE: 265.545,90
- Germany: 228.867,14
- France: 209.024,05
- Australia: 138.521,31
- Spain: 61.577,11
- Switzerland: 56.443,95
- Belgium: 41.196,34
- Sweden: 38.378,33

Insight:

A receita está altamente concentrada no Reino Unido, que representa a maior parte do faturamento total, indicando uma forte dependência de um único mercado.

Os demais países apresentam participação significativamente menor, mesmo os que aparecem no topo do ranking, como Netherlands e EIRE.

Isso sugere uma operação com presença internacional, mas com baixa diversificação de receita fora do mercado principal.

Em um cenário real de negócio, essa concentração pode representar risco, já que mudanças no mercado do Reino Unido podem impactar diretamente o faturamento da empresa.

---

## 4. Top Clientes por Receita

Resultados encontrados:

- Cliente 14646: 280.206,02
- Cliente 18102: 259.657,30
- Cliente 17450: 194.550,79
- Cliente 16446: 168.472,50
- Cliente 14911: 143.825,06
- Cliente 12415: 124.914,53
- Cliente 14156: 117.379,63
- Cliente 17511: 91.062,38
- Cliente 16029: 81.024,84
- Cliente 12346: 77.183,60

Insight:

Os dados mostram uma forte concentração de receita em poucos clientes, com os principais contribuindo com valores significativamente mais altos do que a média.

Isso indica um possível comportamento de clientes de alto valor, que realizam compras frequentes ou em grande volume.

Em um cenário real, essa concentração pode representar tanto uma oportunidade quanto um risco: esses clientes são estratégicos para o faturamento, mas também aumentam a dependência da empresa em um grupo reduzido.

A identificação e retenção desses clientes é fundamental para a sustentabilidade da receita.

---

## 5. Frequência de Clientes

Resultados encontrados:

- Total de clientes: 4.338
- Clientes de compra única: 1.493
- Clientes recorrentes: 2.845

Insight:

A maior parte dos clientes realiza mais de uma compra, indicando um comportamento recorrente e potencial fidelização.

A proporção de aproximadamente 66% de clientes recorrentes sugere uma base de clientes engajada, o que é positivo para a sustentabilidade da receita.

Por outro lado, cerca de 34% dos clientes realizam apenas uma compra, o que pode indicar oportunidades de melhoria em estratégias de retenção.

Em um cenário real, ações focadas em reengajamento desses clientes poderiam aumentar significativamente o valor gerado por cliente ao longo do tempo.

---

## 6. Valor por Cliente (LTV Simplificado)

Resultados encontrados (Top 10 clientes):

- Cliente 14646: 280.206,02 | 73 pedidos | ticket médio: 3.838,44  
- Cliente 18102: 259.657,30 | 60 pedidos | ticket médio: 4.327,62  
- Cliente 17450: 194.550,79 | 46 pedidos | ticket médio: 4.229,36  
- Cliente 16446: 168.472,50 | 2 pedidos | ticket médio: 84.236,25  
- Cliente 14911: 143.825,06 | 201 pedidos | ticket médio: 715,55  
- Cliente 12415: 124.914,53 | 21 pedidos | ticket médio: 5.948,31  
- Cliente 14156: 117.379,63 | 55 pedidos | ticket médio: 2.134,18  
- Cliente 17511: 91.062,38 | 31 pedidos | ticket médio: 2.937,50  
- Cliente 16029: 81.024,84 | 63 pedidos | ticket médio: 1.286,11  
- Cliente 12346: 77.183,60 | 1 pedido | ticket médio: 77.183,60  

Insight:

Os dados mostram diferentes perfis de clientes de alto valor.

Alguns clientes geram receita através de alta frequência de compras, como o cliente 14911, que realizou 201 pedidos com ticket médio mais baixo.

Outros clientes apresentam comportamento oposto, com poucas compras e valores extremamente elevados por pedido, como o cliente 16446.

Isso indica a coexistência de dois perfis distintos: clientes recorrentes de médio valor e clientes de baixo volume, mas alto ticket.

Em um cenário real, estratégias diferentes seriam necessárias para cada perfil, como programas de fidelização para clientes recorrentes e relacionamento personalizado para clientes de alto valor por transação.