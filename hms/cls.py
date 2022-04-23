from django.db.models import Avg, Count, Min, Sum, Max
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response

op = {
    'sum':Sum, 'max':Max,
    'min':Min, 'avg':Avg,
    'count':Count,
}

class Aggregation(object):

    @action(detail=False, methods=['get'], url_path='aggregate')
    def aggr(self, request):
        params = dict(request.query_params)

        func, group = op.get(params.pop('op', None)[0], None), params.pop('group', None)

        if not func or not group:
            raise ValidationError('no aggregation function provided or group missing')

        try:
            model = self.serializer_class.Meta.model
            # res = self.queryset.filter(**params).aggregate(*[func(group) for group in group])
            res = model.objects.values(*group).filter(**params).annotate(**{field+f'__{func.__name__.lower()}': func(field) for field in group})
            return Response(res)
        except Exception as e:
            raise ValidationError(e)
        
