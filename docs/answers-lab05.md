# Lab 05 - Câu hỏi thảo luận

## 1. Ưu, nhược điểm của upstream first so với release first?
Upstream first (sửa ở master rồi cherry-pick vào release) bảo đảm bản sửa
không bị quên ở master, nhưng chậm đưa bản vá tới người dùng. Release first
(học phần) phát hành bản vá nhanh, nhưng dễ quên lan truyền về master.

## 2. Nếu quên lan truyền sang release/lab05 thì lệnh nào phát hiện?
git tag --contains <FIX_SHA> hoặc git log --all --grep "cherry picked from
commit <FIX_SHA>" không thấy bản sửa ở nhánh đó; git cherry -v cho dòng "+"
với commit còn thiếu; vòng lặp kiểm tra hành vi trên từng tag sẽ in 0.

## 3. Vì sao Phần A chưa gắn tag v1.1.0?
Tag đã chia sẻ không được xóa hay di chuyển. Nếu gắn rồi mà còn phải đưa
hotfix vào thì phải phát hành bản mới. Bài này đã gặp: v1.1.0 gắn trước khi
có bản sửa, v1.1.1 và v1.1.2 gắn nhầm commit do nhánh local lệch, nên bản
đúng là v1.1.3.

## Bài học
- Không dùng git pull trên release/*; dùng fetch rồi reset --hard hoặc
  pull --ff-only.
- Trước khi push tag, so git rev-parse <tag>^{commit} với origin/<nhánh>.
- git cherry cho "+" với commit fix vì bản trên master được sửa tay khi giải
  xung đột nên patch khác bản gốc.
- Làm một mình nên Required approvals = 0, mọi thay đổi vẫn qua PR.