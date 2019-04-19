# "Database code" for the DB Forum.

import datetime
import psycopg2

# dev
config_db = "dbname=news user=postgres password=pass host=localhost"

# vagrant
# config_db = "dbname=news"


def database_connect(database_name):
    """Connect to the database.  Returns a database connection."""
    try:
        db = psycopg2.connect(dbname=database_name)
        return db

    except psycopg2.Error as e:
        # THEN you could print an error
        # and perhaps exit the program
        print("Unable to connect to database")
        sys.exit(1)


def get_top_articles():
    db = psycopg2.connect(config_db)
    c = db.cursor()
    query = """\
          select
            articles.title,
            count(log.id) as views
          from log
          inner join articles on concat('/article/', articles.slug) = log.path
          where log.status = '200 OK'
          group by articles.title
          order by count(log.id) desc
          limit 3
          """
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def get_top_authors():
    db = psycopg2.connect(config_db)
    c = db.cursor()
    query = """\
          select
            authors.name,
            count(log.id) as views
          from log
          inner join articles on concat('/article/', articles.slug) = log.path
          inner join authors on authors.id = articles.author
          where (log.status = '200 OK')
          group by authors.name
          order by count(log.id) desc
          """
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def get_top_errors():
    db = psycopg2.connect(config_db)
    c = db.cursor()
    query = """\
          select
              cast("time" as date),
              cast(
                  (( count(id)filter (where status <> '200 OK') * 100.00) /
                  cast(count(id)as numeric)) as numeric(18,4)
              ) as perc_error
          from log
          group by
              cast("time" as date)
          having
              cast(
                  ((count(id)filter (where status <> '200 OK') * 100.00) /
                  cast(count(id)as numeric)) as numeric(18,4)
              ) >= 1.00
          """
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows
