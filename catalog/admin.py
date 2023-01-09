from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    fields = ['title', 'isbn']

# Register the Admin classes for Author using the decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookInline]

admin.site.register(Genre)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', )

    inlines = [BooksInstanceInline]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']