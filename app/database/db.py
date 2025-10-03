from langchain_community.utilities.sql_database import SQLDatabase
import sqlite3 as sqlite

conn = sqlite.connect("Xp.db")
cursor = conn.cursor()

DB = SQLDatabase.from_uri("sqlite:///c:/Users/gabri/Desktop/agenteLanchain/app/database/Xp.db")