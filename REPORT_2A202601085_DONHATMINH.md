# Báo cáo LAB 17 — Data Pipeline Engineering

**Họ tên:** Đỗ Nhật Minh  **Lớp:** AICB-P2T2  **Ngày:** 2026-08-17

---

## 0 · Kết quả `make verify` - 3 giai đoạn sửa lỗi

### Giai đoạn 1 - Sau khi sửa bài 1

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
gold_feature_daily    ✓ ok               8,645       9,100   ✗ thiếu 455 hàng
gold_doc_chunks       ✓ ok              31,200      31,200   ✓
quarantine_tickets    ✓ ok                   0         312   ✗ thiếu 312 hàng

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

Tổng kết: 1 / 4 tiêu chí đạt
```

**Tình trạng:** gold_training_set đạt. Feature thiếu 455 hàng, priority 6,606 sai, quarantine rỗng.

---

### Giai đoạn 2 - Sau khi sửa bài 2

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
quarantine_tickets    ✓ ok                   0         312   ✗ thiếu 312 hàng

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

Tổng kết: 2 / 4 tiêu chí đạt
```

**Tình trạng:** Feature daily đạt 9,100 hàng. Nhưng priority vẫn 6,606 sai, quarantine vẫn rỗng.

---

### Giai đoạn 3 - Hoàn tất sau bài 3

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

Tổng kết: 4 / 4 tiêu chí đạt
```

**Tình trạng:** Tất cả 4/4 tiêu chí đạt.

---

### Giai đoạn 4 - Bài mở rộng (Extra)

#### Bước 1: `make seed-extra` - tạo dữ liệu 5.000 file

```
[seed] dựng bảng nguồn…
[seed] ticket: 12735 tạo / 255 xoá / 12480 sống / 998 sửa / 312 sai kiểu
[seed] ghi seed/tickets_cdc.jsonl…
[seed] ghi seed/events.jsonl…
[seed] ghi seed/transcripts.jsonl…
[seed] ghi data/gold_events/ (5000 file nhỏ)…

CDC rows        :    14,300
events          :   130,683
transcripts     :     5,200
parquet files   :     5,000
expected/       : {"gold_training_set": 12480, "gold_feature_daily": 9100, "gold_doc_chunks": 31200, "quarantine_tickets": 312}
xong sau 28.6s
```

#### Bước 2: Baseline `make explain`

```
queries/dashboard.sql
--------------------------------------------------------------
                             TRƯỚC        HIỆN TẠI      MỤC TIÊU
rows scanned           5,000,000       5,000,000     ≤ 500,000   ✗
rows on disk             130,683         130,683   (tham khảo)
files                      5,000           5,000        ít hơn   ✗
result hash         4379e4c5d9f3    4379e4c5d9f3     không đổi   ✓
thời gian (ms)                 —        45,117.4   (tham khảo)

=> giảm 1.0× (cần ≥ 10×)
```

#### Bước 3: `make compact` - tái cấu trúc Parquet

```
nguồn : data/gold_events  (5,000 file)
rows   : 130,683
sau compact: 130,683 rows
file mới : 14

Đã ghi dataset mới vào data/gold_events_v2/
```

#### Bước 4: `make explain` sau khi compact + sửa dashboard.sql

```
queries/dashboard.sql
--------------------------------------------------------------
                             TRƯỚC        HIỆN TẠI      MỤC TIÊU
rows scanned           5,000,000         132,902     ≤ 500,000   ✓
rows on disk             130,683         130,683   (tham khảo)
files                      5,000              14        ít hơn   ✓
result hash         4379e4c5d9f3    4379e4c5d9f3     không đổi   ✓
thời gian (ms)                 —            12.0   (tham khảo)

=> giảm 37.6× (cần ≥ 10×)
```

#### Bước 5: `make crash-test` - kiểm tra consumer idempotent

```
topic: 20,000 message · batch 500 · giết ở lô 7

A. chạy một mạch, không sự cố
[consumer] đã ghi 20,000 message
   -> 20,000 hàng / 20,000 event_id khác nhau

B. chạy và bị giết ở lô 7
[consumer] 💥 tiến trình bị giết ở lô 7
   -> tiến trình thoát với mã 137
   -> offset đã commit: 3,000

