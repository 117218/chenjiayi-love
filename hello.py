import tkinter as tk
import math

# 设置窗口参数
WIDTH, HEIGHT = 900, 700
CENTER_X, CENTER_Y = WIDTH / 2, HEIGHT / 2

def heart(t, scale=10):
    """数学公式生成爱心坐标"""
    x = 16 * (math.sin(t) ** 3)
    y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
    return int(x * scale + CENTER_X), int(y * scale + CENTER_Y)

def main():
    # 1. 创建主窗口
    win = tk.Tk()
    win.title("💕 情人节快乐 💕")
    win.resizable(False, False)
    
    # 2. 创建画布
    canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT, bg="#1a0a1a", highlightthickness=0)
    canvas.pack()
    
    # 3. 画一个最简单的爱心（测试用）
    points = []
    for i in range(100):
        t = i / 100 * math.pi * 2
        x, y = heart(t)
        points.extend([x, y])
    canvas.create_polygon(points, fill="#FF69B4", outline="")
    
    # 4. 在爱心正中间写“陈佳奕”
    canvas.create_text(
        CENTER_X, CENTER_Y,
        text="陈佳奕",
        fill="white",  # 白色文字，在粉色爱心上清晰可见
        font=("Microsoft YaHei", 36, "bold"),  # 字体大小可调
        anchor="center"  # 居中对齐
    )
    
    # 5. 保持窗口打开
    win.mainloop()

if __name__ == "__main__":
    main()