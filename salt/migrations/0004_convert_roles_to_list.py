from django.db import migrations

def convert_roles_to_list(apps, schema_editor):
    Member = apps.get_model('salt', 'Member')
    for member in Member.objects.all():
        if isinstance(member.roles, str):
            member.roles = [role.strip() for role in member.roles.split(',')]
            member.save()

def convert_roles_to_string(apps, schema_editor):
    Member = apps.get_model('salt', 'Member')
    for member in Member.objects.all():
        if isinstance(member.roles, list):
            member.roles = ', '.join(member.roles)
            member.save()

class Migration(migrations.Migration):
    dependencies = [
        ('salt', '0003_alter_member_full_name_alter_member_roles_and_more'),
    ]

    operations = [
        migrations.RunPython(convert_roles_to_list, convert_roles_to_string),
    ] 