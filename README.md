# Webscrawler-ETL-project

This project is related to ETL process, webscrawler(Extract), transform and load with python script. I implemented this project since I wanted to practice how to apply Apache airflow, Docker, and write a webscrawler with python. Data that I extract are restaurants in Bangkok that have a specific detail such as cuisine, location, price range, contact, award, etc. You can see my overall diagram below.

<img width="890" alt="image" src="https://user-images.githubusercontent.com/102346723/213926933-74d2ced1-9d50-4539-864a-6ce26a7f9ff4.png">

- According to the diagram, the etl process will run daily to extract restaurants data from tripadvisor and load into Postgresql database to keep update data in the database that data from source might have changed such as new restaurants, events, or new award. I designed a relational model to store data that you can see below.

![image](https://user-images.githubusercontent.com/102346723/213959850-5bd9648e-945d-4f72-8c56-04e41533073f.png)
