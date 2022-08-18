ps=0
ns=0
while True:
       s=input("sayıyı giriniz:")
       try:
              if int (s)>0:
                     print(s,"sayısı pozitiftir.")
                     ps=ps+1
              elif int (s)<0:
                     print(s,"sayısı negatiftir.")
                     ns=ns+1
       except:
              if s=="x" or s=="x":
                     print("Bulduğum pozitif sayılar:",ps)
                     print("Bulduğum negatif sayılar:",ns)
                     
              else:
                     print("Hata,lütfen sayı giriniz.")
                     continue
              a=input("çıkmak için y'ye basın devam etmek için herhangi bir tuşa basın:")
              if(a=="y"):
                     quit()
              
