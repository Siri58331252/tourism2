# ฟีเจอร์ส่งออกข้อมูล (Export Features)

## ความสามารถ

ผู้ดูแลระบบสามารถส่งออกประวัติการใช้งานระบบในรูปแบบ 3 ประเภท:

### 1. **CSV Export** 📊

- ไฟล์: `system_logs_[วันที่].csv`
- ได้แก่: วันเวลา, ผู้ใช้, การทำงาน, รายละเอียด, IP Address
- เข้าได้ใน Excel, Google Sheets, หรือทุก Spreadsheet แอปพลิเคชัน
- **Route**: `/moderator/logs/export-csv?days=7&action=`

### 2. **Excel Export** 📈

- ไฟล์: `system_logs_[วันที่].xlsx`
- ฟีเจอร์:
  - ส่วนหัวสีฟ้า
  - เส้นขอบในทุกเซลล์
  - ความกว้างของคอลัมน์อัตโนมัติ
  - สลับสีแถว (ขาว-เทา) เพื่อให้อ่านง่าย
- **Route**: `/moderator/logs/export-excel?days=7&action=`

### 3. **PDF Export** 📄

- ไฟล์: `system_logs_[วันที่].pdf`
- ฟีเจอร์:
  - ชื่อเอกสารแสดงช่วงเวลา
  - ตารางแบบแนวนอน (landscape)
  - จำกัด 100 แถวแรกเพื่อให้ PDF ไม่ใหญ่เกินไป
  - สีส่วนหัวและเส้นขอบ
- **Route**: `/moderator/logs/export-pdf?days=7&action=`

## การใช้งาน

1. เข้าไป **"ประวัติการใช้งาน"** ในแดชบอร์ดผู้ดูแล
2. เลือกช่วงเวลา (1, 7, 30, 90 วัน)
3. เลือกประเภทการทำงาน (ตัวเลือก)
4. คลิกปุ่ม **"CSV"**, **"Excel"**, หรือ **"PDF"**
5. ไฟล์จะดาวน์โหลดโดยอัตโนมัติ

## ตัวอย่าง URL

```
# CSV
http://127.0.0.1:5000/moderator/logs/export-csv?days=7&action=login

# Excel
http://127.0.0.1:5000/moderator/logs/export-excel?days=30

# PDF
http://127.0.0.1:5000/moderator/logs/export-pdf?days=90&action=
```

## เทคโนโลยี

- **CSV**: Python `csv` module
- **Excel**: `openpyxl` library
- **PDF**: `reportlab` library

## หมายเหตุ

- การกรองตามช่วงเวลาและประเภทจะนำไปใช้ต่อแฟ้มที่ส่งออก
- ชื่อไฟล์รวมวันเวลาปัจจุบัน เพื่อหลีกเลี่ยงการทับซ้อน
- ระบบตรวจสอบสิทธิ์ (moderator role) สำหรับทุกไฟล์ที่ส่งออก
