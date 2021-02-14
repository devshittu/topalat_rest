import json

from django.contrib.gis.geos import collections
from rest_framework.renderers import JSONRenderer


class AppJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    pagination_object_label = 'objects'
    pagination_object_count_label = 'count'
    pagination_next_label = 'next'
    pagination_previous_label = 'previous'

    default_info_label = 'info'
    default_warning_label = 'warning'
    default_error_label = 'error'
    # default_error_label = {('error', 'flash', ), ('error', 'normal', ), }

    def render(self, data, media_type=None, renderer_context=None):
        # print('data:// fam: ', type (data), data)
        if data.get('results', None) is not None:
            return json.dumps({
                self.pagination_object_count_label: data['count'],
                self.pagination_next_label: data['next'],
                self.pagination_previous_label: data['previous'],
                self.pagination_object_label: data['results'],
            })

        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        elif data.get('errors', None) is not None:
            return super(AppJSONRenderer, self).render(data)

        elif data.get('detail', None) is not None:
            # label = self.default_error_label[0]
            # behavior_type =
            # return json.dumps({
            #     self.default_error_label: data['detail'],
            # })
            return super(AppJSONRenderer, self).render(data)


        else:
            return json.dumps({
                self.object_label: data
            })
