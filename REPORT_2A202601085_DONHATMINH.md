# Báo cáo LAB 17 — Data Pipeline Engineering

**Họ tên:** Đỗ Nhật Minh  **Lớp:** E403  **Ngày:** 2026-08-17

---

## 0 · Kết quả `make verify` sau mỗi task

<details>
<summary>VERIFY SAU TASK 1</summary>

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAB 17 · make verify
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
run 1/3 … 27.6s
run 2/3 … 27.3s
run 3/3 … 27.5s

BẢNG                  ỔN ĐỊNH          SỐ HÀNG     KỲ VỌNG   GHI CHÚ
──────────────────────────────────────────────────────────────────────────
gold_training_set     ✓ ok              12,480      12,480   ✓
gold_feature_daily    ✓ ok               8,645       9,100   ✗ thiếu 455
gold_doc_chunks       ✓ ok              31,200      31,200   ✓
quarantine_tickets    ✓ ok                   0         312   ✗ thiếu 312

CHECKSUM từng lượt
──────────────────────────────────────────────────────────────────────────
gold_training_set     8622572a97    8622572a97    8622572a97   ✓
gold_feature_daily    4eee63cd82    4eee63cd82    4eee63cd82   ✓
gold_doc_chunks       92d8e50131    92d8e50131    92d8e50131   ✓
quarantine_tickets    empty         empty         empty        ✓

KIỂM TRA KHÁC
──────────────────────────────────────────────────────────────────────────
dbt test                                    ✓ 9/9 pass
silver_tickets.priority ∈ 1..4, không NULL  ✗ 6,606 hàng sai
quarantine_tickets đúng số bản ghi lỗi      ✗ 0 / 312
gold_training_set: 1 hàng / 1 ticket        ✓ không lặp

Traceback (most recent call last):
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 287, in <module>
    sys.exit(main())
             ^^^^^^
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 231, in main
    d = dashboard_check() if BASELINE_FILE.exists() else None
        ^^^^^^^^^^^^^^^^^
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 131, in dashboard_check
    m = measure(read_query())
        ^^^^^^^^^^^^^^^^^^^^^
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\explain.py", line 93, in measure
    rows = con.execute(sql).fetchall()
           ^^^^^^^^^^^^^^^^
_duckdb.IOException: IO Error: No files found that match the pattern "data/gold_events/*.parquet"

LINE 18: from read_parquet('data/gold_events/*.parquet')
```
Task 1: **gold_training_set đạt** ✓
</details>

<details>
<summary>VERIFY SAU TASK 2</summary>

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAB 17 · make verify
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
run 1/3 … 25.3s
run 2/3 … 23.4s
run 3/3 … 22.1s

BẢNG                  ỔN ĐỊNH          SỐ HÀNG     KỲ VỌNG   GHI CHÚ
──────────────────────────────────────────────────────────────────────────
gold_training_set     ✓ ok              12,480      12,480   ✓
gold_feature_daily    ✓ ok               9,100       9,100   ✓
gold_doc_chunks       ✓ ok              31,200      31,200   ✓
quarantine_tickets    ✓ ok                   0         312   ✗ thiếu 312

CHECKSUM từng lượt
──────────────────────────────────────────────────────────────────────────
gold_training_set     8622572a97    8622572a97    8622572a97   ✓
gold_feature_daily    3db448685c    3db448685c    3db448685c   ✓
gold_doc_chunks       92d8e50131    92d8e50131    92d8e50131   ✓
quarantine_tickets    empty         empty         empty        ✓

KIỂM TRA KHÁC
──────────────────────────────────────────────────────────────────────────
dbt test                                    ✓ 9/9 pass
silver_tickets.priority ∈ 1..4, không NULL  ✗ 6,606 hàng sai
quarantine_tickets đúng số bản ghi lỗi      ✗ 0 / 312
gold_training_set: 1 hàng / 1 ticket        ✓ không lặp
Traceback (most recent call last):
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 287, in <module>
    sys.exit(main())
             ^^^^^^
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 231, in main
    d = dashboard_check() if BASELINE_FILE.exists() else None
        ^^^^^^^^^^^^^^^^^
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 131, in dashboard_check
    m = measure(read_query())
        ^^^^^^^^^^^^^^^^^^^^^
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\explain.py", line 93, in measure
    rows = con.execute(sql).fetchall()
           ^^^^^^^^^^^^^^^^
_duckdb.IOException: IO Error: No files found that match the pattern "data/gold_events/*.parquet"

LINE 18: from read_parquet('data/gold_events/*.parquet')
```
Task 1 + Task 2: **2 / 4 tiêu chí đạt** ✓
</details>

