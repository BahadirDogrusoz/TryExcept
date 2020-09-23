try:
    number = int(input("Bir sayı giriniz: "))
    print(number)

except ValueError:
    print("Lütfen bir sayı giriniz metin girmeyiniz")
    number = int(input("Bir sayı giriniz: "))
    print(number)