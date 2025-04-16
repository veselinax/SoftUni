dogs_count = int(input())
animals_count = int(input())
dog_food = dogs_count * 2.50
animals_food = animals_count * 4
final_price = dog_food + animals_food
print(f"{final_price:.2f} lv.")    # format till second digit after .