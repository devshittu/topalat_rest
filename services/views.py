from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from core.permissions import IsSuperUserOrReadOnly
from core.views import MyListCreateAPIView, MyRetrieveUpdateDestroyAPIView, MyListAPIView
from .renderers import ServiceJSONRenderer
from .models import TransactionLog
from .serializers import TransactionLogSerializer


class TransactionLogFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='reference', lookup_expr='icontains')

    class Meta:
        model = TransactionLog
        fields = ('reference',)


class TransactionLogList(MyListCreateAPIView):
    queryset = TransactionLog.objects.all()
    print('Queryset: ', queryset)
    serializer_class = TransactionLogSerializer
    # permission_classes = (AllowAny,)
    name = 'transaction-log-list'
    filterset_class = TransactionLogFilter
    # ordering_fields = ('name',)
    # lookup_field = 'pk'
    # ordering = ('reference',)
    ordering = ('-created_at',)
    search_fields = ('reference',)
    renderer_classes = (ServiceJSONRenderer,)

    permission_classes = (
        # IsSuperUserOrReadOnly,
        IsAuthenticated,
    )

    # def get_queryset(self):
    #     # qs = super(TransactionLogByCategoryList, self).get_queryset()
    #     category_from_uri = self.kwargs['category']
    #     print(category_from_uri)
    #     if category_from_uri is None:
    #         return TransactionLog.objects.get(service_category_raw=category_from_uri)
    #     else:
    #         return TransactionLog.objects.all()


class TransactionLogByCategoryList(MyListAPIView):
    queryset = TransactionLog.objects.all()
    print('Queryset: ', queryset)
    serializer_class = TransactionLogSerializer
    # permission_classes = (AllowAny,)
    name = 'transaction-log-list'
    filterset_class = TransactionLogFilter
    # ordering_fields = ('name',)
    # lookup_field = 'pk'
    ordering = ('reference',)
    search_fields = ('reference',)
    renderer_classes = (ServiceJSONRenderer,)

    permission_classes = (
        # IsSuperUserOrReadOnly,
        IsAuthenticated,
    )

    def get_queryset(self):
        slug_from_uri = self.kwargs['category']
        return TransactionLog.objects.filter(service_category_raw=slug_from_uri)

    # def get_queryset(self):
    #     # print('request: //', self)
    #     qs = super(TransactionLogByCategoryList, self).get_queryset()
    #     slug_from_uri = self.kwargs['category']
    #     try:
    #         the_story = TransactionLog.objects.get(service_category_raw=slug_from_uri)
    #     except TransactionLog.DoesNotExist:
    #         raise NotFound('A transaction with this category: %s does not exist.' % (slug_from_uri,))
    #
    #     # past_stories = the_story.get_all_parents()
    #     # print('LOG: past_stories:// ', past_stories)
    #     past_story_pks = []
    #     for past_story in past_stories:
    #         try:
    #             # check all passed category ids exists
    #             check = TransactionLog.objects.get(pk=past_story.pk)
    #         except TransactionLog.DoesNotExist:
    #             raise NotFound('A story with this id: %s does not exist.' % (past_story,))
    #         if the_story.pk is not past_story.pk:
    #             past_story_pks.append(past_story.pk)
    #
    #     # past_story_pks = past_story_pks[::-1] #_reversed
    #     print('past_story_pks://', past_story_pks)
    #
    #     # return qs.filter(pk__in=past_story_pks_reversed).order_by('-published_at')
    #     return qs.filter(pk__in=past_story_pks)


class TransactionLogDetail(MyRetrieveUpdateDestroyAPIView):
    queryset = TransactionLog.objects.all()
    serializer_class = TransactionLogSerializer
    # lookup_field = 'slug'
    lookup_field = 'reference'
    # permission_classes = (AllowAny,)
    name = 'transaction-log-detail'
    permission_classes = (
        # IsSuperUserOrReadOnly,
        IsAuthenticated,
    )
