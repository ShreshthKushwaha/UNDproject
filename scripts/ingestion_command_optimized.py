import requests
import mysql.connector
from datetime import datetime, timedelta

def ingest_posts(begin_date, end_date):
    # Make API request
    try:
        url = 'https://apps.und.edu/demo/public/index.php/post'
        params = {'from': begin_date, 'to': end_date}
        response = requests.get(url, params=params)
        posts = response.json()
        
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Shreshth@2023',
            database='social_media'  # Specify your database name here
        ) 
        conn.reconnect()
        cursor = conn.cursor()
        
        # Insert posts into the database
        for post in posts:
            # Check if post already exists using its unique id
            cursor.execute('SELECT id FROM post WHERE id = %s', (post['id'],))
            existing_post = cursor.fetchone()
            if existing_post:
                print(f"Post with id {post['id']} already exists. Skipping insertion.")
                print (post['date'])
                continue
            
            cursor.execute('''
                INSERT INTO post (id, date, message, author, image, username, location, likes, reposts)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (post['id'], post['date'], post['message'], post['author'], post['image'], post['username'], post['location'], post['likes'], post['reposts']))
            
            # Process hashtags
            for hashtag in post['message'].split():
                if hashtag.startswith('#'):
                    # Check if tag already exists using its name
                    cursor.execute('SELECT id FROM tag WHERE name = %s', (hashtag,))
                    existing_tag = cursor.fetchone()
                    if not existing_tag:
                        cursor.execute('INSERT INTO tag (name) VALUES (%s)', (hashtag,))
                    cursor.execute('''
                        INSERT IGNORE INTO post_tags (post_id, tag_id)
                        SELECT %s, id FROM tag WHERE name = %s
                    ''', (post['id'], hashtag))
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")






# Define the function to ingest posts for a range of dates
def get_min_max_post_dates():
    ##replace it with your db credentials
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Shreshth@2023',
            database='social_media'
        ) 
        conn.reconnect()
        cursor = conn.cursor()
        
        cursor.execute("SELECT MIN(date), MAX(date) FROM post")
        min_date, max_date = cursor.fetchone()
        
        conn.close()
        
        return min_date, max_date
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None

def ingest_posts_range(start_date, end_date):
    min_post_date, max_post_date = get_min_max_post_dates()
    
    
        
        
    start_array = [int(y) for y in start_date.split('-')]
    end_array = [int(x) for x in end_date.split('-')]
    start_date = datetime(start_array[0],start_array[1],start_array[2])
    end_date = datetime(end_array[0],end_array[1],end_array[2])

    if start_date > end_date:
        print("Start date should be before end date.")
        return

    if min_post_date is not None and max_post_date is not None:
        print (min_post_date,start_date,max_post_date,end_date)
        # Check if there are posts in the database
        if start_date >= min_post_date and end_date <= max_post_date:
          
            print("Posts for the specified date range already exist in the database.")
            return
        elif start_date < min_post_date and end_date < max_post_date:
            end_date = min(end_date,min_post_date)
            print("Posts for the specified date range partially exist in the database.")
        elif start_date > min_post_date and end_date > max_post_date:
            start_date = max(start_date,max_post_date)
            print("Posts for the specified date range partially exist in the database.")
        elif start_date<min_post_date and end_date>max_post_date:
            
            print("Posts for the specified date range partially exist in the database.") 
            ingest_posts_range(start_date.strftime('%Y-%m-%d'),min_post_date.strftime('%Y-%m-%d'))
            ingest_posts_range(max_post_date.strftime('%Y-%m-%d'),end_date.strftime('%Y-%m-%d'))
            return
                 

    delta = timedelta(days=2) 
    current_date = start_date
    
    while current_date <= end_date:
        chunk_end_date = min(current_date + delta, end_date)
        print(f"Ingesting posts from {current_date} to {chunk_end_date}")
        ingest_posts(current_date.strftime('%Y-%m-%d'), chunk_end_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=3) 

# Test the function
#ingest_posts_range('2023-12-02', '2025-04-7')






#(2004-01-01, 2011-01-05)

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validate_date_range(begin_date, end_date):
    begin_date_obj = datetime.strptime(begin_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

    # Validate begin_date is smaller than or equal to end_date
    if begin_date_obj > end_date_obj:
        return False
    return True    

def validate(begin_date, end_date):
    if not validate_date_format(begin_date) or not validate_date_format(end_date):
        return False, "Invalid date format. Use 'YYYY-MM-DD' format."
    
    if not validate_date_range(begin_date, end_date):
        return False, "begin_date should be smaller than or equal to end_date."
    
    return True, None


def takeInputs():
    startDate = input("Enter the start date in 'YYYY-MM-DD' format: ")
    endDate = input("Enter the end date in 'YYYY-MM-DD' format: ")
    valid_result=validate(startDate, endDate)
    if valid_result[0]==False:
        return valid_result[1]
    ingest_posts_range(startDate, endDate)
    return "Ingestion completed successfully"


print (takeInputs())




