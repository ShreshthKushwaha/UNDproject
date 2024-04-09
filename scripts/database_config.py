import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Shreshth@2023'
)


conn.reconnect()
cursor = conn.cursor()

# Create database if not exists
cursor.execute('CREATE DATABASE IF NOT EXISTS social_media')

# Switch to the social_media database
cursor.execute('USE social_media')


#dropping stale tables

cursor.execute('''
    DROP TABLE IF EXISTS post_tags
''')

cursor.execute('''
    DROP TABLE IF EXISTS tag
''')

cursor.execute('''
    DROP TABLE IF EXISTS post
''')




# Create required tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS post (
        id VARCHAR(255) PRIMARY KEY,
        date DATETIME,
        message TEXT,
        author VARCHAR(255),
        image TEXT,
        username VARCHAR(255),
        location VARCHAR(255),
        likes INT,
        reposts INT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tag (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS post_tags (
        post_id VARCHAR(255),
        tag_id INT,
        FOREIGN KEY (post_id) REFERENCES post(id),
        FOREIGN KEY (tag_id) REFERENCES tag(id),
        PRIMARY KEY (post_id, tag_id)
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
