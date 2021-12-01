from django.db import models


class Pokemon(models.Model):
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Изображение', upload_to='pokemons', blank=True,
                              null=True
                              )
    description = models.TextField('Описание', blank=True)
    title_en = models.CharField('Название англ.', max_length=200, blank=True
                                )
    title_jp = models.CharField('Название яп.', max_length=200, blank=True
                                )
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL,
                                           blank=True, null=True,
                                           verbose_name='Из кого эволюционировал',
                                           related_name='next_evolution'
                                           )

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, null=True, blank=True,
        related_name='pokemonentities', verbose_name='Покемон',
    )
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появляется')
    disappeared_at = models.DateTimeField('Исчезает')
    level = models.IntegerField('Уровень', default=0)
    health = models.IntegerField('Здоровье', default=0)
    strength = models.IntegerField('Сила', default=0)
    defence = models.IntegerField('Защита', default=0)
    stamina = models.IntegerField('Выносливость', default=0)

    class Meta:
        verbose_name = 'Сущность на карте'
        verbose_name_plural = 'Сущности на карте'

    def __str__(self):
        return 'Сущность {}'.format(self.pokemon)
