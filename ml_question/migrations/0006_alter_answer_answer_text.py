# Generated by Django 5.1.1 on 2024-09-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_question', '0004_chapter_remove_question_correct_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(max_length=500),
        ),
    ]
