# Generated by Django 5.1.1 on 2024-10-09 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_question', '0010_alter_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='ml_question.chapter'),
        ),
    ]
