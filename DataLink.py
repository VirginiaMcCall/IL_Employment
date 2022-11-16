import pyodbc 
import sqlalchemy as sa 
from sqlalchemy import create_engine 
import urllib 
import pymssql


#Connection string info for SQL Server
conn = urllib.parse.quote_plus( 
    "Data Source Name=desktop-05qb2nr\Tidy Momma's;"
    'Driver={SQL Server};' 
    'Server=desktop-05qb2nr\sqlexpress;' 
    'Database=IL_Emp;' 
    'Trusted_connection=yes;' 
    
) 
#Connection to MSSQL
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn)) 