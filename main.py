class Xisob:
    def __init__(self, son):
        self._son = son

    @property
    def son(self):
        return self._son

    @son.setter
    def son(self, value):
        if isinstance(value, (int, float)):
            self._son = value
        else:
            raise TypeError("Sonlar faqat butun yoki o'ngacha son bo'lishi mumkin.")

    @son.deleter
    def son(self):
        del self._son

class Test:
    def __init__(self):
        self.xisob = Xisob(10)

    def test_property(self):
        print(self.xisob.son)  # 10
        self.xisob.son = 20
        print(self.xisob.son)  # 20
        del self.xisob.son
        try:
            print(self.xisob.son)
        except AttributeError:
            print("Son o'chirilgan")

test = Test()
test.test_property()
```

@property dekoratori getter metodni yaratadi. Uning yordamida klassning atributi o'zgaruvchisiga qarab getter metodni yaratib oladi. Shuningdek, getter metodni yaratish uchun getter metodni yaratish uchun @property dekoratori ishlatiladi.
