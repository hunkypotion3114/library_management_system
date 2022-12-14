# Graphs borrowed books genre wise
# Total borrowed books per genre/publicaton/author
# Books per author/genre/publication
# User stattistics
#  Most of these graphs will be frequency analysis graphs for users
# For books we have four variations :
# --> T.Quantity vs Author,Publication,Genre
# --> T.price vs Author,Publication,Genre
# --> Times_borrowed vs Author,Publication,Genre
# For Users we have:
# BorrowedList --> Bins analysis
# Dues --> Bins analysis

import pandas as pd
import matplotlib.pyplot as pl
import sql_functions as sql
# Book vs attribute graph:
def BookVAttr(cursor,t_name,attribute,agg_type):
    book_attrs = ['quantity','times_borrowed','price*quantity']
    # Price Graphs
    if(agg_type != 'count'):
        for b_attr in book_attrs:
            df = sql.select(cursor,[attribute,f'{agg_type}({b_attr})'],t_name,group_by=attribute,printable=0)
            print(df)
            pl.bar(list(df[attribute]),df[f'{agg_type}({b_attr})']) 
            pl.xlabel(attribute)
            pl.title(f'{attribute} vs {b_attr}')
            pl.show()
    else :
        df = sql.select(cursor,[attribute,f'count(*)'],t_name,group_by=attribute,printable=0)
        pl.bar(list(df[attribute]),df[f'count(*)']) 
        pl.xlabel(attribute)
        pl.title(f'{attribute} vs count(*)')
        pl.show()

def UserStats(cursor,t_name,attribute):
    if(len(attribute) == 1):
        df = sql.select(cursor,[attribute],t_name)
        pl.hist(df[attribute],bins=40)
        pl.xlabel(attribute)
        pl.title(f'{attribute} vs number')
        pl.show()