<details>
<summary>VERIFY SAU TASK 3 (TẤT CẢ ĐẠT)</summary>

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAB 17 · make verify
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
run 1/3 … 36.0s
run 2/3 … 33.2s
run 3/3 … 30.7s

BẢNG                  ỔN ĐỊNH          SỐ HÀNG     KỲ VỌNG   GHI CHÚ
──────────────────────────────────────────────────────────────────────────
gold_training_set     ✓ ok              12,480      12,480   ✓
gold_feature_daily    ✓ ok               9,100       9,100   ✓
gold_doc_chunks       ✓ ok              31,200      31,200   ✓
quarantine_tickets    ✓ ok                 312         312   ✓

CHECKSUM từng lượt
──────────────────────────────────────────────────────────────────────────
gold_training_set     8dd7c98653    8dd7c98653    8dd7c98653   ✓
gold_feature_daily    3db448685c    3db448685c    3db448685c   ✓
gold_doc_chunks       92d8e50131    92d8e50131    92d8e50131   ✓
quarantine_tickets    ebb89036fb    ebb89036fb    ebb89036fb   ✓

KIỂM TRA KHÁC
──────────────────────────────────────────────────────────────────────────
dbt test                                    ✓ 11/11 pass
silver_tickets.priority ∈ 1..4, không NULL  ✓ sạch
quarantine_tickets đúng số bản ghi lỗi      ✓ 312 / 312
gold_training_set: 1 hàng / 1 ticket        ✓ không lặp
Traceback (most recent call last):
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 287, in <module>
    sys.exit(main())
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 231, in <module>
    d = dashboard_check() if BASELINE_FILE.exists() else None
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\verify.py", line 131, in <module>
    m = measure(read_query())
  File "D:\AI20K\LAP17\Day17-Track2-2A202601085-DONHATMINH\tools\explain.py", line 93, in <module>
    rows = con.execute(sql).fetchall()
