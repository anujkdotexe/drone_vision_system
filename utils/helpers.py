def calc_coverage(bbox, shape):
    x1,y1,x2,y2 = bbox; h,w=shape[:2]
    return round(((x2-x1)*(y2-y1))/(h*w)*100,2)