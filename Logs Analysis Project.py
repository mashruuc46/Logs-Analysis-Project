#!/usr/bin/env python3
"""Log Analysis Project for Full Stack Nanodegree by Udacity"""
import psycopg2


def connect_to_database():
    """Connects to the news database and return the result."""
    try:

        database = psycopg2.connect(
            database="news", user="postgres", password="123",
            host="localhost", port="5432")
        cursor = database.cursor()

    except psycopg2.DatabaseError:
        print("Failed to connect PostgreSQL database.")
        return None
    finally:
        return cursor


def most_popular_three_articles(db_cursor):
    """Query and print out the 3 most popular articles.

    Args:db_cursor: psycopg2 PostgreSQL database cursor object. """

    query = """ SELECT title,COUNT(*) as views FROM articles join log on
    substring(log.path,10)=articles.slug WHERE log.path = '/article/' ||
    articles.slug GROUP BY articles.title ORDER BY count(*)
    DESC LIMIT 3; """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('Q1: What are the most popular three articles of all time?\n')

    for result in results:
        print('"{title}" - {count} views'
              .format(title=result[0], count=result[1]))
    return


def most_popular_authors(db_cursor):
    """Query and print out the most popular authors.

    Args: db_cursor: psycopg2 PostgreSQL database cursor object. """

    query = """SELECT authors.name, count(*) FROM authors join
    articles on authors.id=articles.author join log on
    substring(log.path,10)=articles.slug  WHERE  log.path = '/article/' ||
    articles.slug GROUP BY authors.name ORDER BY count(*) DESC;"""
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('\nQ2: Who are the most popular article authors of all time?\n')

    for result in results:
        print('{author} - {count} views'
              .format(author=result[0], count=result[1]))
    return


def days_greater_than_1pc_errors(db_cursor):
    """Query and print out days when the error rate is greater than 1%.

    Args: db_cursor: psycopg2 PostgreSQL database cursor object. """

    query = """WITH No_Request AS ( SELECT time::date AS Days,
     count(*) FROM log GROUP BY time::date ORDER BY time::date ),
     No_Errors AS ( SELECT time::date AS Days, count(*) FROM log
     WHERE status != '200 OK' GROUP BY time::date
     ORDER BY time::date ), Percentage_Error AS (SELECT No_Request.days,
     No_Errors.count::float / No_Request.count::float * 100
     AS Errors FROM No_Request, No_Errors WHERE No_Request.days=
     No_Errors.days ) SELECT Days as Day,Errors FROM Percentage_Error
     WHERE errors > 1 """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('\nQ3: On which days did more than 1% of requests lead to errors?\n')

    for result in results:
        print('{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(
            date=result[0],
            error_rate=result[1]))
    return


if __name__ == "__main__":
    CURSOR = connect_to_database()
    if CURSOR:
        most_popular_three_articles(CURSOR)
        most_popular_authors(CURSOR)
        days_greater_than_1pc_errors(CURSOR)
        CURSOR.close()
    print()
