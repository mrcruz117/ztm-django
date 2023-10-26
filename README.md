# Django Reference

`/drf-test` contains the majority of drf info used on the job so far.


## Very useful modules

`rest_framework_nested` routers make it very simple to make a single intuitive endpoint out of the boxwithout having to add extra views

```bash
$ pip install drf-nested-routers
```
django_filters
```bash
$ pip install django-filter
```


## Important Note

Because of the `drf-nested-routers` library, you need to create different serializers depending on the action if you want to display the foreignKey item rather than just its pk
```python
class Source_locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source_location
        fields = '__all__'

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    source = Source_locationSerializer()

    class Meta:
        model = Item
        # fields = ('name', 'price', 'description')
        fields = '__all__'
```

Here is how you can handle the cooresponding view:

**Note the use of** `ModelViewSet`. This is needed for the `rest_framework_nested` module

```python
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ItemCreateSerializer
        # if self.action == 'list':
        return ItemSerializer
```

