# Minimal Django ListView Clone

## Purpose
Built a simplified ListView-like class to understand Django CBV internals, revise OOPs and metaclass concepts.

## Features
- Enforces `model` attribute.
- Generates default `queryset`, `template_name`, and `context_object_name` automatically.
- Supports custom queryset by overriding `get_queryset()`.
- Automatically renders response using `get_response()`.

## Learnings
- Python metaclass usage
- CBV design patterns
- Django templating and context resolution

## How to Use

### Create a view
```python
from listview import ListView
from .models import Product

class ProductListView(ListView):
    model = Product

```

### Define URL pattern
```python
urlpatterns = [
    path('products/', views.ProductListView().get_response),
] 
```

### Run the server
```
python
py manage.py runserver
```