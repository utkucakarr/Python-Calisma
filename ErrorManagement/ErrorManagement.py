while True:
    try:
        x = int(input("x : "))
        y = int(input("y : "))
        print(x/y)
    except (ZeroDivisionError, IndexError) as e:
        print("y sıfır olamaz")
        print(e) # loglama yaparak bunu veri tabanına kaydedebiliriz.
    except ValueError:
        print("x ve y sayı değer olmalıdır")
    except Exception as e: # farklı bir hata geldiğinde
        print("Bilinmeyen bir hata oluştu")
        print(e)
    else: # except bloğuna girmez ise else girer
        break
    finally: # except çalışsın veya çalışmasın 
        print("Finally bloğu çalıştı")