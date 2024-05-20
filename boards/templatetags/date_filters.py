from django import template
import locale

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

register = template.Library()


@register.filter
def date_avec_heure(value):
    if value:
        return value.strftime('%d %B %Y à %H:%M')
    return ''
