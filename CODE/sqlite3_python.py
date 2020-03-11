#!/usr/bin/python

import sqlite3 as mydb
import sys

con = None

try:
	con = mydb.connect('../log/tempLog.db')
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
	data = cur.fetchone()
	print "SQLite version: %s" % data
except mydb.Error, e:
	print "Error %s:" % e.args[0]
	sys.exit(1)

finally:
	if con:
		con.close()
