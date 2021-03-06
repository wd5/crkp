# -*- coding: utf-8 -*-
from django.db import models
import datetime, os
from django.utils.translation import ugettext_lazy as _
from apps.utils.managers import PublishedManager
from pytils.translit import translify
from apps.utils.utils import ImageField

def image_path_electroload_icon(instance, filename):
    return os.path.join('images','icons', translify(filename).replace(' ', '_') )

class Electroload(models.Model):
    icon = ImageField(upload_to=image_path_electroload_icon, verbose_name=u'иконка', blank=True)
    title = models.CharField(max_length=255, verbose_name=u'название')
    power_parameter = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=u'Мощность (P)')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'electroload')
        verbose_name_plural = _(u'electroloaders')

    def get_parameters(self):
        return self.parameter_set.all()

    def get_parameters_max_count(self):
        max_count = 0
        parameters = self.parameter_set.all()
        for item in parameters:
            if item.count_type == 'single':
                if item.count>max_count:
                    max_count = item.count
            elif item.count_type == 'interval':
                if item.end_count_interval>max_count:
                    max_count = item.end_count_interval
        if max_count == 0:
            max_count = ''
        return max_count

    def get_src_image(self):
        return self.icon.url

    def delete(self, **kwargs):
        if self.id != 7:
            super(Electroload, self).delete(**kwargs)

count_choices = (
    (u'single',u'фиксированное количество'),
    (u'interval',u'интервал'),
    )

class Parameter(models.Model):
    electroload = models.ForeignKey(Electroload, verbose_name = u'электропотребитель')
    count_type = models.CharField(u'тип', choices=count_choices, max_length=20)
    start_count_interval = models.PositiveIntegerField(verbose_name = u'от', blank=True, null=True)
    end_count_interval = models.PositiveIntegerField(verbose_name = u'до', blank=True, null=True)
    count = models.PositiveIntegerField(verbose_name = u'фиксированное количество', blank=True, null=True)
    parameter_demand = models.DecimalField(max_digits=6, decimal_places=4, verbose_name=u'Коэффициент спроса (К.с.)')

    def __unicode__(self):
        return u'параметр №%s для электропотребителя "%s"' % (self.id, self.electroload.title)

    class Meta:
        verbose_name = _(u'parameter')
        verbose_name_plural = _(u'parameters')

class MapPolygon(models.Model):
    polygon = models.CharField(max_length=255, verbose_name=u'координаты полигона')
    title = models.CharField(max_length=100, verbose_name=u'территориальная зона')
    number = models.PositiveSmallIntegerField(verbose_name = u'номер полигона')
    table_rates = models.TextField(verbose_name = u'таблица ставок')
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'полигон № %s' % self.number

    class Meta:
        ordering = ['id']
        verbose_name = _(u'polygon')
        verbose_name_plural = _(u'polygons')