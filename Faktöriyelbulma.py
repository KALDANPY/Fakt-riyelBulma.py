Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("""**************************
FAKTÖRİYEL BULMA PROGRAMI


Programdan çıkmak için q'ya basınız. 
**************************""")

while True:
    sayı = input("Bir sayı giriniz : ")
    if (sayı == "q"):
        print("Program sonlanıyor...")
        break
    else:
        sayı = int(sayı)

        faktoriyel = 1
        for i in range(2,sayı+1):
            faktoriyel *= i #Girilen sayının 4 olduğunu farzedelim i for sayesinde range in içindeki tüm sayılarda geziniyor 
            # teker teker i değerleri 2 ,3,4,5 oluyor range kuralı ise ilk sayıdan son sayıya kadar son sayı HARİÇ bize okuyor.
            # işte bu yüzden faktöriyel zaten 1'idi ve 1*2 = 2 sonra 2*3 = 6 ve sonra 6*4= 24
            #şeklinde sürekli faktöriyel değişkenimiz değişiyor ve i ile çarpılarak gidiyor 
            
        print("Faktöriyel",faktoriyel)
