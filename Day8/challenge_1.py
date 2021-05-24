import math

def calculate_cans_required(height, width):
  area_per_can = 5
  total_area = height * width
  cans_needed = total_area / area_per_can
  cans_needed = math.ceil(cans_needed)
  print(f"You will need {cans_needed} cans of paint")


height = int(input("Enter the height: \n"))
width = int(input("Enter the width: \n"))
calculate_cans_required(height, width)
