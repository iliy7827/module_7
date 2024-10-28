from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name      #название продукта
        self.weight = weight  #общий вес товара
        self.category = category #категория товара
    def __str__(self):  #возвращает строку в формате '<название>, <вес>, <категория>
        return (f'{self.name}, {self.weight}, {self.category}')

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r') #открывает файл и считывает информацию
        product = file.read() #прочитал информацию
        file.close()       #закрыл файл
        return product     #вернул единую строку со всеми товарами file_name

    def add(self, *products):  #принимает неограниченное количество объектов класса products
        for product in products:  #проверяем есть ли продукт в классе products
            if product.name not in self.get_products(): # если названия такого нет в классе
                file = open(self.__file_name, 'a') # открывает и добавляем в файл
                file.write(product.__str__() + '\n')

            else:               # если такой продукт есть выводит строку, что уже есть в магазине
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


