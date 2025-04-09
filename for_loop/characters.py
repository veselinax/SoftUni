start = ord('a') #a
end = ord('{')   # the symbol after z so the range in the for loop can include z
#а ord(), който извежда десетичната стойност на всяка буква съгласно ASCII таблицата

for i in range(start, end): #chr(), който превръща десетична стойност в съответния символ от ASCII таблицатa
    print(chr(i))
