#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from analysis_db import get_top_articles, get_top_authors, get_top_errors

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Project: Log Analysis</title>
    <style>
      h2{ text-align: center; }      
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%;}
      hr.postbound { width: 50%%; }
      em { color: #999 }
    </style>
  </head>
  <body>
    <h2>Top 3 Articles</h2>    
    <!-- post content will go here -->
%s
    <br>
    <h2>Top Authors</h2>    
%s
    <br>
    <h2>Day did more than 1%% errors</h2>    
%s    
  </body>
</html>
'''

# HTML template for an individual comment
TOP_ARTICLES_AUTHORS_DIV = '''\
    <div class=post>%s     - <em> %s views</em></div>
'''

TOP_ERRORS_DIV = '''\
    <div class=post>%s     - <em> %s%% errors</em></div>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''

  top_articles_html = "".join(TOP_ARTICLES_AUTHORS_DIV % (title, views) for title, views in get_top_articles())
  top_authors_html  = "".join(TOP_ARTICLES_AUTHORS_DIV % (name, views) for name, views in get_top_authors())
  top_errors_html  = "".join(TOP_ERRORS_DIV % (date, errors) for date, errors in get_top_errors())
  html = HTML_WRAP % (top_articles_html, top_authors_html, top_errors_html)
  return html


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

