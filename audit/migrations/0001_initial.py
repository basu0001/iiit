# Generated by Django 2.2.5 on 2019-11-05 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('soc_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('net_amount_issued', models.IntegerField()),
                ('amount_left', models.IntegerField()),
                ('dues', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Secretaries',
            fields=[
                ('sec_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('type_of_account', models.CharField(max_length=1, null=True)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=64)),
                ('soc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Society')),
            ],
        ),
        migrations.CreateModel(
            name='Proposals',
            fields=[
                ('proposal_no', models.IntegerField(primary_key=True, serialize=False)),
                ('net_amount_left', models.IntegerField()),
                ('amount_asked_for', models.IntegerField()),
                ('amount_returned', models.IntegerField()),
                ('purpose', models.CharField(max_length=200)),
                ('sec_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Secretaries')),
                ('soc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Society')),
            ],
        ),
    ]