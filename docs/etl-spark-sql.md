# ETL com Spark SQL

Spark SQL permite processar dados estruturados e semi-estruturados.

## Exemplo de ETL
```sql
-- Ingestão
CREATE TEMP VIEW source AS SELECT * FROM csv.`data/sample_data.csv`;

-- Transformação
CREATE TEMP VIEW transformed AS SELECT nome, idade * 2 AS idade_dobrada FROM source;

-- Carga
INSERT INTO delta_table SELECT * FROM transformed;
```