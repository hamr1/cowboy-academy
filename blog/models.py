from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver



# Create your models here.
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')

#class User(AbstractUser):
#    is_student = models.BooleanField('student status', default=False)
#    is_teacher = models.BooleanField('teacher status', default=False)

class UserProfile(models.Model):

    STATE_CHOICES = [('AL', 'Alabama'), ('AK', 'Alaska'), 
    ('AS', 'American Samoa'), ('AZ', 'Arizona'), 
    ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'),
    ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), 
    ('CA', 'California'), ('CO', 'Colorado'),
    ('CT', 'Connecticut'), ('DE', 'Delaware'), 
    ('DC', 'District of Columbia'), ('FL', 'Florida'), 
    ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), 
    ('ID', 'Idaho'), ('IL', 'Illinois'), 
    ('IN', 'Indiana'), ('IA', 'Iowa'), 
    ('KS', 'Kansas'), ('KY', 'Kentucky'), 
    ('LA', 'Louisiana'), ('ME', 'Maine'), 
    ('MD', 'Maryland'), ('MA', 'Massachusetts'),
    ('MI', 'Michigan'), ('MN', 'Minnesota'), 
    ('MS', 'Mississippi'), ('MO', 'Missouri'), 
    ('MT', 'Montana'), ('NE', 'Nebraska'), 
    ('NV', 'Nevada'), ('NH', 'New Hampshire'), 
    ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
    ('NY', 'New York'), ('NC', 'North Carolina'), 
    ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'),
    ('OH', 'Ohio'), ('OK', 'Oklahoma'), 
    ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'), ('SD', 'South Dakota'), 
    ('TN', 'Tennessee'), ('TX', 'Texas'), 
    ('UT', 'Utah'), ('VT', 'Vermont'), 
    ('VI', 'Virgin Islands'), ('VA', 'Virginia'),
    ('WA', 'Washington'), ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'), ('WY', 'Wyoming')]
    
    CAREER_CHOICES = [
        ('Information Systems', 'Information Systems'),
        ('Supply Chain and Logistics', 'Supply Chain and Logistics'),
        ('Manufacturing Engineering', 'Manufacturing Engineering'),
        ('Project Management', 'Project Management'),
        ('Quality Management', 'Quality Management'),
        ('Research and Development', 'Research and Development'),
        ('Production Control', 'Production Control'),
        ('Environmental Management', 'Environmental Management'),
        ('Hiring and Recruiting', 'Hiring and Recruiting'),
        ('Optimization', 'Optimization'),
        ('Consulting', 'Consulting'),
        ('Sales and Marketing', 'Sales and Marketing'),
        ('Entrepeneurship', 'Entrepeneurship')

    ]

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default ='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='', blank = True)
    phone = models.IntegerField(default='0')
    state = models.CharField(max_length=30, choices=STATE_CHOICES, default='OK')
    image = models.ImageField(upload_to='profile_image', blank=True )
    career_interest = models.CharField(max_length=30, default='MGMT', choices=CAREER_CHOICES)


    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)