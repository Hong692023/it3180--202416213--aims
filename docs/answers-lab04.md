# Lab 04 - Câu hỏi thảo luận

## 1. Vì sao release/* không merge ngược vào master?
Release là baseline đóng băng. Master tiếp tục phát triển tính năng mới,
còn release chỉ nhận bản vá (hotfix). Merge ngược sẽ kéo cả commit chuẩn
bị phát hành và các bản vá riêng của nhánh đó vào master, gây xung đột
và làm lịch sử lẫn lộn. Bản sửa lỗi được cherry-pick sang master.

## 2. So sánh với GitFlow
GitFlow dùng develop và main, release/* được merge vào cả hai. Release
Flow của học phần chỉ có master làm trục chính, release/* tách ra từ
master và không bao giờ quay lại, nên đơn giản hơn, hợp với nhiều bản
phát hành song song.

## 3. Vì sao lên 1.0.0 mà không phải 0.4.0?
Từ lab 04 sản phẩm có đủ tính năng, có test và quy trình phát hành, được
coi là ổn định để giao cho người dùng. SemVer dành 0.y.z cho giai đoạn
chưa ổn định, nên mốc phát hành đầu tiên là 1.0.0.