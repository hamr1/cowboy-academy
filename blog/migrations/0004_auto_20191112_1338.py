# Generated by Django 2.2.6 on 2019-11-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_menteeprofile_career_interest3'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorprofile',
            name='mentor_capacity',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=1, max_length=3, verbose_name='What is your maximum mentee threshold?'),
        ),
        migrations.AlterField(
            model_name='menteeprofile',
            name='career_interest1',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30, verbose_name='First Career Interest'),
        ),
        migrations.AlterField(
            model_name='menteeprofile',
            name='career_interest2',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30, verbose_name='Second Career Interest'),
        ),
        migrations.AlterField(
            model_name='menteeprofile',
            name='career_interest3',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship')], default='MGMT', max_length=30, verbose_name='Third Career Interest'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='career_expertise1',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship'), ('--', '--')], default='--', max_length=30, verbose_name='Career Expertise 1'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='career_expertise2',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship'), ('--', '--')], default='--', max_length=30, verbose_name='Career Expertise 2'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='career_expertise3',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship'), ('--', '--')], default='--', max_length=30, verbose_name='Career Expertise 3'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='career_expertise4',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship'), ('--', '--')], default='--', max_length=30, verbose_name='Career Expertise 4'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='career_expertise5',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship'), ('--', '--')], default='--', max_length=30, verbose_name='Career Expertise 5'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='career_expertise6',
            field=models.CharField(choices=[('Information Systems', 'Information Systems'), ('Supply Chain and Logistics', 'Supply Chain and Logistics'), ('Manufacturing Engineering', 'Manufacturing Engineering'), ('Project Management', 'Project Management'), ('Quality Management', 'Quality Management'), ('Research and Development', 'Research and Development'), ('Production Control', 'Production Control'), ('Environmental Management', 'Environmental Management'), ('Hiring and Recruiting', 'Hiring and Recruiting'), ('Optimization', 'Optimization'), ('Consulting', 'Consulting'), ('Sales and Marketing', 'Sales and Marketing'), ('Entrepeneurship', 'Entrepeneurship'), ('--', '--')], default='--', max_length=30, verbose_name='Career Expertise 6'),
        ),
    ]
