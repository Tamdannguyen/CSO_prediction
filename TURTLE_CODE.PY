import cv2
import numpy as np
import turtle

# Đọc ảnh đen trắng
img = cv2.imread("30_4_2025.png")

red_color = img[:, :, 0]
green_color = img[:, :, 1]
blue_color = img[:, :, 2]

yellow_mask = (red_color < 150) & (green_color > 150) & (blue_color > 100) #Tạo điểm màu vàng từ 3 màu RGB

# Ngưỡng để phân biệt các màu đỏ/xanh 
_, red_thres = cv2.threshold(red_color, 150, 255, cv2.THRESH_BINARY_INV)
_, blue_thres = cv2.threshold(blue_color, 150, 255, cv2.THRESH_BINARY_INV)

# Tìm tọa độ các điểm màu
red_points = np.column_stack(np.where(red_thres > 0))
blue_points = np.column_stack(np.where(blue_thres > 0))
yellow_points = np.column_stack(np.where(yellow_mask))

# Lấy kích thước ảnh
height, width = img.shape[:2]

# Khởi tạo Turtle
screen = turtle.Screen()
screen.setup(width=width, height=height)
screen.title('Drawing Points')
turtle.tracer(0, 0)

#Lấy các điểm màu
all_points = []

for point in red_points:
    all_points.append((point[0], point[1], 'red'))

for point in blue_points:
    all_points.append((point[0], point[1], 'blue'))

for point in yellow_points:
    all_points.append((point[0], point[1], 'yellow'))

# Sắp xếp các điểm theo y tăng dần
all_points.sort(key=lambda x: x[0])

# Tạo turtle
t = turtle.Turtle()
t.speed(0)
t.penup()

# Vẽ lần lượt
for i, (y, x, color) in enumerate(all_points):
    turtle_x = x - width // 2
    turtle_y = height // 2 - y

    t.goto(turtle_x, turtle_y)
    t.dot(2, color)

    if i % 1000 == 0:
        turtle.update()
t.hideturtle()
turtle.update()

#Kết thúc turtle
turtle.done()