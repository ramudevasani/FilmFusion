# Generated by Django 4.2.5 on 2023-11-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.CharField(choices=[(1, 'A1'), (1, 'B1'), (1, 'C1'), (1, 'D1'), (1, 'E1'), (1, 'F1'), (1, 'G1'), (1, 'H1'), (1, 'I1'), (1, 'J1'), (2, 'A2'), (2, 'B2'), (2, 'C2'), (2, 'D2'), (2, 'E2'), (2, 'F2'), (2, 'G2'), (2, 'H2'), (2, 'I2'), (2, 'J2'), (3, 'A3'), (3, 'B3'), (3, 'C3'), (3, 'D3'), (3, 'E3'), (3, 'F3'), (3, 'G3'), (3, 'H3'), (3, 'I3'), (3, 'J3'), (4, 'A4'), (4, 'B4'), (4, 'C4'), (4, 'D4'), (4, 'E4'), (4, 'F4'), (4, 'G4'), (4, 'H4'), (4, 'I4'), (4, 'J4'), (5, 'A5'), (5, 'B5'), (5, 'C5'), (5, 'D5'), (5, 'E5'), (5, 'F5'), (5, 'G5'), (5, 'H5'), (5, 'I5'), (5, 'J5'), (6, 'A6'), (6, 'B6'), (6, 'C6'), (6, 'D6'), (6, 'E6'), (6, 'F6'), (6, 'G6'), (6, 'H6'), (6, 'I6'), (6, 'J6'), (7, 'A7'), (7, 'B7'), (7, 'C7'), (7, 'D7'), (7, 'E7'), (7, 'F7'), (7, 'G7'), (7, 'H7'), (7, 'I7'), (7, 'J7'), (8, 'A8'), (8, 'B8'), (8, 'C8'), (8, 'D8'), (8, 'E8'), (8, 'F8'), (8, 'G8'), (8, 'H8'), (8, 'I8'), (8, 'J8'), (9, 'A9'), (9, 'B9'), (9, 'C9'), (9, 'D9'), (9, 'E9'), (9, 'F9'), (9, 'G9'), (9, 'H9'), (9, 'I9'), (9, 'J9'), (10, 'A10'), (10, 'B10'), (10, 'C10'), (10, 'D10'), (10, 'E10'), (10, 'F10'), (10, 'G10'), (10, 'H10'), (10, 'I10'), (10, 'J10')], max_length=3),
        ),
    ]
