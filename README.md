# 💎 Termux-to-Gallery | 安卓相册一键保存工具

> **解决痛点**：专门解决 Termux 下载的视频在相册里“隐身”的问题。一键迁移，瞬间入库。

---

### 🛠️ 傻瓜式操作流程 (新手必看)

**第一步：复制下方指令并在 Termux 中运行 (环境一键配置)**
```bash
pkg update && pkg install python ffmpeg git -y && termux-setup-storage

```
*(弹出授权提示时，请务必点击“允许”)*
**第二步：下载并运行工具**
```bash
git clone [https://github.com/maomaoati-coder/Termux-to-Gallery.git](https://github.com/maomaoati-coder/Termux-to-Gallery.git)
cd Termux-to-Gallery && python sync_to_gallery.py

```
*按提示输入文件名，完成后直接打开手机相册即可！*

### ☕ 技术支持与打赏
如果你觉得这个小工具帮你节省了找视频的时间，欢迎支持作者持续维护。

#### 💎 **[👉 点击此处 (打赏 2.9 元)](wechat_pay.jpg)**
---
### 📂 关联仓库 (各自对位跳转)
 * TrustFlow-Zenith-01 - 芯片逻辑验证
 * UI-Gallery - 界面增强版同步工具
**Powered by maomaoati-coder** | 追求极致的移动端开发效率
```

