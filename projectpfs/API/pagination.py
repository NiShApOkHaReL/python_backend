# #PageNumberPagination
# from rest_framework.pagination import PageNumberPagination

# class StudentPagination(PageNumberPagination):
#     page_size = 5  
#     page_query_param ='p'
#     page_size_query_param = 'page_size' # Lets clients choose custom page size via URL
#     max_page_size = 10
#     last_page_strings = 'end'


# .....................................................
# LimitOffsetPagination
from rest_framework.pagination import LimitOffsetPagination

class StudentPagination(LimitOffsetPagination):
    default_limit = 5              # Default items per page
    limit_query_param = 'per_page' # Query param to set items per page (e.g., ?per_page=7)
    offset_query_param = 'offset'  # Query param to skip items (e.g., ?offset=10)
    max_limit = 10                 # Max items allowed per request

# #Cursor Pagination
# from rest_framework.pagination import CursorPagination

# class StudentPagination(CursorPagination):
#     page_size = 5
#     ordering = '-id' # Ordering by id in descending order
