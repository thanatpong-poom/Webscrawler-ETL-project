
import os
import psycopg2
import time

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='21Octoberc99',
    dbname='mydatabase',
    port=5432
)

# delete all rows before inserting
with conn, conn.cursor() as cursor:
    cursor.execute('CREATE TABLE IF NOT EXISTS restuarant(res_id serial,res_name varchar(50),res_description text,res_rating float(3),res_price_min float(3),res_price_max float(3),res_email varchar(50),res_phone varchar(12),res_street_1 varchar(50),res_street_2 varchar(50),res_city varchar(20),res_country varchar(30),res_postcode varchar(20))')
    cursor.execute('CREATE TABLE IF NOT EXISTS res_award(res_award_id serial,award_id serial,res_id serial)')
    cursor.execute('CREATE TABLE IF NOT EXISTS award(award_id serial,award_name varchar(50))')
    cursor.execute('CREATE TABLE IF NOT EXISTS res_cuisin(res_cuisine_id serial,cuisine_id serial,res_id serial)')
    cursor.execute('CREATE TABLE IF NOT EXISTS cuisin(cuisine_id serial,cuisine_name varchar(50))')
    cursor.execute('CREATE TABLE IF NOT EXISTS res_metro_station(res_station_id serial,station_id serial,res_id serial)')
    cursor.execute('CREATE TABLE IF NOT EXISTS metro_station(station_id serial,station_name varchar(50))')
    cursor.execute('CREATE TABLE IF NOT EXISTS res_operateday(res_operateday_id serial,operateday_id serial,operatetime_res_operate_day_id serial)')
    cursor.execute('CREATE TABLE IF NOT EXISTS operatetime_res_operate_day(operatetime_res_operate_day_id serial,res_operateday_id serial,operatime_id serial)')
    cursor.execute('CREATE TABLE IF NOT EXISTS operatetime_res_operate_day(operatetime_res_operate_day_id serial,res_operateday_id serial,operatime_id serial)')
    cursor.execute('CREATE TABLE IF NOT EXISTS operate_time(operatime_id serial,close_time time ,open_time time)')
    cursor.execute('CREATE TABLE IF NOT EXISTS operate_day(operateday_id serial,operateday_name varchar(15))')

# Add primary keys

    cursor.execute('ALTER TABLE restuarant ADD CONSTRAINT pk_resturant PRIMARY KEY (res_id)')

    cursor.execute('ALTER TABLE award ADD CONSTRAINT pk_award PRIMARY KEY (award_id)')

    cursor.execute('ALTER TABLE res_award ADD CONSTRAINT pk_res_award PRIMARY KEY (res_award_id)')

    cursor.execute('ALTER TABLE res_cuisin ADD CONSTRAINT pk_res_cuisin_id PRIMARY KEY (res_cuisine_id)')

    cursor.execute('ALTER TABLE cuisin ADD CONSTRAINT pk_cuisin PRIMARY KEY (cuisine_id)')

    cursor.execute('ALTER TABLE res_metro_station ADD CONSTRAINT pk_resstation PRIMARY KEY (res_station_id)') 

    cursor.execute('ALTER TABLE metro_station ADD CONSTRAINT pk_station PRIMARY KEY (station_id)')

    cursor.execute('ALTER TABLE operatetime_res_operate_day ADD CONSTRAINT pk_operatetime_res_operate_day PRIMARY KEY (operatetime_res_operate_day_id)')

    cursor.execute('ALTER TABLE operate_time ADD CONSTRAINT pk_operate_time PRIMARY KEY (operatime_id)')
    
    cursor.execute('ALTER TABLE operate_day ADD CONSTRAINT pk_operate_day PRIMARY KEY (operateday_id)')

    cursor.execute('ALTER TABLE res_operateday ADD CONSTRAINT pk_res_operate_day PRIMARY KEY (res_operateday_id)')


#Add foreign keys

    cursor.execute('ALTER TABLE res_award ADD CONSTRAINT fk_res_award FOREIGN KEY (res_id) REFERENCES restuarant(res_id), ADD CONSTRAINT fk_award_resaward FOREIGN KEY (award_id) REFERENCES award(award_id)')

    cursor.execute('ALTER TABLE res_cuisin ADD CONSTRAINT fk_res_cuisin FOREIGN KEY (res_id) REFERENCES restuarant(res_id), ADD CONSTRAINT fk_cuisin_rescuisin FOREIGN KEY (cuisine_id) REFERENCES cuisin(cuisine_id)')

    cursor.execute('ALTER TABLE res_metro_station ADD CONSTRAINT fk_resmetro_metrostation FOREIGN KEY (station_id) REFERENCES metro_station(station_id), ADD CONSTRAINT fk_resmetro_rest FOREIGN KEY (res_id) REFERENCES restuarant(res_id)')

    cursor.execute('ALTER TABLE res_operateday ADD CONSTRAINT fk_res_operateday_id FOREIGN KEY (operateday_id) REFERENCES operate_day(operateday_id), ADD CONSTRAINT fk_resoperate_operatetime FOREIGN KEY (operatetime_res_operate_day_id) REFERENCES operatetime_res_operate_day(operatetime_res_operate_day_id)')

    cursor.execute('ALTER TABLE operatetime_res_operate_day ADD CONSTRAINT fk_resoperatetime_resoperateday FOREIGN KEY (res_operateday_id) REFERENCES res_operateday(res_operateday_id), ADD CONSTRAINT fk_resoperate_operatetime FOREIGN KEY (operatime_id) REFERENCES operate_time(operatime_id)')







    





  



