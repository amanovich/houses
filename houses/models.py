from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class House(models.Model):
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    beds = models.PositiveIntegerField()
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.title

class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='houses/')

class BookingRequest(models.Model):
    house = models.ForeignKey(House, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    people = models.PositiveIntegerField()
    criteria = models.TextField(blank=True)
    budget = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Region(models.Model):
        name = models.CharField(max_length=255)  # Название области
        description = models.TextField()  # Описание области

        def __str__(self):
            return self.name

class District(models.Model):
        name = models.CharField(max_length=255)  # Название района
        region = models.ForeignKey(Region, related_name='districts', on_delete=models.CASCADE)  # Связь с областью


        def __str__(self):
            return f"{self.name} ({self.region.name})"

class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'Дом'),
        ('apartment', 'Квартира'),
        ('hotel', 'Гостиница'),
    ]

    type = models.CharField(max_length=20, choices=PROPERTY_TYPES)  # Тип недвижимости
    street = models.CharField(max_length=255)                      # Улица
    house_number = models.CharField(max_length=10)                 # Номер дома
    # apartment_number = models.CharField(max_length=10, blank=True, null=True)  # Квартира (необязательно)
    phone_number = models.CharField(max_length=20)                 # Телефон
    # latitude = models.DecimalField(max_digits=9, decimal_places=6)   # Широта
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Долгота
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        address = f"{self.street} {self.house_number}"
        if self.apartment_number:
            address += f", кв. {self.apartment_number}"
        return f"{self.get_type_display()}: {address} ({self.district})"
