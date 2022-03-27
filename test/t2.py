import pymysql
# host# passward# user# database name
db = pymysql.connect(host='127.0.0.1', user='root',
                        password='12345678',
                        database='sample', 
                         port=3306,  
                         charset='utf8')
cursor = db.cursor()

sql_command = 'SELECT * FROM products_product'
cursor.execute(sql_command)
data = cursor.fetchall()

print('{}'.format(data))