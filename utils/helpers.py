def calculate_bbox_coverage(bbox, image_shape):
    x1, y1, x2, y2 = bbox
    img_h, img_w = image_shape[:2]
    box_area = (x2 - x1) * (y2 - y1)
    img_area = img_h * img_w
    coverage = round((box_area / img_area) * 100, 2)
    return coverage
