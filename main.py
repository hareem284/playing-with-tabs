#You are part of the Data Analytics team of the Mavericks Cricket Team. A database is provided to you that consists of all the details and statistics of the team. For analysing the data of the Matches table, perform the following tasks using SQL.

# IMPORTING sqlite3
import sqlite3
# importing pandas
import pandas as pd
cd=sqlite3.connect('database.sqlite')
print("connection is established")
# doing thinds for pandas
readM=pd.read_sql("SELECT * FROM Match;",cd)
print(readM)
readingT=pd.read_sql("SELECT * FROM Team;",cd)
print(readingT)
#reading all the matches whic were won my mi
readmi=pd.read_sql("SELECT * FROM MATCH WHERE Match_Winner==7;",cd)
print(readmi)
# selecting all the data where team name starts with de
readde=pd.read_sql("SELECT * FROM Team WHERE Team_Name LIKE 'De%';",cd)
print(readde)