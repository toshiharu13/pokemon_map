from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemons', null=True, blank=True)
    description = models.TextField(default='добавить описание')
    title_en = models.CharField(max_length=200, default='-')
    title_jp = models.CharField(max_length=200, default='-')
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL,
                                           blank=True, null=True,
                                           verbose_name='Из кого эволюционировал'
                                           )

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, null=True, blank=True,
        related_name='pokemonentity',
    )
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
