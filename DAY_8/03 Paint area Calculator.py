import math
def paint_calc(height, width, cover):
    number_of_cans = height * width / cover
    rounded_no_of_cans = math.ceil(number_of_cans)
    print(f"You'll need {rounded_no_of_cans} cans of paint")

test_h = int(input())   #Height of the wall (m)
test_w = int(input())   #Width of the wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
