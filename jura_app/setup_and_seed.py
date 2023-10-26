import django, os, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techtest.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

from techtest.articles.models import Article
from techtest.regions.models import Region
from techtest.authors.models import Author
from django.core import management

# Migrate
management.call_command("migrate", no_input=True)

# Create authors
author1 = Author.objects.create(first_name="John", last_name="Doe")
author2 = Author.objects.create(first_name="Jane", last_name="Smith")

# Seed
Article.objects.create(title="Fake Article1", content="Fake Content1", author=author1).regions.set(
    [
        Region.objects.create(code="AL", name="Albania"),
        Region.objects.create(code="UK", name="United Kingdom"),
    ]
)
Article.objects.create(title="Fake Article2", content="Fake Content2")
Article.objects.create(title="Fake Article3", content="Fake Content3")
Article.objects.create(title="Fake Article4", content="Fake Content4", author=author2)
Article.objects.create(title="Fake Article5", content="Fake Content5", author=author2).regions.set(
    [
        Region.objects.create(code="AU", name="Austria"),
        Region.objects.create(code="US", name="United States of America"),
    ]
)