C. khởi động lại, chạy nốt
[consumer] đã ghi 17,000 message
   -> 20,000 hàng / 20,000 event_id khác nhau

không mất bản ghi                 ✓
không trùng bản ghi               ✓
C == A                            ✓

BÀI MỞ RỘNG B: ĐẠT ✓
```

#### Bước 6: `make verify` - xác nhận cuối cùng

```
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
dashboard rows scanned                      ✓ 5,000,000 → 132,902 (37.6×, cần ≥ 10×)
  số file parquet                           ✓ 5,000 → 14
  kết quả truy vấn không đổi                ✓
DAG: catchup / max_active_runs              ✓ False / 1

TỔNG KẾT
──────────────────────────────────────────────────────────────────────────
✓  1 · gold_training_set idempotent & đúng số hàng
✓  2 · gold_feature_daily đủ hàng (dữ liệu về muộn)
✓  3 · contract + quarantine + dbt test
✓  4 · gold_doc_chunks vẫn ổn định (đối chứng)
──────────────────────────────────────────────────────────────────────────
4/4 tiêu chí đạt
```

---

## 1 · Bảng training tăng row sau mỗi lần chạy

|                    | |
| ------------------ | --- |
| **Triệu chứng**    | `gold_training_set` tăng số hàng sau mỗi lần chạy `make pipeline`. Mỗi lần chạy thêm 12,480 hàng, 3 lần chạy có 37,440 hàng thay vì 12,480. |
| **Nguyên nhân**    | Model `gold_training_set` được khai báo `materialized = 'incremental'` nhưng **không có** `unique_key`. Khi dbt không biết khóa, nó sinh ra câu lệnh `INSERT INTO` thuần túy — mỗi bản ghi mới đều được chèn vào cuối bảng, không kiểm tra trùng lặp. Cùng một ticket_id xuất hiện ở nhiều ngày khác nhau trong lịch sử, nên mỗi lần chạy lại đều chèn thêm bản ghi cũ vào Gold. |
| **Cách khắc phục** | `dbt/models/gold/gold_training_set.sql`: thêm `unique_key = 'ticket_id'` và `incremental_strategy = 'merge'` vào `config()`. Merge theo khóa `ticket_id` đảm bảo bản ghi cũ bị ghi đè bởi bản ghi mới, không còn chèn thêm. |
| **Bằng chứng**     | Trước: row tăng sau mỗi lần chạy (12,480 → 24,960 → 37,440). Sau: 12,480 hàng, checksum 3 lượt giống nhau: `8dd7c98653`. 1 hàng / 1 ticket, không lặp. |

---

## 2 · Bảng đặc trưng theo ngày thiếu hàng ở các ngày quá khứ

|                        | |
| ---------------------- | --- |
| **Triệu chứng**        | `gold_feature_daily` có 8,645 hàng thay vì 9,100. Các cặp (event_date, customer_id) thiếu tập trung ở các ngày cũ (08-03 đến 08-13), mỗi ngày thiếu 30-48 cặp. |
| **P99 độ trễ đo được** | **2.7258 ngày** (~65 giờ) |
| **Lookback đã chọn**   | **3 ngày** — vì P99 = 2.7258, làm tròn lên 3 để đảm bảo tất cả event muộn đều được tính lại. |
| **Nguyên nhân**        | Điều kiện lọc `event_date > max(event_date)` trong khối `is_incremental()` chỉ xử lý những ngày lớn hơn ngày lớn nhất đã có trong bảng đích. Tuy nhiên, ~5% bản ghi có `_ingested_at - event_time > 1 ngày`. Một event có `event_date = 08-12` nhưng `_ingested_at = 08-15` sẽ **không được xử lý** khi run 08-15 vì `max(event_date)` của bảng đích tại thời điểm đó là `08-14`. Đến ngày 08-16 thì event 08-12 vẫn bị bỏ qua vì 08-12 < 08-14. Không có lookback, event muộn sẽ **không bao giờ được tính**. |
| **Cách khắc phục**     | `dbt/models/gold/gold_feature_daily.sql`: (1) Đổi `>` thành `>=` để tính lại những ngày vừa gặp, (2) Trừ đi 3 ngày để bắt kịp sự muộn của dữ liệu: `event_date >= (select max(event_date) from {{ this }}) - interval 3 day`. (3) Đảm bảo `unique_key = ['event_date', 'customer_id']` và `incremental_strategy = 'merge'` trong `config()` để mỗi lần tính lại **thay thế** kết quả cũ, không cộng dồn. |
| **Bằng chứng**         | Trước: 8,645 hàng. Sau: 9,100 hàng. Checksum 3 lượt giống nhau: `3db448685c`. |

**Vì sao chọn P99 thay vì `max`? Chi phí của mỗi lựa chọn là gì?**

Chọn P99 vì nó là giá trị mà 99% bản ghi đã được xử lý trong khoảng thời gian đó. Nếu dùng `max` (= 2.9447 ngày), cần lookback 3 ngày nhưng chỉ nhận được thêm 1% trong khi phải trả chi phí quét thêm 1 ngày ở mỗi lượt chạy. P99 cho một mức compromise tốt: phục vụ 99% bản ghi muộn với chi phí thêm 1 ngày lookback. Mỗi ngày lookback thêm = quét thêm 1 ngày dữ liệu nguồn ở mỗi lượt chạy, nhưng chi phí này trả một lần (ở thời điểm ban đầu) rồi giữ nguyên ở các lượt sau.

---

## 3 · Kiểu dữ liệu cột priority thay đổi giữa chu kỳ

|                                                            | |
| ---------------------------------------------------------- | --- |
| **Triệu chứng**                                            | Cột `priority` trong `silver_tickets` chứa giá trị NULL, số ngoài khoảng 1..4, và có ít nhất 6,606 hàng sai. Nguồn `bronze_tickets_cdc` gửi `priority_raw` với ba loại giá trị khác nhau. |
| **Nguyên nhân**                                            | Macro `normalize_priority` sử dụng `try_cast(priority_raw as integer)`. `try_cast` có hai lỗi: (a) Biến nhãn chuỗi (`'urgent'`, `'high'`, `'medium'`, `'low'`) thành NULL — mất dữ liệu tốt, (b) Chấp nhận giá trị số thực sự nhưng nằm ngoài khoảng 1..4 (`'0'`, `'5'`, `'-1'`) vì chúng là số hợp lệ theo kiểu. Contract không được `enforced: true`, `dbt test` chưa được bật, và `quarantine_tickets` vẫn rỗng (`WHERE false`) nên dữ liệu lỗi ngang nhiên không bị phát hiện. |
| **Ba nhóm giá trị** `priority` **và cách xử lý từng nhóm** | **(Nhóm 1)** Giá trị `'1'`, `'2'`, `'3'`, `'4'` — đúng contract cũ. Giữ nguyên. **(Nhóm 2)** Nhãn chữ `'urgent'`, `'high'`, `'medium'`, `'low'` — schema evolution: từ ngày 2026-08-10 team backend đổi cách biểu diễn, ý nghĩa không đổi. Map theo tài liệu API: urgent→1, high→2, medium→3, low→4. **(Nhóm 3)** `'P1'`, `'unknown'`, `'0'`, `'5'`, `'-1'`, `''`, `NULL` — dữ liệu hỏng thật. Trả về NULL để quarantine. |
| **Cách khắc phục**                                         | (a) `dbt/macros/normalize_priority.sql`: thay `try_cast` bằng CASE xử lý đủ 3 nhóm. (b) `dbt/models/silver/silver_tickets.sql`: **lọc bản ghi lỗi (priority NULL) TRƯỚC khi xếp hạng** — đảm bảo ticket vẫn có trạng thái hợp lệ từ lần cập nhật trước, không bị mất khi bản ghi mới nhất hỏng. (c) `dbt/models/silver/quarantine_tickets.sql`: thay `where false` bằng `where normalize_priority(priority_raw) is null`. (d) `dbt/models/silver/schema.yml`: bật `contract.enforced: true` và thêm `accepted_values` test `[1, 2, 3, 4]` cho cột priority. |
| **Bằng chứng**                                             | `quarantine_tickets` = 312 hàng. `dbt test` = 11/11 pass (tăng từ 9). `silver_tickets.priority` sạch, không NULL, nằm trong 1..4. `silver_tickets` giữ nguyên 12,480 ticket (loại bản ghi hỏng, không loại ticket). |

**Câu hỏi thiết kế: nên chặn ở tầng Bronze hay Silver? Vì sao không để pipeline dừng khi gặp bản ghi lỗi?**

Chặn ở **Silver** thay vì Bronze. Bronze giữ lại trạng thái thô của dữ liệu, cho phép người trực điều tra nguyên nhân gốc khi sự cố xảy ra. Nếu chặn ở Bronze, người trực mất khả năng trace về nguồn — không biết dữ liệu đã đến từ đâu, được gửi khi nào, có bị thay đổi giữa đường không. Silver là nơi dữ liệu đã được làm sạch, phân biệt rõ ràng giữa lỗi thật (không thể map) và schema evolution (map được nhưng cần chuẩn hóa), phù hợp để chèn ngưỡng.

**Không dừng pipeline** khi gặp bản ghi lỗi vì tỷ lệ lỗi rất nhỏ: 312 bản ghi lỗi trên tổng 12,735 tạo + 998 sửa = 13,733 bản ghi CDC, chỉ khoảng 2.3%. Khoảng 130,000 event và 31,200 chunk hoàn toàn bình thường vẫn đang chờ. Quarantine tách riêng các bản ghi lỗi làm một hàng đợi cho người trực xử lý thủ công, trong khi pipeline vẫn phục vụ người dùng. Dừng toàn bộ DAG cho 0.2% lỗi là chi phí quá lớn.

---

## 4 · Query dashboard chậm *(Bài A - Mở rộng, +5 điểm)*

### Triệu chứng

Dashboard mất 38 giây load, trước đó 2 giây. Không ai sửa code.

### Root cause

- **Small-file problem**: 5,000 file nhỏ (~26 rows/file) → mỗi file tốn khối lượng đọc ~1,000 rows
- `strftime(event_time, '%Y-%m-%d')` **không sargable**: cột bị bọc hàm → engine không so được với min/max statistics của row group
- Không partition theo date → phải đọc toàn bộ 130,683 rows dù chỉ cần 1 ngày

### Ba quyết định trong `tools/compact.py`

| Quyết định         | Lựa chọn                    | Lý do |
| ------------------ | --------------------------- | ----- |
| **Cột partition**  | `event_date`                | Dashboard filter theo ngày, chỉ 14 giá trị → 14 thư mục. Filter theo customer không hợp lý (650 thư mục, mỗi thư mục chỉ ~200 rows, overhead lớn) |
| **ORDER BY**       | `event_date, customer_name` | Các hàng cùng customer trong cùng ngày nằm liền nhau, tối ưu min/max statistics của row group |
| **ROW_GROUP_SIZE** | Mặc định (122,880)          | Mỗi partition ~9,300 rows ≈ mặc định, không cần thay đổi |

### Sửa `queries/dashboard.sql`

- Đổi path: `data/gold_events/*.parquet` → `data/gold_events_v2/**/*.parquet`
- Đổi filter: `strftime(event_time, '%Y-%m-%d') = '2026-08-09'` → `event_time >= '2026-08-09' and event_time < '2026-08-10'` (sargable)

### Kết quả

```
                          TRƯỚC        SAU          MỤC TIÊU
