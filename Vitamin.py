class Vitamin:

    def __init__(self, name, description, resource_url, price):
        self.name = name
        self.description = description
        self.resource_url = resource_url
        self.price = price



vitamins = [
    Vitamin(name="Тройная Омега",description="Максимум омега-3 в каждой капсуле – 950 мг. В 3 раза сильнее обычной. Выгоднее зарубежного аналога", resource_url="resourses/omega_3.png",price=1),
    Vitamin(name="Цинк",description="биологически активная добавка к пище, содержащая важный для здоровья человека микроэлемент, цинк в биодоступной форме.", resource_url="resourses/zinc.png",price=2),
    Vitamin(name="Черника Форте",description="Комплекс для зрения с антоцианами черники и таурином", resource_url="resourses/blueberry.png",price=3),
    Vitamin(name="Инозитол",description="Высокая дозировка активной формы инозитола – мио-инозитол.", resource_url="resourses/inozitol.png",price=4),
]