import duckdb
con = duckdb.connect('warehouse.duckdb')
cnt = con.sql("select count(*) from gold_training_set").fetchone()[0]
print(f'gold_training_set: {cnt}')
