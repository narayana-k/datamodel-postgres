# DROP TABLES

songplay_table_drop = "DROP table songplays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table time"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays  (songplay_id  SERIAL  PRIMARY KEY  , start_time timestamp , user_id int , level varchar, song_id varchar , artist_id varchar, session_id int, location varchar, user_agent varchar );")

user_table_create = ("CREATE TABLE IF NOT EXISTS users    (user_id int PRIMARY KEY, first_name varchar , last_name varchar, gender varchar, level varchar);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs  (song_id varchar PRIMARY KEY, title varchar NOT NULL, artist_id varchar, year int, duration int);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists   (artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, latitude int , longitude int  );")

time_table_create = ("CREATE TABLE IF NOT EXISTS time   (start_time timestamp PRIMARY KEY, hour int, day int, week int, month int, year int, weekday int);")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays ( start_time  , user_id , level , song_id , artist_id , session_id , location , user_agent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

user_table_insert = ("INSERT INTO users (user_id , first_name , last_name , gender , level ) VALUES (%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO UPDATE SET level = excluded.level")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id,year,duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

artist_table_insert = ("INSERT INTO artists (artist_id , name , location , latitude , longitude ) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")


time_table_insert = ("INSERT INTO time   (start_time , hour , day , week , month , year , weekday )VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

# FIND SONGS
#row.song, row.artist, row.length
song_select = ("select a.song_id, b.artist_id from songs a, artists b where a.title=%s and b.name=%s and a.duration=%s")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
#drop_table_queries = []