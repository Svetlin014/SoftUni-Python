nylon_metres = int(input())
paint_liters = int(input())
diluent_liters = int(input())
hours_needed = int(input())

nylon_sum = (nylon_metres + 2) * 1.50
paint_sum = (paint_liters * 1.10) * 14.50
diluent_sum = diluent_liters * 5.00
bag_price = 0.40
materials_sum = nylon_sum + paint_sum + diluent_sum + bag_price
pay_per_hour = materials_sum * 0.30
final_pay = pay_per_hour * hours_needed

total_sum = final_pay + materials_sum
print(total_sum)
