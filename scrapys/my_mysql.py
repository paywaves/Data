import pymysql as pymysql


def connect():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         db='family',
                         user='root',
                         password='123456',
                         charset='utf8')
    return db


def create_table(name):
    db = connect()
    cursor = db.cursor()
    sql = 'create table %s(id int auto_increment primary key)engine=innodb default charset=utf8;' % name
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def insert_keys(table_name, name, name_type, other=''):
    db = connect()
    cursor = db.cursor()
    sql = 'alter table %s add %s %s %s;' % (table_name, name, name_type, other)
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def search_data(name,key,value):
    db = connect()
    cursor = db.cursor()
    sql = 'select * from %s where %s="%s";' % (name, key, value)
    raw=cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return raw


def method_try(num, table_name, key_name='', type='varchar(10)'):
    db = connect()
    cursor = db.cursor()
    sql=''
    if num == 1:
        sql = 'alter table %s drop %s;' % (table_name, key_name)
    if num == 2:
        sql = 'alter table %s modify %s %s;' % (table_name, key_name, type)
    if num == 3:
        sql = 'drop table %s;' % table_name
    if num == 4:
        sql = 'truncate table %s;' % table_name
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def insert_data(table_name, table_key, datas):
    db = connect()
    cursor = db.cursor()
    keys = '('
    num = 1
    for key in table_key:
        if num == 1:
            keys += '%s' % key
        else:
            keys += ',%s' % key
        num += 1
    keys += ')'
    # values = tuple(datas)
    # search_key = search_data('%s' % table_name,'family_name',['赵'])
    # if not search_key:
    sql = 'insert into %s %s values %s;' % (table_name,keys,datas)
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


# def main():
#     db=connect()
#     # cursor=insert_keys('mogujie','tradeItemId','varchar(100)')
#     # cursor=insert_data('mogujie','(tradeItemId)','("dfsd")')
#     cursor.close()
#     db.close()


if __name__=='__main__':
    # main()
    pass