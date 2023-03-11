# PageNumberPagination Local Settings:
from rest_framework.pagination import PageNumberPagination
class SmallPageNumberPagination(PageNumberPagination):
    page_size = 25
    # page_query_param = "sayfa"

# LimitOffsetPagination Local Settings:
from rest_framework.pagination import LimitOffsetPagination
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'adet'

# CursorPagination Local Settings:
from rest_framework.pagination import CursorPagination
class MyCursorPagination(CursorPagination):
    page_size = 10
    ordering = "number"