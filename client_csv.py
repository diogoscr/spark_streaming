from pyspark.sql import SparkSession as ss
import shutil

for item in ['./check', './csv']:
    try:
        shutil.rmtree(item)
    except OSError as err:
        print(f'Aviso: {err.strerror}')    

spark = ss.builder.appName('SparkStreaming').getOrCreate()

tweets = spark.readStream.format('socket').option('host', 'localhost').option('port', 9009).load()

query = tweets.writeStream.outputMode('append').option('enconding', 'utf-8').format('csv').option('path', './csv').option('checkpointLocation', './check').start()

query.awaitTermination()