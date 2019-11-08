# Generated by Django 2.2.6 on 2019-10-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menteeprofile',
            old_name='career_interest',
            new_name='career_interest1',
        ),
        migrations.RenameField(
            model_name='mentorprofile',
            old_name='career_interest',
            new_name='career_expertise1',
        ),
        migrations.AddField(
            model_name='menteeprofile',
            name='career_interest2',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='career_expertise2',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='career_expertise3',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='career_expertise4',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='career_expertise5',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='career_expertise6',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_mentee',
            field=models.BooleanField(default=False, verbose_name='Mentee'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_mentor',
            field=models.BooleanField(default=False, verbose_name='Mentor'),
        ),
    ]