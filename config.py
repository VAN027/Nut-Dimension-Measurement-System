class Config:
    # 图像预处理参数
    GAUSSIAN_KSIZE = (7, 7)  # 高斯模糊核大小
    CANNY_THRESH1 = 10  # Canny边缘检测阈值1
    CANNY_THRESH2 = 80  # Canny边缘检测阈值2

    # 轮廓筛选参数
    MIN_AREA = 1000  # 最小轮廓面积
    MAX_AREA = 10000  # 最大轮廓面积

    # 标定参数（需根据实际标定结果修改）
    PIXELS_PER_MM = 15.5  # 每毫米像素数（通过标定板计算）
