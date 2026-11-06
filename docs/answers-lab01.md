# Lab 01 - Câu hỏi thảo luận

## 1. Cấu hình --global được lưu ở đâu? Khác gì --local?
--global lưu trong tệp ~/.gitconfig của người dùng, áp dụng cho mọi repo
trên máy. --local lưu trong .git/config của từng repo, chỉ áp dụng cho repo
đó và ghi đè --global khi trùng khóa.

## 2. Vì sao dùng git mv?
git mv đổi tên và đưa thay đổi vào staging cùng lúc, giúp Git nhận diện là
rename (similarity 100%) nên git log --follow giữ được lịch sử tệp.

## 3. release/lab01 có phải baseline không?
Có. Đó là phiên bản đã thống nhất, được đóng băng và chỉ thay đổi qua quy
trình (PR, hotfix), dùng để nộp bài.

## 4. Vì sao không commit thẳng master dù làm một mình?
Để mọi thay đổi đều qua PR: có điểm review, có lịch sử truy vết, có thể
revert theo từng PR và tập thói quen đúng quy trình SCM.
