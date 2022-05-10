from django.db import models
from django.urls import reverse


class Delivered_status(models.Model):
    ''' Статусы заявки '''
    name = models.CharField(max_length=100, db_index=True, verbose_name="Наименование статусов заявки")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('delivered_status', kwargs={'delivered_status_slug': self.slug})

    class Meta:
        verbose_name = 'Статусы заявки'
        verbose_name_plural = 'Статусы заявки'
        ordering = ['id']


class Shipping_request(models.Model):
    ''' Заявка на отгрузку '''

    ''' Общая информация '''
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    is_deleted = models.BooleanField(default=False, verbose_name="Публикация")
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    datetime_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    delivered_status = models.ForeignKey('delivered_status', on_delete=models.PROTECT, verbose_name="Статусы заказов")

    # delivered_status verbose_name="ссылка на справочник статусов заказа (новый, оформлен, отгружен, в пути, доставлен)"

    ''' Информация для перевозчика '''
    Delivery_information = models.CharField(max_length=255, verbose_name="Информация для перевозчика")
    Deliverier = models.CharField(max_length=255, verbose_name="Перевозчик")
    Deliverier_phone = models.CharField(max_length=255, verbose_name="Телефон перевозчика")

    ''' Информация о Грузоотправителе '''
    shipper = models.CharField(max_length=255, verbose_name="Грузоотправитель")
    shipper_inn = models.CharField(max_length=255, verbose_name="ИНН Грузоотправителя")
    shipper_address = models.CharField(max_length=255, verbose_name="Адрес Грузоотправителя")
    shipper_phone = models.CharField(max_length=255, verbose_name="Телефоны Грузоотправителя")
    shipper_contacts = models.CharField(max_length=255, verbose_name="Контактное лицо")

    ''' Информация о Грузополучателе '''
    consignee = models.CharField(max_length=255, verbose_name="Грузополучатель")
    consignee_address = models.CharField(max_length=255, verbose_name="Адрес Грузополучателя")
    consignee_phone = models.CharField(max_length=255, verbose_name="Телефоны Грузополучателя")
    Consignee_contacts = models.CharField(max_length=255, verbose_name="Контактное лицо")
    Consignee_workhours = models.CharField(max_length=255, verbose_name="Время работы склада Грузополучателя")

    ''' Информация о Грузе '''
    cargo_name = models.CharField(max_length=255, verbose_name="Наименование груза")
    cargo_quantity = models.IntegerField(verbose_name="Фактическое количество мест")
    cargo_addition = models.CharField(max_length=255, verbose_name="Дополнение к грузу")
    cargo_addition_quantity = models.IntegerField(verbose_name="Доп. фактическое количество мест")

    ''' Информация о доп. услугах '''
    shipper_additional_services1 =\
        models.BooleanField(default=False,
                            verbose_name="Дополнительная услуга перевозчика ""Жесткая упаковка"" по желанию клиента")
    shipper_additional_services2 =\
        models.BooleanField(default=False,
                            verbose_name="Дополнительная услуга перевозчика ""Доставка до двери"""
                                         " в городе грузополучателя")


    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ship', kwargs={'ship_slug': self.slug})

    class Meta:
        verbose_name = 'Заявки на отгрузку'
        verbose_name_plural = 'Заявки на отгрузку'
        ordering = ['id']



