import math

def paint_calc(height,width,coverage):
    paint_required = math.ceil((height*width)/coverage)
    return paint_required


height = float(input("enter height of wall :"))
width = float(input("enter width of wall :"))
cover = float(input("enter coverage of wall :"))

paint = paint_calc(height,width,cover)
print(f"you will need {paint} cans of paint")