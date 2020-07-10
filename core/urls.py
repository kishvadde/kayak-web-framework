import re
from .views import hello, bye, raise_exception

urlpatterns = [
    ('hello$', hello),
    ('bye$', bye),
    ('exception$', raise_exception),
]


def view_resolver(path):
    for pattern, handler in urlpatterns:
        if re.search(pattern, path):
            return handler
    raise Exception('No matching view found')