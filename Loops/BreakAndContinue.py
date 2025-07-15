# break döngüyü durdurur.
# continue döngüde o değeri bulduğunda onu almaz ve devam eder.
name = "Utku Çakar"

for harf in name:
    if(harf == " "):
        continue
    print(harf)

print("***********")

for harf in name:
    if(harf == " "):
        break
    print(harf)