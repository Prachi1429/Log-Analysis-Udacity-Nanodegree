#!/usr/bin/env python3.6.4

# Log Analysis Project

# psycopg2 Python module to connect to database
import psycopg2

# Query_1: What are the most popular three articles of all time?
query_1 = """select  articles.title, count(*) as sum_1 from articles join log
on log.path like ('/article/%'||articles.slug)group by articles.title order by
sum_1 desc LIMIT 3;"""


# Query_2: Who are the most popular article authors of all time?
query_2 = """select authors.name, count(*) as sum_2 from authors join articles
on authors.id = articles.author join log on log.path like
('/article/%'||articles.slug) group by authors.name order by sum_2 desc LIMIT
4; """


# Query_3: On which days did more than 1% of requests lead to errors?
query_3 = """select to_char(time::DATE,'MonthDD,YYYY'), count(*) as sum_3 from
log where status LIKE('%404 NOT FOUND%') group by time having count(*) > 1
order by sum_3 desc LIMIT 1"""


def get_query(query):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def display_output():
    print("The most popular three articles of all time are:-- \n")
    result = get_query(query_1)
    for row in result:
        print(str(row[0]) + ' :- ' + str(row[1]) + ' views\n')
    print("The most popular article authors of all time are:-- \n")
    result = get_query(query_2)
    for row in result:
        print(str(row[0]) + ' :- ' + str(row[1]) + ' views\n')

    print("""The days on which more than 1% of requests lead to errors
    are :--\n""")
    result = get_query(query_3)
    for row in result:
        print(str(row[0]) + ' :- ' + str(row[1]) + '% errors\n')
# Call to output function
display_output()
