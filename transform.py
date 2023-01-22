import crawler
import datetime

loaded_data_list = crawler.data_list


def transform_latitude_longitude(data_dict):
    data_dict['latitude'] = float(data_dict['latitude'])
    data_dict['longitude'] = float(data_dict['longitude'])
    print(data_dict['latitude'],data_dict['longitude'])

def transform_numreviews(data_dict):
    data_dict['num_reviews'] = int(data_dict['num_reviews'])
    print(data_dict['num_reviews'])
    pass
def transform_raw_ranking(data_dict):
    data_dict['raw_ranking'] = float(data_dict['raw_ranking'])
    print(data_dict['raw_ranking'])
    
def transform_rating(data_dict):
    data_dict['rating'] = float(data_dict['rating'])
    print(data_dict['rating'])
    
def transform_price(data_dict):
    minp,maxp = data_dict['price'].replace(u'\xa0','').replace('THB','').replace('THB','-').strip().replace(',','').split(' - ')
    data_dict['min_price'] = float(minp)
    data_dict['max_price'] = float(maxp)
    print(data_dict['max_price'],data_dict['min_price'])
    
def transform_phone(data_dict):
    data_dict['phone'] =data_dict['phone'].replace(' ','-')
    print(data_dict['phone'])
    
def transform_open_close_time(data_dict):
    for day in data_dict['hours']['week_ranges']:   
        for item in day:
            
            
            open_time_hour = int(item['open_time'])//60
            open_time_minute = int(item['open_time'])%60
            close_time_hour = int(item['close_time'])//60
            close_time_minute = int(item['close_time'])%60
            if open_time_hour >=24:
                open_time_hour = 0
            if close_time_hour >= 24:
                close_time_hour = 0
            item['open_time'] = datetime.time(open_time_hour, open_time_minute)
            item['close_time'] = datetime.time(close_time_hour, close_time_minute)
            print(item['open_time'],item['close_time'])
def transform_main(data_dict):
    transform_latitude_longitude(data_dict)
    transform_numreviews(data_dict)
    transform_raw_ranking(data_dict)
    transform_rating(data_dict)
    transform_price(data_dict)
    transform_raw_ranking(data_dict)
    transform_phone(data_dict)
    transform_open_close_time(data_dict)

for key, value in crawler.data_list[0].items():
    print(key,  value, type(value))
    print()
    print('****')

for dict_item in crawler.data_list:
    transform_main(dict_item)
    # print(dict_item)