rows scanned           5,000,000         132,902     ≤ 500,000   ✓
files                      5,000              14        ít hơn   ✓
result hash         4379e4c5d9f3    4379e4c5d9f3   không đổi   ✓
thời gian (ms)               —              12.0

=> giảm 37.6×
```

**37.6 lần** giảm rows scanned, **thời gian giảm từ ~45,117ms xuống 12ms** (~3,759×), hash không đổi → kết quả query y hệt.

---

## 5 · Consumer gặp sự cố giữa batch *(Bài B - Mở rộng, +5 điểm)*

### Triệu chứng

Consumer bị `kill -9` ở lô thứ 7 trong 20 lô × 500 message. Sau khi restart, mất bản ghi hay bị trùng?

### Phân tích - At-most-once (trước khi sửa)

```
consumer.commit()          # (1) commit offset TRƯỚC
maybe_crash(batch_no)      # (2) crash tại đây
write_batch(con, batch)   # (3) ghi dữ liệu - CHƯA chạy
```

Khi crash: offset đã dịch → lần restart bỏ qua 6 lô đầu → **mất dữ liệu** (at-most-once).

### Sửa (a) - Đổi thứ tự → At-least-once

```
write_batch(con, batch)   # (1) ghi TRƯỚC
consumer.commit()          # (2) commit SAU
maybe_crash(batch_no)      # (3) crash
```

Crash ở lô 7: offset chưa dịch → lần restart đọc lại từ lô 7 → **trùng dữ liệu** (at-least-once).

### Sửa (b) - INSERT idempotent với DO UPDATE

Với `ON CONFLICT DO NOTHING`: nếu message được replay với nội dung **đã đổi**, dữ liệu cũ bị giữ nguyên → **sai**.

Với `ON CONFLICT DO UPDATE`: nếu message được replay, dữ liệu được **cập nhật** → luôn đúng với bản mới nhất.

Chọn **DO UPDATE** vì đảm bảo khi message được phát lại với nội dung mới, dữ liệu trong DB phản ánh phiên bản mới nhất.

Cần thêm `PRIMARY KEY` vào `event_id` để DuckDB chấp nhận `ON CONFLICT`.

### Kết quả crash-test

```
A. chạy một mạch, không sự cố
   -> 20,000 hàng / 20,000 event_id khác nhau

