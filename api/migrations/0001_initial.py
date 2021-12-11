from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(
            name="mark",
            email="mark@gmail.com",
            is_staff=True,
            is_superuser=True,
            phone="0971094624",
        )

        user.set_password("qwerty")
        user.save()

    dependencies = []
    operations = [migrations.RunPython(seed_data)]
