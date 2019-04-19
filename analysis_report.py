#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from analysis_db import get_top_articles, get_top_authors, get_top_errors


# HTML template for the forum page
HTML_WRAP = '''\

Top 3 Articles
%s

Top Authors
%s

Day(s) did more than 1%% errors
%s

'''

# TXT template
TXT_APPEND_VIEWS = '''\
%s -> %s views
'''

TXT_APPEND_ERRORS = '''\
%s -> %s%% errors
'''

top_articles_html = "".join(TXT_APPEND_VIEWS %
                            (title, views) for title, views in
                            get_top_articles())

top_authors_html = "".join(TXT_APPEND_VIEWS %
                           (name, views) for name, views in
                           get_top_authors())

top_errors_html = "".join(TXT_APPEND_ERRORS %
                          (date, errors) for date, errors in get_top_errors())

html = HTML_WRAP % (top_articles_html, top_authors_html, top_errors_html)
print(html)
