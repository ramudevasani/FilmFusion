# Generated by Django 4.2.5 on 2023-11-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.CharField(choices=[('A1', 'A1'), ('B1', 'B1'), ('C1', 'C1'), ('D1', 'D1'), ('E1', 'E1'), ('F1', 'F1'), ('G1', 'G1'), ('H1', 'H1'), ('I1', 'I1'), ('J1', 'J1'), ('A2', 'A2'), ('B2', 'B2'), ('C2', 'C2'), ('D2', 'D2'), ('E2', 'E2'), ('F2', 'F2'), ('G2', 'G2'), ('H2', 'H2'), ('I2', 'I2'), ('J2', 'J2'), ('A3', 'A3'), ('B3', 'B3'), ('C3', 'C3'), ('D3', 'D3'), ('E3', 'E3'), ('F3', 'F3'), ('G3', 'G3'), ('H3', 'H3'), ('I3', 'I3'), ('J3', 'J3'), ('A4', 'A4'), ('B4', 'B4'), ('C4', 'C4'), ('D4', 'D4'), ('E4', 'E4'), ('F4', 'F4'), ('G4', 'G4'), ('H4', 'H4'), ('I4', 'I4'), ('J4', 'J4'), ('A5', 'A5'), ('B5', 'B5'), ('C5', 'C5'), ('D5', 'D5'), ('E5', 'E5'), ('F5', 'F5'), ('G5', 'G5'), ('H5', 'H5'), ('I5', 'I5'), ('J5', 'J5'), ('A6', 'A6'), ('B6', 'B6'), ('C6', 'C6'), ('D6', 'D6'), ('E6', 'E6'), ('F6', 'F6'), ('G6', 'G6'), ('H6', 'H6'), ('I6', 'I6'), ('J6', 'J6'), ('A7', 'A7'), ('B7', 'B7'), ('C7', 'C7'), ('D7', 'D7'), ('E7', 'E7'), ('F7', 'F7'), ('G7', 'G7'), ('H7', 'H7'), ('I7', 'I7'), ('J7', 'J7'), ('A8', 'A8'), ('B8', 'B8'), ('C8', 'C8'), ('D8', 'D8'), ('E8', 'E8'), ('F8', 'F8'), ('G8', 'G8'), ('H8', 'H8'), ('I8', 'I8'), ('J8', 'J8'), ('A9', 'A9'), ('B9', 'B9'), ('C9', 'C9'), ('D9', 'D9'), ('E9', 'E9'), ('F9', 'F9'), ('G9', 'G9'), ('H9', 'H9'), ('I9', 'I9'), ('J9', 'J9'), ('A0', 'A0'), ('B0', 'B0'), ('C0', 'C0'), ('D0', 'D0'), ('E0', 'E0'), ('F0', 'F0'), ('G0', 'G0'), ('H0', 'H0'), ('I0', 'I0'), ('J0', 'J0'), ('A1', 'A1'), ('B1', 'B1'), ('C1', 'C1'), ('D1', 'D1'), ('E1', 'E1'), ('F1', 'F1'), ('G1', 'G1'), ('H1', 'H1'), ('I1', 'I1'), ('J1', 'J1'), ('A2', 'A2'), ('B2', 'B2'), ('C2', 'C2'), ('D2', 'D2'), ('E2', 'E2'), ('F2', 'F2'), ('G2', 'G2'), ('H2', 'H2'), ('I2', 'I2'), ('J2', 'J2'), ('A3', 'A3'), ('B3', 'B3'), ('C3', 'C3'), ('D3', 'D3'), ('E3', 'E3'), ('F3', 'F3'), ('G3', 'G3'), ('H3', 'H3'), ('I3', 'I3'), ('J3', 'J3'), ('A4', 'A4'), ('B4', 'B4'), ('C4', 'C4'), ('D4', 'D4'), ('E4', 'E4'), ('F4', 'F4'), ('G4', 'G4'), ('H4', 'H4'), ('I4', 'I4'), ('J4', 'J4'), ('A5', 'A5'), ('B5', 'B5'), ('C5', 'C5'), ('D5', 'D5'), ('E5', 'E5'), ('F5', 'F5'), ('G5', 'G5'), ('H5', 'H5'), ('I5', 'I5'), ('J5', 'J5'), ('A6', 'A6'), ('B6', 'B6'), ('C6', 'C6'), ('D6', 'D6'), ('E6', 'E6'), ('F6', 'F6'), ('G6', 'G6'), ('H6', 'H6'), ('I6', 'I6'), ('J6', 'J6'), ('A7', 'A7'), ('B7', 'B7'), ('C7', 'C7'), ('D7', 'D7'), ('E7', 'E7'), ('F7', 'F7'), ('G7', 'G7'), ('H7', 'H7'), ('I7', 'I7'), ('J7', 'J7'), ('A8', 'A8'), ('B8', 'B8'), ('C8', 'C8'), ('D8', 'D8'), ('E8', 'E8'), ('F8', 'F8'), ('G8', 'G8'), ('H8', 'H8'), ('I8', 'I8'), ('J8', 'J8'), ('A9', 'A9'), ('B9', 'B9'), ('C9', 'C9'), ('D9', 'D9'), ('E9', 'E9'), ('F9', 'F9'), ('G9', 'G9'), ('H9', 'H9'), ('I9', 'I9'), ('J9', 'J9'), ('A0', 'A0'), ('B0', 'B0'), ('C0', 'C0'), ('D0', 'D0'), ('E0', 'E0'), ('F0', 'F0'), ('G0', 'G0'), ('H0', 'H0'), ('I0', 'I0'), ('J0', 'J0'), ('A1', 'A1'), ('B1', 'B1'), ('C1', 'C1'), ('D1', 'D1'), ('E1', 'E1'), ('F1', 'F1'), ('G1', 'G1'), ('H1', 'H1'), ('I1', 'I1'), ('J1', 'J1'), ('A2', 'A2'), ('B2', 'B2'), ('C2', 'C2'), ('D2', 'D2'), ('E2', 'E2'), ('F2', 'F2'), ('G2', 'G2'), ('H2', 'H2'), ('I2', 'I2'), ('J2', 'J2'), ('A3', 'A3'), ('B3', 'B3'), ('C3', 'C3'), ('D3', 'D3'), ('E3', 'E3'), ('F3', 'F3'), ('G3', 'G3'), ('H3', 'H3'), ('I3', 'I3'), ('J3', 'J3'), ('A4', 'A4'), ('B4', 'B4'), ('C4', 'C4'), ('D4', 'D4'), ('E4', 'E4'), ('F4', 'F4'), ('G4', 'G4'), ('H4', 'H4'), ('I4', 'I4'), ('J4', 'J4'), ('A5', 'A5'), ('B5', 'B5'), ('C5', 'C5'), ('D5', 'D5'), ('E5', 'E5'), ('F5', 'F5'), ('G5', 'G5'), ('H5', 'H5'), ('I5', 'I5'), ('J5', 'J5'), ('A6', 'A6'), ('B6', 'B6'), ('C6', 'C6'), ('D6', 'D6'), ('E6', 'E6'), ('F6', 'F6'), ('G6', 'G6'), ('H6', 'H6'), ('I6', 'I6'), ('J6', 'J6'), ('A7', 'A7'), ('B7', 'B7'), ('C7', 'C7'), ('D7', 'D7'), ('E7', 'E7'), ('F7', 'F7'), ('G7', 'G7'), ('H7', 'H7'), ('I7', 'I7'), ('J7', 'J7'), ('A8', 'A8'), ('B8', 'B8'), ('C8', 'C8'), ('D8', 'D8'), ('E8', 'E8'), ('F8', 'F8'), ('G8', 'G8'), ('H8', 'H8'), ('I8', 'I8'), ('J8', 'J8'), ('A9', 'A9'), ('B9', 'B9'), ('C9', 'C9'), ('D9', 'D9'), ('E9', 'E9'), ('F9', 'F9'), ('G9', 'G9'), ('H9', 'H9'), ('I9', 'I9'), ('J9', 'J9'), ('A0', 'A0'), ('B0', 'B0'), ('C0', 'C0'), ('D0', 'D0'), ('E0', 'E0'), ('F0', 'F0'), ('G0', 'G0'), ('H0', 'H0'), ('I0', 'I0'), ('J0', 'J0'), ('A1', 'A1'), ('B1', 'B1'), ('C1', 'C1'), ('D1', 'D1'), ('E1', 'E1'), ('F1', 'F1'), ('G1', 'G1'), ('H1', 'H1'), ('I1', 'I1'), ('J1', 'J1'), ('A2', 'A2'), ('B2', 'B2'), ('C2', 'C2'), ('D2', 'D2'), ('E2', 'E2'), ('F2', 'F2'), ('G2', 'G2'), ('H2', 'H2'), ('I2', 'I2'), ('J2', 'J2'), ('A3', 'A3'), ('B3', 'B3'), ('C3', 'C3'), ('D3', 'D3'), ('E3', 'E3'), ('F3', 'F3'), ('G3', 'G3'), ('H3', 'H3'), ('I3', 'I3'), ('J3', 'J3'), ('A4', 'A4'), ('B4', 'B4'), ('C4', 'C4'), ('D4', 'D4'), ('E4', 'E4'), ('F4', 'F4'), ('G4', 'G4'), ('H4', 'H4'), ('I4', 'I4'), ('J4', 'J4'), ('A5', 'A5'), ('B5', 'B5'), ('C5', 'C5'), ('D5', 'D5'), ('E5', 'E5'), ('F5', 'F5'), ('G5', 'G5'), ('H5', 'H5'), ('I5', 'I5'), ('J5', 'J5'), ('A6', 'A6'), ('B6', 'B6'), ('C6', 'C6'), ('D6', 'D6'), ('E6', 'E6'), ('F6', 'F6'), ('G6', 'G6'), ('H6', 'H6'), ('I6', 'I6'), ('J6', 'J6'), ('A7', 'A7'), ('B7', 'B7'), ('C7', 'C7'), ('D7', 'D7'), ('E7', 'E7'), ('F7', 'F7'), ('G7', 'G7'), ('H7', 'H7'), ('I7', 'I7'), ('J7', 'J7'), ('A8', 'A8'), ('B8', 'B8'), ('C8', 'C8'), ('D8', 'D8'), ('E8', 'E8'), ('F8', 'F8'), ('G8', 'G8'), ('H8', 'H8'), ('I8', 'I8'), ('J8', 'J8'), ('A9', 'A9'), ('B9', 'B9'), ('C9', 'C9'), ('D9', 'D9'), ('E9', 'E9'), ('F9', 'F9'), ('G9', 'G9'), ('H9', 'H9'), ('I9', 'I9'), ('J9', 'J9'), ('A0', 'A0'), ('B0', 'B0'), ('C0', 'C0'), ('D0', 'D0'), ('E0', 'E0'), ('F0', 'F0'), ('G0', 'G0'), ('H0', 'H0'), ('I0', 'I0'), ('J0', 'J0'), ('A1', 'A1'), ('B1', 'B1'), ('C1', 'C1'), ('D1', 'D1'), ('E1', 'E1'), ('F1', 'F1'), ('G1', 'G1'), ('H1', 'H1'), ('I1', 'I1'), ('J1', 'J1'), ('A2', 'A2'), ('B2', 'B2'), ('C2', 'C2'), ('D2', 'D2'), ('E2', 'E2'), ('F2', 'F2'), ('G2', 'G2'), ('H2', 'H2'), ('I2', 'I2'), ('J2', 'J2'), ('A3', 'A3'), ('B3', 'B3'), ('C3', 'C3'), ('D3', 'D3'), ('E3', 'E3'), ('F3', 'F3'), ('G3', 'G3'), ('H3', 'H3'), ('I3', 'I3'), ('J3', 'J3'), ('A4', 'A4'), ('B4', 'B4'), ('C4', 'C4'), ('D4', 'D4'), ('E4', 'E4'), ('F4', 'F4'), ('G4', 'G4'), ('H4', 'H4'), ('I4', 'I4'), ('J4', 'J4'), ('A5', 'A5'), ('B5', 'B5'), ('C5', 'C5'), ('D5', 'D5'), ('E5', 'E5'), ('F5', 'F5'), ('G5', 'G5'), ('H5', 'H5'), ('I5', 'I5'), ('J5', 'J5'), ('A6', 'A6'), ('B6', 'B6'), ('C6', 'C6'), ('D6', 'D6'), ('E6', 'E6'), ('F6', 'F6'), ('G6', 'G6'), ('H6', 'H6'), ('I6', 'I6'), ('J6', 'J6'), ('A7', 'A7'), ('B7', 'B7'), ('C7', 'C7'), ('D7', 'D7'), ('E7', 'E7'), ('F7', 'F7'), ('G7', 'G7'), ('H7', 'H7'), ('I7', 'I7'), ('J7', 'J7'), ('A8', 'A8'), ('B8', 'B8'), ('C8', 'C8'), ('D8', 'D8'), ('E8', 'E8'), ('F8', 'F8'), ('G8', 'G8'), ('H8', 'H8'), ('I8', 'I8'), ('J8', 'J8'), ('A9', 'A9'), ('B9', 'B9'), ('C9', 'C9'), ('D9', 'D9'), ('E9', 'E9'), ('F9', 'F9'), ('G9', 'G9'), ('H9', 'H9'), ('I9', 'I9'), ('J9', 'J9'), ('A0', 'A0'), ('B0', 'B0'), ('C0', 'C0'), ('D0', 'D0'), ('E0', 'E0'), ('F0', 'F0'), ('G0', 'G0'), ('H0', 'H0'), ('I0', 'I0'), ('J0', 'J0')], max_length=3),
        ),
    ]
