import os, subprocess
ALBUM_PATH = "/storage/emulated/0/DCIM/Camera/"
def main():
    video_in = input("请输入源视频名: ").strip()
    if not os.path.exists(video_in): return
    output = "STORE_" + video_in
    subprocess.run(f"ffmpeg -i '{video_in}' -c:v libx264 -pix_fmt yuv420p -y '{output}'", shell=True)
    if os.path.exists(ALBUM_PATH):
        target = os.path.join(ALBUM_PATH, output)
        subprocess.run(f"cp '{output}' '{target}'", shell=True)
        subprocess.run(f"am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file://{target}", shell=True)
        print("✅ 已同步至相册")
if __name__ == "__main__":
    main()
