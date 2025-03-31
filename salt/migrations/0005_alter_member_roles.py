from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('salt', '0004_convert_roles_to_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='roles',
            field=models.JSONField(default=list),
        ),
    ] 