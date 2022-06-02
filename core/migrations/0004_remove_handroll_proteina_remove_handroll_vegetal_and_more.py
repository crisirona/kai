# Generated by Django 4.0.4 on 2022-06-01 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_agregadoalmuerzo_basebowl_cortekai_extrabowl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handroll',
            name='proteina',
        ),
        migrations.RemoveField(
            model_name='handroll',
            name='vegetal',
        ),
        migrations.RemoveField(
            model_name='handrollready',
            name='proteina',
        ),
        migrations.RemoveField(
            model_name='handrollready',
            name='vegetal',
        ),
        migrations.AddField(
            model_name='handroll',
            name='proteina1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Handroll.proteina1+', to='core.proteinahandroll'),
        ),
        migrations.AddField(
            model_name='handroll',
            name='proteina2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Handroll.proteina2+', to='core.proteinahandroll'),
        ),
        migrations.AddField(
            model_name='handroll',
            name='proteina3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Handroll.proteina3+', to='core.proteinahandroll'),
        ),
        migrations.AddField(
            model_name='handroll',
            name='vegetal1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Handroll.vegetal1+', to='core.vegetaleshandroll'),
        ),
        migrations.AddField(
            model_name='handroll',
            name='vegetal2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Handroll.vegetal2+', to='core.vegetaleshandroll'),
        ),
        migrations.AddField(
            model_name='handroll',
            name='vegetal3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Handroll.vegetal3+', to='core.vegetaleshandroll'),
        ),
        migrations.AddField(
            model_name='handrollready',
            name='proteina1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HandrollReady.proteina1+', to='core.proteinahandroll'),
        ),
        migrations.AddField(
            model_name='handrollready',
            name='proteina2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HandrollReady.proteina2+', to='core.proteinahandroll'),
        ),
        migrations.AddField(
            model_name='handrollready',
            name='proteina3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HandrollReady.proteina3+', to='core.proteinahandroll'),
        ),
        migrations.AddField(
            model_name='handrollready',
            name='vegetal1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HandrollReady.vegetal1+', to='core.vegetaleshandroll'),
        ),
        migrations.AddField(
            model_name='handrollready',
            name='vegetal2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HandrollReady.vegatal2+', to='core.vegetaleshandroll'),
        ),
        migrations.AddField(
            model_name='handrollready',
            name='vegetal3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HandrollReady.vegetal3+', to='core.vegetaleshandroll'),
        ),
        migrations.CreateModel(
            name='Almuerzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agregado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.agregadoalmuerzo')),
                ('proteina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.proteinaalmuerzo')),
            ],
        ),
    ]
