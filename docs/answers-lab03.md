# Lab 03 - Câu hỏi thảo luận

## 1. Merge base là gì?
Merge base là commit tổ tiên chung gần nhất của hai nhánh. Git dùng nó
làm điểm so sánh (ba chiều: base, nhánh A, nhánh B) để biết mỗi bên đã
thay đổi gì. Cả hai cùng sửa một dòng so với merge base thì xung đột.

## 2. Vì sao master/release/* phải dùng revert?
reset viết lại lịch sử (dời con trỏ nhánh), làm lệch với bản người khác
đã kéo về và buộc phải force push. revert tạo commit đảo ngược mới nên
lịch sử vẫn nguyên vẹn, an toàn cho nhánh dùng chung.

## Ghi chú
- Ở Windows, print tiếng Việt gây UnicodeEncodeError (cp1252). Khắc phục
  bằng PYTHONUTF8=1. Chạy trên Linux/macOS không bị.
- Khi giải xung đột, cần chạy test trước khi commit (đã gặp lỗi do
  không làm vậy ở PR #16/#17).
- Làm một mình nên Required approvals = 0.