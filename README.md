# 💎 Termux-to-Gallery | 安卓相册强同步专家

> **Origin Determinism (源头决定论)**：解决移动端开发中最后 1 厘米的系统刷新鸿沟。

### 🌟 为什么选择本项目？
在 Termux 环境下处理视频，最痛苦的是生成的视频在系统相册中“不可见”。本项目通过底层广播协议实现：
* **物理层对位**：精准定位 Android DCIM 核心簇，确保文件物理入库。
* **即时刷新**：内置 ASR 媒体扫描广播，无需重启，相册秒出成品。
* **高质量渲染**：默认 libx264 兼容性压制，画质超清且预览不花屏。

---

### 🛠️ 傻瓜式操作流程

1. **环境初始化 (仅需一次)**
   ```bash
   pkg update && pkg install python ffmpeg -y
   termux-setup-storage
