from rest_framework.pagination import PageNumberPagination

class SmallResultsSetPagination (PageNumberPagination):
    page_size = 12
    page_size_query_param = "size"
