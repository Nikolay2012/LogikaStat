from django.db import models

# Create your models here.
class BasicData(models.Model):
    title = models.CharField(max_length=255)# определаем текстовое поле с максимальным количеством символов 255
    content = models.TextField(blank= True) # blank = True - данное поле может быть пустым
    # перед созданием поля image проверяем наличие пакета Pillow в установленных модулях Python
    image = models.ImageField(upload_to= "images/%Y/%m/%d/") # создаем в папке images каждый раз при добавлении новой картинки новую папку года или месяца, или дня
    time_create = models.DateTimeField(auto_now_add= True) # фиксируется дата на момент создания контента и больше это поле не меняется
    time_update = models.DateTimeField(auto_now= True) # в этом поле обновляется дата после каждого обновления информации
    is_published = models.BooleanField(default= True) # 

    def __str__(self):
        return self.title

object1 = BasicData()