B. chạy và bị giết ở lô 7
   -> tiến trình thoát với mã 137
   -> offset đã commit: 3,000

C. khởi động lại, chạy nốt
   -> 20,000 hàng / 20,000 event_id khác nhau

không mất bản ghi                 ✓
không trùng bản ghi               ✓
C == A                            ✓

BÀI MỞ RỘNG B: ĐẠT ✓
```

---

## 6 · Tổng kết

| Nhiệm vụ | Khi tiếp nhận một hệ thống chưa quen, tôi sẽ kiểm tra điều này trước tiên |
| -------- | --- |
| 1        | Kiểm tra `config()` của mọi incremental model: có `unique_key` chưa? Có `incremental_strategy` chưa? Nếu thiếu, hỏi người thiết kế xem họ có chắn không. Incremental mà không có khóa là một phantom - chạy đúng nhưng tạo ra duplicate mà không ai hay. |
| 2        | Với dữ liệu CDC, luôn đo phân bố độ trễ giữa lúc tạo và lúc đến warehouse. Nếu có dữ liệu đến muộn (trễ > 0), phải có lookback window trong mọi incremental model đọc từ bảng đó. Nếu không có, các bản ghi muộn sẽ bị mất vĩnh viễn khi gặp đầu tiên của ngày lớn hơn. |
| 3        | Kiểm tra contract trên cột quan trọng (enum, range, not null). Nếu `enforced: false` thì dữ liệu có thể mang bất cứ giá trị nào, và lỗi chỉ được phát hiện khi người dùng gặp. Đặt `enforced: true` bắt buộc người đưa dữ liệu phải tuân thủ contract. Đồng thời, xử lý nhóm lỗi nhỏ bằng quarantine thay vì dừng pipeline - tránh làm chết toàn bộ hệ thống vì 0.2% dữ liệu hỏng. |
| 4 (A)    | Parquet trên đĩa không có index. File nằm ở đâu và hàng nằm theo thứ tự nào trong file mới là thứ duy nhất ta điều khiển được. Partition theo date (14 giá trị) để engine bỏ qua 13/14 file trước khi mở bất kỳ file nào. Filter phải sargable (cột đứng một mình, không bọc hàm) để engine dùng được min/max statistics. |
| 5 (B)    | Với consumer message queue, luôn chọn at-least-once (ghi trước, commit sau) vì nó không mất dữ liệu. Kết hợp với INSERT idempotent (ON CONFLICT DO UPDATE) để tránh trùng khi message được replay. Exactly-once không tồn tại ở tầng transport; chọn at-least-once + idempotent là pattern chuẩn. |

---

## 7 · Bảng tự chấm nhanh (theo RUBRIC.md)

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
| Dashboard rows scanned | 5,000,000 → 132,902 (37.6×) | ≥10× | ✓ |

### Điểm tổng kết

| Hạng mục | Điểm đạt | Tối đa |
|----------|----------|--------|
| A. Tính ổn định | 30 | 30 |
| B. Tính đúng | 30 | 30 |
| C. Chất lượng dữ liệu | 20 | 20 |
| D. Báo cáo | 20 | 20 |
| + Thưởng EXTRA A + B | +10 | +10 |
| **TỔNG** | **110** | 100 |
