import os
from flask import Flask, request
from flask_mysqldb import MySQL
app = Flask('Practice app')
app.debug = True

app.config['MYSQL_HOST']=os.environ['MYSQL_HOST']
app.config['MYSQL_PORT']=int(os.environ['MYSQL_PORT'])
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='password'
app.config['MYSQL_DB']='flask'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)


@app.route('/users/<user_id>', methods=['GET', 'POST'])
def users(user_id):
    if request.method == 'GET':
        print('Performing a GET')
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('''SELECT * FROM user WHERE id=%s;''',user_id)
            user= cursor.fetchone()
            mysql.connection.commit()
            cursor.close()
            print(user)
            return user
        except:
            return "No data found"
    elif request.method == 'POST':
        print('Performing a POST')
        data = request.get_json()
        try:
            print(data)
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO user(name,lastname,role) VALUES(%s,%s,%s);''',(data.get('name'),data.get('lastname'),data.get('role')))
            mysql.connection.commit()
            cursor.close()
            return '''
                    <h1>The framework value is: {}</h1>'''.format(data)
        except Exception as e:
            return f"Was no able to save data {data}, due '{e}'"
