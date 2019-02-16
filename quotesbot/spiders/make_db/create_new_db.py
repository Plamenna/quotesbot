import sqlite3

sqlite_file = 'create_newdb.db' 
table_name1 = 'Jobs_Title'  
#table_name2 = 'Jobs_Links'  


new_field='Title_Of_the_Job'
field_type='TEXT'


conn = sqlite3.connect('create_newdb.db')
c = conn.cursor()


c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name1, nf=new_field, ft=field_type))


conn.commit()
conn.close()


