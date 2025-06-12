from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name='districts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.region.name})"


class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'Дом'),
        ('apartment', 'Квартира'),
        ('hotel', 'Гостиница'),
        ('hostel', 'Хостел'),
    ]

    type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    custom_id = models.PositiveIntegerField(null=True, editable=False)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    features = models.ManyToManyField(Feature, blank=True)

    def __str__(self):
        address = f"{self.street} {self.house_number}"
        if self.apartment_number:
            address += f", кв. {self.apartment_number}"
        return f"{self.get_type_display()}: {address} ({self.district})"

    def save(self, *args, **kwargs):
        if self.custom_id is None:
            # Найдём максимальный custom_id среди объектов того же типа
            last = Property.objects.filter(type=self.type).aggregate(models.Max('custom_id'))['custom_id__max']
            self.custom_id = (last or 0) + 1
        super().save(*args, **kwargs)

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Изображение для {self.property}"


class House(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    beds = models.PositiveIntegerField()
    features = models.ManyToManyField(Feature, blank=True)

    def __str__(self):
        return self.title


class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='houses/')

    def __str__(self):
        return f"Фото для {self.house}"


class Hostel(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    features = models.ManyToManyField(Feature, blank=True)

    def __str__(self):
        return self.name


class BookingRequest(models.Model):
    house = models.ForeignKey(House, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    people = models.PositiveIntegerField()
    criteria = models.TextField(blank=True)
    budget = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        status = "Подтверждено" if self.is_confirmed else "Ожидает"
        return f"{self.name} ({self.phone}) — {status}"


class HouseRequest(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    people_count = models.PositiveIntegerField()
    criteria = models.TextField(blank=True)
    budget = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} — {self.check_in} to {self.check_out}"


class RequestForm(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    guests = models.IntegerField()
    criteria = models.TextField()
    budget = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.check_in} - {self.check_out})"


class Apartment(Property):
    class Meta:
        proxy = True
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

class Hotel(Property):
    class Meta:
        proxy = True
        verbose_name = "Гостиница"
        verbose_name_plural = "Гостиницы"
