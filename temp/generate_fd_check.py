# Hópur:
	# Ólafur Andri Davíðsson (olafurd18)
	# Pálmi C. Rúnarsson (palmi18)
	# Þór Breki Davíðsson (thord18)
TABLES = ["COFFEES"]
COLUMNS = ['DID', 'HID', 'CID', 'DN', 'DS', 'CN', 'CM']
filestream = open("temp/CHECKFD4.sql", "w+", newline="", encoding="UTF-8")
query = ""
def create_query(tablename, column, other_column):
	query = ""
	query += "SELECT '{}: {} --> {}' AS FD,\n".format(tablename, column, other_column)
	query += "\tCASE WHEN COUNT(*)=0 THEN 'GILDIR'\n"
	query += "\tELSE 'gildir ekki' END AS VALIDITY\n"
	query += "FROM (\n"
	query += "\tSELECT {}\n".format(column)
	query += "\tFROM {}\n".format(tablename)
	query += "\tGROUP BY {}\n".format(column)
	query += "\tHAVING COUNT(DISTINCT {}) > 1\n".format(other_column)
	query += ") X;\n"
	return query
for table in TABLES:
	for column in COLUMNS:
		for other_column in COLUMNS:
			if column == other_column:
				continue
			query += create_query(table, column, other_column)

filestream.write(query)
filestream.close()