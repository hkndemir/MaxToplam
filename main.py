def maxOlan(sayi1: int, sayi2: int):
    if sayi1 < sayi2:
        return sayi2
    else:
        return sayi1

def asalOlmayan(sayi):
    if sayi == 1 or sayi == 0 or sayi == -1:
        return False
    if sayi == 2:
        return True
    if sayi == 4 or sayi == -4:
        return False
    is_prime_number = True
    for i in range(2, int(sayi / 2)):
        if sayi % i == 0:
            is_prime_number = False
    return is_prime_number

def piramitToplam(pyramid, i, j, row):
    if i == row:
        return 0
    else:
        return pyramid[i][j] + maxOlan(piramitToplam(pyramid, i+1, j, row), piramitToplam(pyramid, i+1, j+1, row))
if __name__ == "__main__":
    #Dosya Okuma
    with open('input.txt', 'r') as file:
        #Her satırı diziye çevirme
        list = [[int(x) for x in line.split()] for line in file]
    # Satır Sayısını Bulma
    print(list)
    row = len(list)
    maxSum = 0
    # Asal olan sayıları değersiz yapılıyor
    for i in range(0, row):
        for j in range(0, i + 1):
            if list[i][j] != None and asalOlmayan(list[i][j]):
                list[i][j] = float('-inf')
    # İlk sayının asal olup olmadığına bakılıyor
    if list[0][0] == float('-inf'):
        print("There is no path")
    # Piramitten en büyük toplam bulunuyor
    maxSum = piramitToplam(list, 0, 0, row)
    print(maxSum)
