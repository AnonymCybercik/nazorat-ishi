# Generated by Django 3.1.2 on 2020-11-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0021_student_is_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinflarfanlar',
            name='fanlar',
            field=models.CharField(choices=[('Ona tili', 'Ona tili'), ('Adabiyot', 'Adabiyot'), ('Fizika', 'Fizika'), ('Algebra', 'Algebra'), ('Rus tili', 'Rus tili'), ('Kimyo', 'Kimyo'), ('Biologiya', 'Biologiya'), ('Informatika', 'Informatika'), ('Ingliz tili', 'Ingliz tili'), ('Geometriya', 'Geometriya'), ('Huquq', 'Huquq'), ('Tarix', 'Tarix')], max_length=30, null=True),
        ),
    ]
