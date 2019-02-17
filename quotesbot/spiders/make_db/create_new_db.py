import sqlite3


def insertValuesInDb(value1,value2):
    sqlite_file = 'create_newdb.db' 
    table_name1 = 'Jobs_Title'  
    table_name2 = 'Jobs_Links'  


    new_field='Title_Of_the_Job'
    new_field2='Links'
    field_type='TEXT'
    





    conn = sqlite3.connect('/home/rado/quotesbot/quotesbot/spiders/make_db/create_newdb.db')
    c = conn.cursor()
    #delete the tables
    #c.execute('DROP TABLE Jobs_Links')
    #c.execute('DROP TABLE Jobs_Title')

    #add column to an existing table
    #c.execute('ALTER TABLE {table_name} ADD COLLUMN {type1}'.format(table_name=table_name1,type1='TEXT'))



    
    #create table with two columns
    #c.execute('CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft}, {af} {bt}) '.format(tn=table_name2, nf=new_field, ft=field_type, af=new_field2,bt=field_type1))




    #inserting some values into the table
    c.execute('INSERT INTO {what} ({c1}, {c2}) VALUES ({v1}, {v2})'.format(what=table_name1 (c1=new_field,c2=new_field2) (v1= value1,v2=value2)))   
    
    #c.execute('CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=table_name2, nf=new_field2, ft=field_type))
    #c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name, cn=new_column1, ct=column_type))



    conn.commit()
    conn.close()
    return

