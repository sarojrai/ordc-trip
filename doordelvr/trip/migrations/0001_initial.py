# Generated by Django 2.2 on 2020-08-30 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0002_auto_20200830_1657'),
        ('shipment', '0002_auto_20200811_1613'),
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_ref_number', models.CharField(db_index=True, max_length=128)),
                ('trip_created_by', models.IntegerField(db_index=True)),
                ('trip_delivered_by', models.IntegerField(db_index=True, null=True)),
                ('trip_created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('trip_updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('trip_accepted_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('trip_started_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('trip_ended_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('start_km', models.FloatField(default=0)),
                ('end_km', models.FloatField(default=0)),
                ('shipment_handover_to', models.CharField(max_length=128)),
                ('number_of_items', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'CANCELED'), (1, 'CREATED'), (2, 'STARTED'), (3, 'COMPLETED'), (4, 'INPROGRESS'), (5, 'ACCEPTED'), (6, 'REJECTED'), (7, 'BROADCASTED')], default=1)),
                ('total_weight', models.FloatField(default=0)),
                ('total_delivery_value', models.FloatField(default=0)),
                ('trip_charge', models.FloatField(default=0)),
                ('trip_discount', models.FloatField(default=0)),
                ('gst_type', models.CharField(default='OTHER', max_length=50)),
                ('gst_percentage', models.FloatField(default=0)),
                ('cgst', models.FloatField(default=0)),
                ('sgst', models.FloatField(default=0)),
                ('igst', models.FloatField(default=0)),
                ('gst_charge', models.FloatField(default=0)),
                ('flat_surchage', models.FloatField(default=0)),
                ('surchage_percentage', models.FloatField(default=0)),
                ('percentage_surchage', models.FloatField(default=0)),
                ('gross_total_charge', models.FloatField(default=0)),
                ('notification_status', models.BooleanField(default=False)),
                ('shipment', models.ManyToManyField(to='shipment.Shipment')),
                ('trip_drop_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trip_drop_address', to='location.Address')),
                ('trip_pickup_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trip_pickup_address', to='location.Address')),
                ('trip_via', models.ManyToManyField(default=True, to='location.Area')),
                ('vehicle_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.VehicleCategory')),
            ],
        ),
    ]
