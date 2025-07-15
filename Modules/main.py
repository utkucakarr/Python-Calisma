import module

result = module.number
result = module.numbers
result = module.product
result = module.product["productName"]
result = module.product["renkler"]
result = module.sum(5,10)

import module as m # module takma isim verildi

result = m.number

from module import number, numbers, product # burada modülden belirtilen değişkenleri çektik
result = number

from module import * # module dosyasından herşeyi import et demek module ismini kullanmamıza gerek kalmaz

print(result)