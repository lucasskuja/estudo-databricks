# Introdução ao Delta Lake

Delta Lake é uma camada de armazenamento open-source que traz ACID transactions para big data.

## Benefícios
- Transações ACID
- Schema enforcement
- Time travel

## Exemplo Básico
```sql
CREATE TABLE delta_table USING DELTA AS SELECT * FROM source_table;
```