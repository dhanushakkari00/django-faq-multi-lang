from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    """
    Admin configuration for the FAQ model.
    """
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question', 'question_hi', 'question_bn', 'question_ta',
                     'question_te', 'question_mr', 'question_ml', 'question_kn')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'answer':  # Apply CKEditor only to the answer field
            # Dynamically set the language for CKEditor
            user_language = request.GET.get('lang', 'en')  # Default to English
            kwargs['widget'] = CKEditorWidget(config_name='default')
            kwargs['widget'].attrs.update({'lang': user_language})
        return super().formfield_for_dbfield(db_field, request, **kwargs)

admin.site.register(FAQ, FAQAdmin)
