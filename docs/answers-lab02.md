# Lab 02 - Câu hỏi thảo luận

## 1. Vì sao phải đồng bộ master trước khi PR?
Để phát hiện xung đột và lỗi tích hợp ngay trên nhánh của mình, trước khi
vào master. Nhánh tạo từ master cũ có thể thiếu thay đổi của người khác.

## 2. Khi nào không được rebase?
Khi commit đã được push và người khác đang dùng chung nhánh. Rebase viết
lại lịch sử (SHA mới) nên làm hỏng nhánh của người khác.

## 3. feature/* khác topic/* ra sao?
feature/* thêm tính năng cho sản phẩm (cart-print, search-by-title).
topic/* là thay đổi theo chủ đề, không phải tính năng: tài liệu,
cấu hình (pr-template, use-case-diagram).

## Ghi chú
Làm một mình nên Required approvals = 0 và bước review chỉ dùng được
"Comment" (tác giả không tự Request changes được PR của mình). Vẫn
bắt buộc đi qua PR.