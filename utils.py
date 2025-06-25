import cv2


def draw_measurements(image, contours, dimensions):
    """可视化标注工具"""
    for cnt, dim in zip(contours, dimensions):
        # 绘制轮廓
        cv2.drawContours(image, [cnt], 0, (0, 255, 0), 2)

        # 标注文字
        text = f"across_flats:{dim['diameter']}mm"
        x, y, _, _ = cv2.boundingRect(cnt)
        cv2.putText(image, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    return image
