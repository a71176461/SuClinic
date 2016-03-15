from django.contrib import admin
from messages_board.models import Post

# Register your models here.

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

    # class Meta:
    #     exclude = (
    #         'response',
    #     )

admin.site.register(Post, MessagesAdmin)
