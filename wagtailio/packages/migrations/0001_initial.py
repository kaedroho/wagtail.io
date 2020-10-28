# Generated by Django 2.2.13 on 2020-10-27 21:17

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('images', '0010_add_duplicatefindingmixin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('uid', models.IntegerField(editable=False, help_text='The DjangoPackages.org id', unique=True)),
                ('repo_url', models.URLField(blank=True)),
                ('pypi_version', models.CharField(blank=True, max_length=255)),
                ('repo_forks', models.IntegerField(blank=True, null=True)),
                ('repo_description', models.TextField(blank=True)),
                ('pypi_url', models.URLField(blank=True)),
                ('documentation_url', models.URLField(blank=True)),
                ('repo_watchers', models.IntegerField(blank=True, null=True)),
                ('participants', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='PackagesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, help_text='Description of this page as it should appear when shared on social networks, or in Google results', max_length=255, verbose_name='Meta description')),
                ('listing_intro', models.TextField(blank=True, help_text='Summary of this page to display when this is linked from elsewhere in the site.')),
                ('subtitle', models.CharField(max_length=255)),
                ('listing_image', models.ForeignKey(blank=True, help_text='Image to display along with summary, when this page is linked from elsewhere in the site.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.WagtailIOImage')),
                ('social_image', models.ForeignKey(blank=True, help_text="Image to appear alongside 'Meta description', particularly for sharing on social networks", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.WagtailIOImage', verbose_name='Meta image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('uid', models.IntegerField(editable=False, help_text='The DjangoPackages.org id', unique=True)),
                ('packages', models.ManyToManyField(blank=True, to='packages.Package')),
            ],
        ),
    ]
