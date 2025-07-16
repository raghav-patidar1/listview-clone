from django.shortcuts import render


class BaseListView(type):
    '''Meta class for ListView'''
    
    def __new__(cls, name, bases, attrs):
        if name == "ListView":
            return super().__new__(cls, name, bases, attrs)
        
        if "model" not in attrs:
            raise NotImplementedError("model field is required.")
        
        model = attrs.get('model')
        attrs['queryset'] = model.objects.all()
        cls = super().__new__(cls, name, bases, attrs)
        return cls
    

class ListView(metaclass=BaseListView):
    '''
    Class based view to list the queryset objects.
    
    - 'model' field is required
    - default template_name = model_list.html
    - default context_object_name = model_objects
    '''
    template_name = None
    context_object_name = None

    def get_queryset(self):
        return self.queryset

    @property  
    def get_template_name(self):
        template_format_str = f"{self.model.__name__.lower()}_list.html"
        return self.template_name if self.template_name else \
            template_format_str
    
    @property
    def get_context_object_name(self):
        context_object_str = f"{self.model.__name__.lower()}_objects"
        return self.context_object_name if self.context_object_name else \
            context_object_str

    def get_response(self, request):
        context = {
            self.get_context_object_name: self.get_queryset()
        }
        return render(request, self.get_template_name, context)
    
