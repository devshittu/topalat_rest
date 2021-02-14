from core.renderers import AppJSONRenderer


class ProfileJSONRenderer(AppJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_object_count_label = 'profilesCount'


class ServiceJSONRenderer(AppJSONRenderer):
    object_label = 'service'
    pagination_object_label = 'services'
    pagination_object_count_label = 'servicesCount'
