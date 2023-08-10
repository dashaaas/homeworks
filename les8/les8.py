1.apps.py:
from django.apps import AppConfig


class AppAdvertisementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_advertisements'
    verbose_name = 'Объявления'


2.admin.py --> class AdvertisementAdmin:
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'user', 'price', 'auction', 'created_at', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_true', 'make_auction_false']

models.py:
@admin.display(description='дата редактирования')
def updated_date(self):
    from django.utils import timezone
    if self.updated_at.date() == timezone.now().date():
        updated_time = self.updated_at.time().strftime("%H:%M:%S")
        return format_html(
            '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', updated_time
        )
    return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
