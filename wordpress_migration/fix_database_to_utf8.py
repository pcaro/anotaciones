from MySQLdb import connect
import MySQLdb


def alter_columns(conn, schema_name, table_name):
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='%s' AND TABLE_NAME='%s'" %
                   (schema_name, table_name))

    for row in cursor:
        character_set_name = row['CHARACTER_SET_NAME']
        if not character_set_name:
            continue
        import ipdb; ipdb.set_trace()
        query = build_query(row, schema_name, table_name, row['COLUMN_NAME'])

        print query + ";"
        alter_cursor = conn.cursor()
        try:
            try:
                alter_cursor.execute(query)
                print "-- Successfuly executed: %s" % query
            except:
                print_error("Failed %s;" % query)
        finally:
            alter_cursor.close()
    cursor.close()


def build_query(row, schema_name, table_name, column_name, new_charset='utf8', new_collation='utf8_general_ci'):
    column_type = row['COLUMN_TYPE']
    column_default = row['COLUMN_DEFAULT']
    is_nullable = (row['IS_NULLABLE'] == 'YES')
    query = "ALTER TABLE %s.%s MODIFY COLUMN %s %s" % (schema_name, table_name, column_name, column_type)
    query += " CHARSET %s" % new_charset
    query += " COLLATE %s" % new_collation

    if not is_nullable:
        query += " NOT NULL"
    if column_default:
        query += " DEFAULT '%s'" % column_default
    return query


def print_error(message):
    print "-- ERROR: %s" % message


conn = connect(user="root", passwd="PASSWORD")
cur = conn.cursor()

cur.execute("show databases;")
dbs_to_update = filter(
    lambda db: db not in ('information_schema', 'mysql', 'performance_schema'),
    [dbname[0] for dbname in cur.fetchall()])

dbs_to_update = ['blog']

for db_to_update in dbs_to_update:
    print "Updating %s db" % db_to_update
    print "-" * (12 + len(db_to_update))

    cur.execute("use %s" % db_to_update)
    cur.execute("show tables;")

    tables_to_update = [t[0] for t in cur.fetchall()]

    for table_to_update in tables_to_update:
        alter_columns(conn, db_to_update, table_to_update)
#         query = "ALTER TABLE %s CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;" % table_to_update
#         cur.execute(query)
#         print table_to_update, "updated"
