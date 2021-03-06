# Generated by Django 3.1.7 on 2021-08-01 00:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonUser',
            fields=[
                ('commonUserID', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('commonUserName', models.CharField(max_length=25)),
                ('level', models.CharField(choices=[(1, 'Level1'), (2, 'Level2'), (3, 'Level3'), (4, 'Level4')], default='Level1', max_length=20)),
                ('imageLocation', models.TextField()),
                ('continueCheckDays', models.IntegerField(default=0)),
                ('lastCheckDate', models.DateField()),
            ],
            options={
                'verbose_name': 'CommonUsers',
                'verbose_name_plural': 'CommonUsers',
                'db_table': 'CommonUser',
            },
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('conceptID', models.AutoField(primary_key=True, serialize=False)),
                ('conceptName', models.CharField(max_length=100, unique=True)),
                ('conceptDescription', models.TextField()),
            ],
            options={
                'db_table': 'Concept',
            },
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('exampleID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('example', models.TextField()),
                ('meaning', models.TextField()),
                ('translation', models.TextField()),
                ('level2Mode', models.BooleanField(default=1)),
                ('level3Mode', models.BooleanField(default=1)),
                ('level4Mode', models.BooleanField(default=1)),
                ('level5Mode', models.BooleanField(default=0)),
                ('level6Mode', models.BooleanField(default=0)),
                ('concept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='concept', to='questionRecord.concept')),
            ],
            options={
                'verbose_name': 'Examples',
                'verbose_name_plural': 'Examples',
                'db_table': 'Example',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('groupID', models.AutoField(primary_key=True)),
                ('groupName', models.TextField()),
            ],
            options={
                'verbose_name': 'Groups',
                'verbose_name_plural': 'Groups',
                'db_table': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='SubConcept',
            fields=[
                ('subConceptID', models.AutoField(primary_key=True, serialize=False)),
                ('subConceptName', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'SubConcept',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unitID', models.AutoField(primary_key=True, serialize=False)),
                ('unitName', models.TextField()),
            ],
            options={
                'db_table': 'Unit',
            },
        ),
        migrations.CreateModel(
            name='Wrong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[(1, 'Level1'), (2, 'Level2'), (3, 'Level3'), (4, 'Level4')], default='Level1', max_length=20)),
                ('questionID', models.CharField(max_length=25)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=1)),
                ('commonUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionRecord.commonuser')),
            ],
            options={
                'db_table': 'Wrong',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qstNum', models.IntegerField()),
                ('cumScore', models.IntegerField()),
                ('commonUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Progress', to='questionRecord.commonuser')),
            ],
            options={
                'verbose_name': 'Progresses',
                'verbose_name_plural': 'Progresses',
                'db_table': 'Progress',
            },
        ),
        migrations.CreateModel(
            name='NotesCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[(1, 'Level1'), (2, 'Level2'), (3, 'Level3'), (4, 'Level4')], default='Level1', max_length=20)),
                ('questionID', models.CharField(max_length=25)),
                ('commonUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionRecord.commonuser')),
            ],
            options={
                'verbose_name': 'NotesCollections',
                'verbose_name_plural': 'NotesCollections',
                'db_table': 'NotesCollection',
            },
        ),
        migrations.CreateModel(
            name='Level4',
            fields=[
                ('questionID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('example', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Level4', to='questionRecord.example')),
            ],
            options={
                'verbose_name': 'Level4Questions',
                'verbose_name_plural': 'Level4Questions',
                'db_table': 'Level4',
            },
        ),
        migrations.CreateModel(
            name='Level3',
            fields=[
                ('questionID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('op1', models.TextField()),
                ('op2', models.TextField()),
                ('op3', models.TextField()),
                ('example', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Level3', to='questionRecord.example')),
            ],
            options={
                'verbose_name': 'Level3Questions',
                'verbose_name_plural': 'Level3Questions',
                'db_table': 'Level3',
            },
        ),
        migrations.CreateModel(
            name='Level2',
            fields=[
                ('questionID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('op1', models.TextField()),
                ('op2', models.TextField()),
                ('op3', models.TextField()),
                ('example', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Level2', to='questionRecord.example')),
            ],
            options={
                'verbose_name': 'Level2Questions',
                'verbose_name_plural': 'Level2Questions',
                'db_table': 'Level2',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[(1, 'Level1'), (2, 'Level2'), (3, 'Level3'), (4, 'Level4')], default='Level1', max_length=20)),
                ('questionID', models.CharField(max_length=25)),
                ('commonUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='History', to='questionRecord.commonuser')),
            ],
            options={
                'verbose_name': 'Histories',
                'verbose_name_plural': 'Histories',
                'db_table': 'History',
            },
        ),
        migrations.AddField(
            model_name='example',
            name='subConcept1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Example1', to='questionRecord.subconcept'),
        ),
        migrations.AddField(
            model_name='example',
            name='subConcept2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Example2', to='questionRecord.subconcept'),
        ),
        migrations.AddField(
            model_name='example',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit', to='questionRecord.unit'),
        ),
        migrations.CreateModel(
            name='DailyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dailyGoalNum', models.IntegerField()),
                ('commonUserID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='DailyTask', to='questionRecord.commonuser')),
            ],
            options={
                'verbose_name': 'DailyTasks',
                'verbose_name_plural': 'DailyTasks',
                'db_table': 'DailyTask',
            },
        ),
        migrations.AddField(
            model_name='concept',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='concept', to='questionRecord.unit'),
        ),
        migrations.AddField(
            model_name='commonuser',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CommonUser', to='questionRecord.groups'),
        ),
    ]
