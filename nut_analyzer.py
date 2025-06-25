import cv2
import numpy as np
from config import Config


class NutAnalyzer:
    @staticmethod
    def filter_contours(contours):
        """筛选有效螺母轮廓"""
        valid_contours = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if Config.MIN_AREA < area < Config.MAX_AREA:
                valid_contours.append(cnt)
        return valid_contours

    @staticmethod
    def calculate_dimensions(contour):
        """计算螺母尺寸"""
        # 最小外接圆
        (x, y), radius = cv2.minEnclosingCircle(contour)

        # 外接矩形
        rect = cv2.minAreaRect(contour)

        (w, h) = rect[1]
        distance_across_flats_pixels = min(w, h)

        # 转换实际尺寸（毫米）
        diameter_mm = distance_across_flats_pixels / Config.PIXELS_PER_MM
        width_mm = w / Config.PIXELS_PER_MM
        height_mm = h / Config.PIXELS_PER_MM

        return {
            "diameter": round(diameter_mm, 2),
            "width": round(width_mm, 2),
            "height": round(height_mm, 2)
        }
