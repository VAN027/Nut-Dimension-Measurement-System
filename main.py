import cv2
from image_processor import ImageProcessor
from nut_analyzer import NutAnalyzer
from utils import draw_measurements

'''
版本：1.0
功能说明：可识别静态图片上的螺母的跨平距离
可优化：1.图片中9个螺母只能识别出7个；2.无法在图像中显示中文；3.没有区分圆形螺母和六角螺母
'''


def main():
    # 1. 读取输入
    image = cv2.imread("Nut.jpg")

    # 2. 图像预处理
    processed = ImageProcessor.preprocess(image)

    # 3. 轮廓检测
    contours = ImageProcessor.find_contours(processed)

    # 4. 筛选螺母轮廓
    valid_contours = NutAnalyzer.filter_contours(contours)

    # 5. 尺寸计算
    dimensions = [NutAnalyzer.calculate_dimensions(cnt)
                  for cnt in valid_contours]

    # 6. 可视化结果
    result_image = draw_measurements(image.copy(), valid_contours, dimensions)

    # 7. 显示输出
    cv2.imshow("Measurement Result", result_image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
