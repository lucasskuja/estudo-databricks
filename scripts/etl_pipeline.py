# Pipeline ETL Básico

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

# Exemplo de ETL
df = spark.read.csv("data/sample_data.csv", header=True)
df_transformed = df.withColumn("nova_coluna", df["coluna_existente"] * 2)
df_transformed.write.format("delta").save("data/output")

print("ETL concluído!")