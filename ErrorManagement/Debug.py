# Hata Ayıklama
import pdb

one = "one"
two = "two"

pdb.set_trace() # uygulama burada durur
# l => listeleme
# n => next line sonraki satıra geçer
# p => print değişken içerine bakmak için
# c => continue kodların ilerletilmesi

result = one + two

three = "three"

result += three

print(result)