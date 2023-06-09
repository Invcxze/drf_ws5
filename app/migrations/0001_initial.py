# Generated by Django 4.1.7 on 2023-03-21 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusorder', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Статус Заказа',
                'verbose_name_plural': 'Статус Заказов',
            },
        ),
        migrations.CreateModel(
            name='StatusOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statuspet', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Статус',
            },
        ),
        migrations.CreateModel(
            name='TypeOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typepet', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тип',
            },
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.URLField(blank=True, default=None)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categ', to='app.category')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stat', to='app.statusof')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='app.typeof')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
        migrations.CreateModel(
            name='OrderOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('datetime', models.DateTimeField(default=None)),
                ('is_complete', models.BooleanField(default=False)),
                ('ordernum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pets')),
                ('ordstatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.orderstatus')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
