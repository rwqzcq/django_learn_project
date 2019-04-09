# Generated by Django 2.2 on 2019-04-08 14:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Fiction', '0006_notice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name_plural': '章节管理'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name_plural': '公告管理'},
        ),
        migrations.AlterModelOptions(
            name='novel',
            options={'verbose_name_plural': '小说管理'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name_plural': '类型管理'},
        ),
        migrations.AlterField(
            model_name='chapter',
            name='adder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='添加人'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='章节内容'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='create_time',
            field=models.DateField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='intro',
            field=models.TextField(verbose_name='章节概要'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(max_length=32, verbose_name='章节名称'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='novel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Fiction.Novel', verbose_name='小说名'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='status',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='update_time',
            field=models.DateField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='adder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='添加人'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='create_time',
            field=models.DateField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=32, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='adder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='添加人'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='author',
            field=models.CharField(max_length=32, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='create_time',
            field=models.DateField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='img',
            field=models.ImageField(null=True, upload_to='novels', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='name',
            field=models.CharField(max_length=32, verbose_name='小说名'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='novel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Fiction.Type', verbose_name='小说类型'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='update_time',
            field=models.DateField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.CharField(max_length=32, verbose_name='类型名称'),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Fiction.Novel', verbose_name='小说名')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='收藏人')),
            ],
            options={
                'verbose_name_plural': '收藏管理',
            },
        ),
    ]