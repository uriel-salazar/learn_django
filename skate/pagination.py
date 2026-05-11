from rest_framework import pagination

class CostumPagination(pagination.PageNumberPagination):
    default_limit = 10
    max_limit = 1000000
    min_limit = 1
    min_offset = 1
    max_offset =1000000
    
    