# Generated by Django 3.2.4 on 2021-08-11 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AflowStructure',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('structure_string', models.TextField()),
                ('nsites', models.IntegerField()),
                ('nelements', models.IntegerField()),
                ('chemical_system', models.CharField(max_length=25)),
                ('density', models.FloatField()),
                ('molar_volume', models.FloatField()),
                ('formula_full', models.CharField(max_length=50)),
                ('formula_reduced', models.CharField(max_length=50)),
                ('formula_anonymous', models.CharField(max_length=50)),
                ('spacegroup', models.IntegerField()),
                ('final_energy', models.FloatField(blank=True, null=True)),
                ('final_energy_per_atom', models.FloatField(blank=True, null=True)),
                ('formation_energy_per_atom', models.FloatField(blank=True, null=True)),
                ('band_gap', models.FloatField(blank=True, null=True)),
                ('energy_above_hull', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CodStructure',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('structure_string', models.TextField()),
                ('nsites', models.IntegerField()),
                ('nelements', models.IntegerField()),
                ('density', models.FloatField()),
                ('molar_volume', models.FloatField()),
                ('spacegroup', models.IntegerField()),
                ('chemical_system', models.TextField()),
                ('formula_full', models.TextField()),
                ('formula_reduced', models.TextField()),
                ('formula_anonymous', models.TextField()),
                ('is_ordered', models.BooleanField()),
                ('has_implicit_hydrogens', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JarvisStructure',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('structure_string', models.TextField()),
                ('nsites', models.IntegerField()),
                ('nelements', models.IntegerField()),
                ('chemical_system', models.CharField(max_length=25)),
                ('density', models.FloatField()),
                ('molar_volume', models.FloatField()),
                ('formula_full', models.CharField(max_length=50)),
                ('formula_reduced', models.CharField(max_length=50)),
                ('formula_anonymous', models.CharField(max_length=50)),
                ('spacegroup', models.IntegerField()),
                ('formation_energy_per_atom', models.FloatField(blank=True, null=True)),
                ('energy_above_hull', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaterialsProjectStructure',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('structure_string', models.TextField()),
                ('nsites', models.IntegerField()),
                ('nelements', models.IntegerField()),
                ('chemical_system', models.CharField(max_length=25)),
                ('density', models.FloatField()),
                ('molar_volume', models.FloatField()),
                ('formula_full', models.CharField(max_length=50)),
                ('formula_reduced', models.CharField(max_length=50)),
                ('formula_anonymous', models.CharField(max_length=50)),
                ('spacegroup', models.IntegerField()),
                ('final_energy', models.FloatField(blank=True, null=True)),
                ('final_energy_per_atom', models.FloatField(blank=True, null=True)),
                ('formation_energy_per_atom', models.FloatField(blank=True, null=True)),
                ('energy_above_hull', models.FloatField(blank=True, null=True)),
                ('band_gap', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OqmdStructure',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('structure_string', models.TextField()),
                ('nsites', models.IntegerField()),
                ('nelements', models.IntegerField()),
                ('chemical_system', models.CharField(max_length=25)),
                ('density', models.FloatField()),
                ('molar_volume', models.FloatField()),
                ('formula_full', models.CharField(max_length=50)),
                ('formula_reduced', models.CharField(max_length=50)),
                ('formula_anonymous', models.CharField(max_length=50)),
                ('spacegroup', models.IntegerField()),
                ('final_energy', models.FloatField(blank=True, null=True)),
                ('energy_above_hull', models.FloatField(blank=True, null=True)),
                ('band_gap', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
