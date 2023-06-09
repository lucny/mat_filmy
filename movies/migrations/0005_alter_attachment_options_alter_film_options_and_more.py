# Generated by Django 4.0.4 on 2023-04-22 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_film_poster'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'ordering': ['-last_update', 'type'], 'verbose_name': 'Příloha', 'verbose_name_plural': 'Přílohy'},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['-release_date', 'title'], 'verbose_name': 'Film', 'verbose_name_plural': 'Filmy'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name'], 'verbose_name': 'Žánr', 'verbose_name_plural': 'Žánry'},
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Zadejte křestní jméno umělce', max_length=50, verbose_name='Jméno')),
                ('second_name', models.CharField(help_text='Zadejte příjmení umělce', max_length=50, verbose_name='Příjmení')),
                ('birth', models.DateField(help_text='Zadejte datum narození umělce', verbose_name='Datum narození')),
                ('photo', models.ImageField(blank=True, help_text='Vložte fotku umělce', null=True, upload_to='artists', verbose_name='Fotka')),
                ('bio', models.TextField(blank=True, help_text='Napište informace o životě umělce', null=True, verbose_name='Životopis')),
                ('gender', models.CharField(choices=[('muž', 'Muž'), ('žena', 'Žena'), ('jiné', 'Jiné')], default='žena', help_text='Zadejte pohlaví umělce', max_length=10, verbose_name='Pohlaví')),
                ('film', models.ManyToManyField(help_text='Vyberte filmy spojené s umělcem', to='movies.film', verbose_name='Název filmu')),
            ],
            options={
                'verbose_name': 'Umělec',
                'verbose_name_plural': 'Umělci',
                'ordering': ['-birth', 'second_name'],
            },
        ),
    ]
