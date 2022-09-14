import sqlite3 
con = sqlite3.connect('C:\\Users\\joey\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History') 
cursor = con.cursor() 
cursor.execute("SELECT url FROM urls") 
urls = cursor.fetchall() 
print('\n'.join(urls))