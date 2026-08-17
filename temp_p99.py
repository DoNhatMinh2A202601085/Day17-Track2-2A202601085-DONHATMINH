import duckdb
con = duckdb.connect('warehouse.duckdb')

print("=== PERCENTILE DO TRE (ngay) ===")
result = con.sql('''
select
    percentile_cont(0.50) within group (order by (epoch(_ingested_at) - epoch(event_time))/86400.0) as p50,
    percentile_cont(0.95) within group (order by (epoch(_ingested_at) - epoch(event_time))/86400.0) as p95,
    percentile_cont(0.99) within group (order by (epoch(_ingested_at) - epoch(event_time))/86400.0) as p99,
    max((epoch(_ingested_at) - epoch(event_time))/86400.0) as max_ngay,
    avg(case when _ingested_at > event_time + interval 1 day then 1.0 else 0 end) as ty_le_late
from bronze_events
''').fetchone()
print(f"P50: {result[0]:.4f} ngay ({result[0]*24:.1f} gio)")
print(f"P95: {result[1]:.4f} ngay ({result[1]*24:.1f} gio)")
print(f"P99: {result[2]:.4f} ngay ({result[2]*24:.1f} gio)")
print(f"Max: {result[3]:.4f} ngay ({result[3]*24:.1f} gio)")
print(f"Ty le toi muon (>1 ngay): {result[4]:.1%}")
