from django.shortcuts import render


class BaseListView(type):
    """
    Metaclass for ListView.

    - Automatically injects a default queryset if the `model` attribute is present.
    - Enforces the presence of the `model` attribute in subclasses (except for the base ListView).
    """
    
    def __new__(cls, name, bases, attrs):
        if name == "ListView":
            return super().__new__(cls, name, bases, attrs)
        
        if "model" not in attrs:
            raise NotImplementedError("model field is required.")
        
        # add default queryset
        model = attrs.get('model')
        attrs['queryset'] = model.objects.all()
        cls = super().__new__(cls, name, bases, attrs)
        return cls
    

class ListView(metaclass=BaseListView):
    """
    A minimal implementation of Django-like ListView using metaclasses.

    Attributes:
        model (Model): Required. The Django model to list.
        template_name (str): Optional. Defaults to `<model>_list.html`.
        context_object_name (str): Optional. Defaults to `<model>_objects`.

    Methods:
        get_queryset(): Returns the queryset to be rendered.
        get_template_name(): Resolves the template name.
        get_context_object_name(): Resolves the context variable name.
        get_response(request): Renders the response with context and template.
    """
    template_name = None
    context_object_name = None

    def get_queryset(self):
        """
        Returns the queryset to be rendered in the template.
        Override this method to customize the queryset.
        """
        return self.queryset
  
    @property
    def get_template_name(self):
        """
        Returns the template name to use.
        If not specified, defaults to `<model>_list.html`.
        """
        template_format_str = f"{self.model.__name__.lower()}_list.html"
        return self.template_name if self.template_name else \
            template_format_str
    
    @property
    def get_context_object_name(self):
        """
        Returns the context variable name for the queryset.
        If not specified, defaults to `<model>_objects`.
        """
        context_object_str = f"{self.model.__name__.lower()}_objects"
        return self.context_object_name if self.context_object_name else \
            context_object_str

    def get_response(self, request):
        """
        Renders the response using the resolved template and context.
        """
        context = {
            self.get_context_object_name: self.get_queryset()
        }
        return render(request, self.get_template_name, context)
    
