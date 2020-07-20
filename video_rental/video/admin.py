from django.contrib import admin
from .models import Movie,Customer


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields         = ["relase_year","title","length"]
    list_display   = ['title','length','relase_year']
    list_filter    = ['title','length','relase_year']
    search_fields  = ['title','relase_year']
    ## if it is only one then you have to use the list
    list_editable  = ["relase_year",'length']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display   = ["first_name","last_name","phone"]
    list_filter    = ["first_name","last_name","phone"]
    search_fields  = ["first_name","last_name","phone"]
    list_editable  = ['phone']
