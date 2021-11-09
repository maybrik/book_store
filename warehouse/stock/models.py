from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    about = models.CharField(max_length=500)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def str(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    name = models.CharField('Название книги', max_length=100)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=10)
    author = models.ManyToManyField(Author, 'Автор')
   # available = models.BooleanField('Доступность к заказу', default=True)

    def _str_(self):
        return f'{self.name}'


class Publisher(models.Model):
    publisher_name = models.TextField('Издательство', max_length=200)
    city = models.TextField('Город', max_length=100)
    license = models.CharField('Номер лицензии', max_length=19)


class BookInstance(models.Model):

    IN_PROGRESS = 'In_progress'
    PACKED = 'Packed'
    DELIVERING = 'Delivering'
    RECEIVED = 'Received'

    CHOICE_STATUS = {
        (IN_PROGRESS, 'В обработке'),
        (PACKED, 'Упакован'),
        (DELIVERING, 'Доставляется'),
        (RECEIVED, 'Получен')
    }

    name = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher_name = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    date_of_order = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Статус заказа', choices=CHOICE_STATUS, max_length=30, default=IN_PROGRESS)

    def __str__(self):
        return f'{self.isbn + self.status}'