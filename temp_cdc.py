import duckdb
con = duckdb.connect('warehouse.duckdb')

# Kiem tra op trong bronze_tickets_cdc
result = con.sql("select op, count(*) from bronze_tickets_cdc group by 1 order by 1").fetchall()
print("=== Phan bo op trong bronze ===")
for row in result:
    print(f"  {row[0]}: {row[1]}")

# Kiem tra tickets bi update nhieu lan
result = con.sql('''
select count(*) as total_tickets,
       count(distinct ticket_id) as distinct_tickets
from bronze_tickets_cdc where op = 'u'
''').fetchone()
print(f"\nBan ghi update: {result[0]} rows cho {result[1]} tickets")

# Check duplicate tickets
dup = con.sql('''
select ticket_id, count(*) as n
from bronze_tickets_cdc
group by 1 having n > 1
order by n desc limit 5
''').fetchall()
print("\nTickets co nhieu ban ghi CDC:")
for row in dup:
    print(f"  {row[0]}: {row[1]} ban ghi")