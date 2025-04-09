N = int(input())  # Number of snowballs
max_value = -1  # To track the highest snowball value
best_snowball = ""  # To store the details of the best snowball

for _ in range(N):
    snowballSnow = int(input())  # Input snowballSnow
    snowballTime = int(input())  # Input snowballTime
    snowballQuality = int(input())  # Input snowballQuality

    # Calculate the snowball value
    snowballValue = round(snowballSnow / snowballTime) ** snowballQuality

    # Check if this is the highest snowball value
    if snowballValue > max_value:
        max_value = snowballValue
        best_snowball = f"{snowballSnow} : {snowballTime} = {snowballValue} ({snowballQuality})"

# Output the result
print(best_snowball)