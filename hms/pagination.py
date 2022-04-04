from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pg_size'
    max_page_size = 1000