n = int(input())

def loading_bar(num):
    bar = []
    percent = num  # if we have 30 then 30 %
    if num == 100:
        return f"{percent}% Complete!\n[%%%%%%%%%%]"
    elif num < 100:
        num = num // 10   # number of % (if we have 30 we need 3 %)
        for i in range(num):   # adding % n times
            bar.append("%")
        left_dots = 10 - num   # remaining dots
        add = "."*left_dots   # to be [%%%.......] for example  (string)
        bar.append(add)  #we add it to the list
        string = "".join(bar)  #joining so we don't have spaces and commas (making the list string)
        return f"{percent}% [{string}]\nStill loading..."



print(loading_bar(n))