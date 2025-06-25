import cv2
from config import Config


class ImageProcessor:
    @staticmethod
    def preprocess(image):
        """图像预处理流水线"""
        # 转换为灰度图
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 高斯模糊降噪
        blurred = cv2.GaussianBlur(gray, Config.GAUSSIAN_KSIZE, 0)

        # Canny边缘检测
        edges = cv2.Canny(blurred, Config.CANNY_THRESH1, Config.CANNY_THRESH2)

        # 形态学操作（闭合小孔）
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        return closed

    @staticmethod
    def find_contours(processed_image):
        """轮廓检测方法"""
        contours, _ = cv2.findContours(
            processed_image,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )
        return contours
