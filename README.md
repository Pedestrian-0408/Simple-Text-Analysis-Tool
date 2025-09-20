# Simple Text Analysis Tool

Một công cụ đơn giản để phân tích văn bản. Dự án bao gồm việc đếm từ, ký tự, và các phân tích cơ bản khác.

---

## ✨ Mục lục

- [Giới thiệu](#giới-thiệu)  
- [Tính năng](#tính-năng)  
- [Yêu cầu](#yêu-cầu)  
- [Cài đặt & sử dụng](#cài-đặt--sử-dụng)  
- [Cấu trúc dự án](#cấu-trúc-dự-án)  
- [Ví dụ](#ví-dụ)  
- [Đóng góp](#đóng-góp)  
- [Bản quyền](#bản-quyền)

---

## Giới thiệu

`Simple-Text-Analysis-Tool` là một chương trình viết bằng Python để thực hiện các phân tích cơ bản trên văn bản, như:

- Đếm số từ  
- Đếm số ký tự  
- Các phân tích thống kê đơn giản khác của văn bản đầu vào  

---

## Tính năng

- Đọc từ file hoặc từ input người dùng  
- Xử lý văn bản cơ bản (loại bỏ ký tự đặc biệt, phân tách từ, v.v.)  
- Trả về các chỉ số như: tổng số từ, tổng số ký tự, từ dài nhất, từ ngắn nhất, và các thông số hữu ích khác  

---

## Yêu cầu

- Python 3.x  
- Các thư viện phụ thuộc được liệt kê trong `requirements.txt`

---

## Cài đặt & sử dụng

1. Clone repo:

   ```bash
   git clone https://github.com/Pedestrian-0408/Simple-Text-Analysis-Tool.git
   cd Simple-Text-Analysis-Tool
   ```

2. Tạo môi trường ảo (khuyến khích):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # trên Linux/macOS
   # hoặc
   venv\Scripts\activate      # trên Windows
   ```

3. Cài đặt các gói cần thiết:

   ```bash
   pip install -r requirements.txt
   ```

4. Chạy chương trình:

   ```bash
   python main.py
   ```

   Chương trình sẽ yêu cầu bạn nhập văn bản hoặc đường dẫn tới file để phân tích.

---

## Cấu trúc dự án

```
Simple-Text-Analysis-Tool/
├── main.py
├── requirements.txt
└── README.md
```

- `main.py`: tệp chứa code chính thực hiện phân tích văn bản  
- `requirements.txt`: liệt kê các thư viện cần cài đặt  

---

## Ví dụ

Giả sử bạn có file `sample.txt` chứa:

```
Hello world! This is a test.
```

Chạy:

```bash
python main.py sample.txt
```

Kết quả có thể là:

```
Số ký tự: 29
Số từ: 6
Từ dài nhất: "Hello" (5 ký tự)
Từ ngắn nhất: "a" (1 ký tự)
```

---
