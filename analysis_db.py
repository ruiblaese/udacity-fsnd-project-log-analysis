# "Database code" for the DB Forum.

import datetime
import psycopg2

#dev
#config_db = "dbname=news user=postgres password=pass host=localhost"

#vagrant
config_db = "dbname=news"

def get_top_articles():
  
  db = psycopg2.connect(config_db)
  c = db.cursor()
  query = """\
          select 
            articles.title,
            count(log.id)		
          from log
          inner join articles on position(articles.slug in log.path) > 0
          where
            log.status = '200 OK'
          group by 
            articles.title
          order by 
            count(log.id) desc
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
            count(log.id)		
          from log
          inner join articles on position(articles.slug in log.path) > 0
          inner join authors on authors.id = articles.author
          where
            log.status = '200 OK'
          group by 
            authors.name
          order by 
            count(log.id) desc
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
            cast( (( count(id)filter (where status <> '200 OK') * 100.00) / cast(count(id)as numeric)) as numeric(18,4)) as perc_error
          from log
          group by 
            cast("time" as date)
          having
            cast( (( count(id)filter (where status <> '200 OK') * 100.00) / cast(count(id)as numeric)) as numeric(18,4)) >= 1.00
          """  
  c.execute(query)
  rows = c.fetchall()
  db.close()  
  return rows  