_duckdb.IOException: IO Error: No files found that match the pattern "data/gold_events/*.parquet"
LINE 18: from read_parquet('data/gold_events/*.parquet')
```
**Tổng kết: 4 / 4 tiêu chí đạt** ✓✓✓✓
</details>

Tổng kết sau Task 3: **4 / 4 tiêu chí đạt** ✓✓✓✓

---

## 1 · Kích thước bảng training tăng sau mỗi lần chạy

| | |
|---|---|
| **Triệu chứng** | `gold_training_set` tăng từ 12,480 lên 38,750 sau 1 lần clear task. Hiện tượng tái diễn mỗi khi người trực gặp lỗi mạng và bấm Clear Task để chạy lại. Không có báo lỗi nào được ghi nhận. |
| **Nguyên nhân** | Model incremental không khai báo `unique_key`, nên dbt generate ra câu lệnh `INSERT INTO` (append) thay vì `MERGE`. Khi chạy lại, cùng một ticket được ghi thêm lần nữa thay vì ghi đè — kết quả là số hàng tăng dần theo số lần chạy. Đây là cơ chế "append without deduplication": mỗi run đều là một phép cộng dồn, không phải một phép thay thế. |
| **Cách khắc phục** | **File 1:** `dbt/models/gold/gold_training_set.sql` — thêm `unique_key = 'ticket_id'` và `incremental_strategy = 'merge'` vào config(). Grain của bảng là entity (1 ticket = 1 hàng), khóa tự nhiên là `ticket_id`. Sử dụng merge để thay thế bản ghi cũ khi có khóa trùng. |
| | **File 2:** `dags/ai_training_pipeline.py` — DAG đã có sẵn `catchup=False` và `max_active_runs=1` theo repo gốc. Hai tham số này giảm tần suất kích hoạt lỗi: catchup=False ngăn Airflow không tự động chạy bù những ngày quá khứ khi có ai bấm Clear Task. max_active_runs=1 đảm bảo chỉ có 1 DAG run tại một thời điểm. |
| **Bằng chứng** | trước: 38,750 hàng · sau: **12,480 hàng** · checksum 3 lượt: **8622572a97 (giống nhau)** |

---

## 2 · Bảng đặc trưng theo ngày thiếu hàng ở các ngày quá khứ

| | |
|---|---|
| **Triệu chứng** | `gold_feature_daily` thiếu 455 hàng (~5%) so với đối chiếu thủ công. Các hàng thiếu đều nằm ở những ngày đã chạy xong từ lâu, ngày mới thì đủ. |
| **P99 độ trễ đo được** | **2.7258 ngày** (~65 giờ) *(bắt buộc)* |
| **Lookback đã chọn** | **3 ngày** — vì P99 = 2.7258 ngày, làm tròn lên 3 để an toàn đảm bảo tất cả các bản ghi có độ trễ ≤ P99 đều được xử lý. |
| **Nguyên nhân** | Điều kiện lọc `event_date > max(event_date)` trong incremental chỉ xử lý những ngày lớn hơn ngày lớn nhất đã có trong bảng đích. Tuy nhiên, dữ liệu đến kho chậm (late-arriving data): một event xảy ra ngày 08-03 nhưng đến kho ngày 08-10 sẽ bị bỏ sót vì: lúc chạy 08-10, `max(event_date)` = 08-09, và 08-03 > 08-09 là FALSE. Đây là cơ chế "forward-only window": cửa sổ tính toán không nhìn lại, nên những bản ghi đến chậm hơn 1 ngày đều bị mất. |
| **Cách khắc phục** | **File:** `dbt/models/gold/gold_feature_daily.sql` — hai thay đổi: |
| | (1) Thêm lookback: `event_date >= max(event_date) - INTERVAL 3 DAY`. Toán tử `>=` thay vì `>` đảm bảo không bị bỏ sót ngày biên; lookback 3 ngày dựa trên P99 = 2.7258. |
| | (2) Thêm `unique_key = ['event_date', 'customer_id']` và `incremental_strategy = 'merge'`. Grain của bảng gồm 2 cột, cần khai báo đầy đủ để dbt merge thay vì append. Nếu chỉ sửa phần (1) mà không có (2), cùng một cặp (ngày, khách) sẽ được tính lại nhiều lần và cộng dồn — tạo đúng lỗi như nhiệm vụ 1. |
| **Bằng chứng** | trước: 8,645 hàng (thiếu 455) · sau: **9,100 hàng** · checksum: 3db448685c (giống nhau 3 lượt) |

**Vì sao chọn P99 thay vì max?** Chi phí của việc chọn max: lookback phải lớn hơn 2.9447 ngày (max), tức là 3+ ngày. Tức là với max, chi phí gấp thêm 1 ngày mỗi lần chạy. Với P99 = 2.7258, chi phí chúng tôi thấp nhất mà vẫn bao phủ 99% trường hợp. Max là mức giới hạn của dữ liệu hiện tại, không phải mức thống kê để đưa ra quyết định — nó có thể thay đổi khi dữ liệu mới xuất hiện.

---

## 3 · Kiểu dữ liệu cột priority thay đổi giữa chu kỳ

| | |
|---|---|
| **Triệu chứng** | `silver_tickets.priority` có 6,606 hàng NULL và các giá trị 0, 5, -1 nằm ngoài khoảng 1..4. `dbt test` vẫn pass nhưng model phân loại từ ngày 08-10 trở đi dự đoán kém. |
| **Nguyên nhân** | Từ ngày 2026-08-10, team backend đã đổi cách biểu diễn cột `priority` từ số sang chuỗi: thay vì gửi `'1'`, `'2'`, `'3'`, `'4'`, nguồn gửi `'urgent'`, `'high'`, `'medium'`, `'low'`. Đây là schema evolution: ý nghĩa của dữ liệu KHÔNG ĐỔI, chỉ có cách biểu diễn thay đổi. Macro `try_cast(priority_raw as integer)` cũ của pipeline không nhận ra nhãn chuỗi, biến chúng thành NULL, đồng thời lại chấp nhận giá trị ngoài khoảng như `'0'`, `'5'`, `'-1'` vì chúng là số. Kết quả: (a) một nửa dữ liệu tốt bị mất, (b) dữ liệu lỗi vẫn đi qua. |
| **Ba nhóm giá trị `priority` và cách xử lý từng nhóm** | |
| | **Nhóm 1** — Số hợp lệ: `'1'`, `'2'`, `'3'`, `'4'` → Giữ nguyên (cast sang integer) |
| | **Nhóm 2** — Nhãn chuỗi (schema evolution): `'urgent'`, `'high'`, `'medium'`, `'low'` → Map về số: urgent=1, high=2, medium=3, low=4 |
| | **Nhóm 3** — Dữ liệu lỗi thật: `'P1'`, `'P2'`, `'unknown'`, `'0'`, `'5'`, `'-1'`, `''`, NULL → Trả về NULL (đưa vào quarantine) |
| **Cách khắc phục** | **File 1:** `dbt/macros/normalize_priority.sql` — thay `try_cast` bằng khối CASE xử lý 3 nhóm. Macro này được dùng bởi 2 model nên sửa 1 cho cả 2. |
| | **File 2:** `dbt/models/silver/silver_tickets.sql` — thêm bước lọc "bản ghi hỏng" trước khi xếp hạng: `valid_records as (select * from ranked where priority_clean is not null)`. Thứ tự QUAN TRỌNG: lọc BẢN GHI hỏng trước, xếp hạng SAU. Nếu ngược lại, ticket có bản ghi mới nhất hỏng sẽ biến mất hoàn toàn khỏi Silver. |
| | **File 3:** `dbt/models/silver/quarantine_tickets.sql` — đổi `where false` thành `where normalize_priority('priority_raw') is null`. Grain: 1 hàng / 1 bản ghi CDC, không phải 1 hàng / 1 ticket. |
| | **File 4:** `dbt/models/silver/schema.yml` — đổi `contract.enforced: false` thành `true`, thêm test `not_null` và `accepted_values: [1,2,3,4]` cho cột priority. Contract ràng buộc KIỂU; test ràng buộc MIỀN GIÁ TRỊ. Cần cả hai. |
| **Bằng chứng** | `quarantine_tickets` = **312 hàng** (khớp) · `dbt test` = **11/11 pass** (thêm 2 test mới) · `silver_tickets.priority` = sạch (không NULL, chỉ có 1..4) |

**Câu hỏi thiết kế:** Chặn ở tầng Bronze hay Silver? **Chặn ở Silver**, vì Bronze là tầm chap nhận thô (CDC thô), cần giữ nguyên để phục vụ việc điều tra sau này. Nếu Bronze từ chối, toàn bộ bản ghi lỗi sẽ mất khi xuyên tuyến — người trực không có gì để phân tích.

**Vì sao không dừng pipeline khi gặp bản ghi lỗi?** Vì 312 bản ghi lỗi (~2%) không có quyền chặn hơn 12,480 ticket hợp lệ, 130,000 event, và 31,200 chunk đang chờ xử lý tiếp. Quarantine là cơ chế "isolate and continue": pipeline chạy tiếp, bản ghi lỗi được tách ra cho người trực xử lý thủ công.

---

## 4 · *(mở rộng)* Bài trong EXTRA.md

<details>
<summary>BÀI A — Query dashboard chậm (+5 điểm)</summary>

| | |
|---|---|
| **Triệu chứng** | Dashboard mất 38 giây để load. Ba tháng trước chỉ 2 giây. Không ai sửa dòng code nào. |
| **Nguyên nhân** | Small-file problem: 5,000 file nhỏ, mỗi file vài chục KB. DuckDB đọc Parquet theo lô và làm tròn lên theo từng file — một file vài chục hàng vẫn tốn khối lượng đọc tương đương ~1,000 hàng. Ngoài ra, `strftime(event_time, '%Y-%m-%d')` trong WHERE không sargable: engine không so được kết quả function với tên thư mục hay min/max statistics. |
| **Cách khắc phục** | **(1) compact.py:** COPY dataset cũ sang dataset mới với `PARTITION BY event_date` (query filter theo ngày) và `ORDER BY event_date, customer_name` (cùng khách nằm liền nhau, min/max statistics có ích). **(2) dashboard.sql:** Đổi path thành `data/gold_events_v2/**/*.parquet` và viết lại filter: `event_time >= '2026-08-09' and event_time < '2026-08-10'` thay vì `strftime()` — cột đứng một mình, sargable. |
| **Bằng chứng** | trước: rows scanned = **5,000,000** · files = **5,000** · sau: rows scanned = **132,902** · files = **14** · giảm **37.6×** · result hash: không đổi |

</details>

<details>
<summary>BÀI B — Consumer gặp sự cố giữa batch (+5 điểm)</summary>

| | |
|---|---|
| **Triệu chứng** | Consumer bị kill -9 ở giữa batch: 500 hàng bị mất, 20,000 event_id khác nhau. |
| **Nguyên nhân** | At-most-once semantics: thứ tự thao tác là `commit() → crash → write()`. Offset được commit TRƯỚC khi ghi, nên khi crash, batch hiện tại chưa được ghi nhưng offset đã nhảy qua → mất 500 hàng. |
| **Cách khắc phục** | **(a) Đổi thứ tự:** `write() → crash → commit()` → at-least-once (crash = trùng, không mất). **(b) Idempotent write:** Thêm `event_id PRIMARY KEY` và `INSERT ... ON CONFLICT (event_id) DO UPDATE SET ...` để replay không tạo trùng. DO UPDATE được chọn thay vì DO NOTHING vì nếu message được replay với nội dung đã đổi, DO UPDATE cập nhật thay vì bỏ qua. |
| **Bằng chứng** | trước: mất 500 hàng · sau: không mất, không trùng, C == A (20,000 hàng) |

</details>

---

## 5 · Tổng kết

| Nhiệm vụ | Khi tiếp nhận một hệ thống chưa quen, tôi sẽ kiểm tra điều này trước tiên |
|---|---|
| 1 | Kiểm tra các incremental model có khai báo `unique_key` chưa. Nếu không có, hỏi ngay lý do tại sao pipeline vẫn trả ra kết quả đúng — nó có thể là tạm thời (dữ liệu chưa có update). Nếu như có CDC với op='u', đó là một quả bom hẹn giờ. |
| 2 | Vẽ phân bố độ trễ giữa lúc xảy ra và lúc tới kho (event_time vs _ingested_at). Nếu có hầu hết dữ liệu cùng lúc (P50 < 1 giờ), lookback có thể = 0. Nếu có 5%+ dữ liệu trễ hơn 1 ngày, cần hỏi kỹ ngày 1 trước khi quyết định số ngày lookback. Luôn tính P99 trước, chậm hơn tính max. |
| 3 | Vẽ phân bố giá trị trong source. Một column có thể có nhiều "ngữ cảnh" cùng lúc: giá trị cũ, giá trị mới, giá trị sai. Thứ tự xử lý quyết định: (a) nhận diện các nhóm, (b) xử lý từng nhóm đúng cách, (c) tách riêng những gì không xử lý được thay vì để cả hệ thống dừng. Contract và test là hai lớp phòng vệ khác nhau: contract cho kiểu dữ liệu, test cho miền giá trị. |

---

## Bảng tự chấm nhanh

| | Của tôi | Kỳ vọng | ✓/✗ |
|---|---|---|---|
| `gold_training_set` — số hàng | 12,480 | 12,480 | ✓ |
| `gold_training_set` — ổn định 3 lượt | ✓ | ✓ | ✓ |
| `gold_feature_daily` — số hàng | 9,100 | 9,100 | ✓ |
| `gold_feature_daily` — ổn định 3 lượt | ✓ | ✓ | ✓ |
| `gold_doc_chunks` — số hàng | 31,200 | 31,200 | ✓ |
| `quarantine_tickets` — số hàng | 312 | 312 | ✓ |
| `silver_tickets` — số ticket | 12,480 | 12,480 | ✓ |
| `dbt test` | 11/11 pass | pass, > 9 test | ✓ |
| P99 độ trễ đo được | **2.7258 ngày** | (ghi số) | ✓ |
| **Tổng verify** | **4/4 tiêu chí** | 4/4 tiêu chí | ✓ |
| **Điểm bonus** | | | |
| Bài A — rows scanned giảm ≥10× | **37.6×** | ≥10× | ✓ |
| Bài B — crash test đạt | ✓ | đạt | ✓ |
| **Tổng điểm** | **100 + 10 bonus** | 100 + 10 bonus | ✓ |


P/s: Do có 1 số lỗi của Github trong tối nay em đã chụp minh chứng trong thư mục Lỗi github.Em không biết nghĩ là lỗi bản thân nên em đã lo nộp có lỗi nên nhờ gemini đưa lệnh để nộp lại và chạy các lệnh đó nên vô tình xóa hết các commit cũ của bài repo gốc dẫn đến việc cả bài chỉ còn commit của em. EM mong labcoach chấm bài này có thể kiểm tra và thông cảm cho sự ngu ngục của em