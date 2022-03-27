from clickhouse_driver import Client,connection

client = Client(host='localhost',password="nur")

print(client.execute('SHOW DATABASES'))


reuslt = client.execute('SELECT * FROM mysql_db_v2.products_product LIMIT 5')
# reuslt = client.execute('SELECT * FROM system.numbers LIMIT 5')
print(reuslt)