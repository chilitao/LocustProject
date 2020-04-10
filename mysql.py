import pymysql
def sql(sql=None):
    db = pymysql.connect(host='13.234.218.139', user='root', password="pay%123", db='nanopay_test')

# 创建一个游标对象
    cursor = db.cursor()

    cursor.execute(sql)

    data = cursor.fetchall()[0]
    # for i in range(0, len(data)):
    #     print(data[i])
    return data
    db.close()
if __name__=='__main__':
    sql()