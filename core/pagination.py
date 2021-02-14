from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination, CursorPagination


class LimitOffsetPaginationWithMaxLimit(LimitOffsetPagination):
    max_limit = 1000
    default_limit = 1000
    # page_size = 2


class StandardResultsSetPagination(PageNumberPagination):
    # page_size = 30
    # page_size = 10
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000
#
#
# # class StoryLineResultSetPagination(CursorPagination):
# #     page_size = 2
# #     ordering = '-created_at'
#
#
# class StoryLineResultSetPagination(PageNumberPagination):
#     page_size = 2
#     ordering = '-created_at'

