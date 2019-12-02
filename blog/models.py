from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models import Count

# Create your models here.
#class UserProfileManager(models.Manager):
#    def get_queryset(self):
#        return super(UserProfileManager, self).get_queryset().filter(city='London')

class User(AbstractUser):
    is_mentor = models.BooleanField('Mentor', default=False)
    is_mentee = models.BooleanField('Mentee', default=False)

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

    description = models.CharField(max_length=100, default ='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='', blank = True)
    phone = models.IntegerField(default='0')
    state = models.CharField(max_length=30, choices=STATE_CHOICES, default='OK')
    image = models.ImageField(upload_to='profile_image', blank=True )

    # @classmethod
    # def get_connections(self):
    #     user = self.user
    #     return Connections.objects.filter(Q(creator=user)|Q(Connection=user))
        
    # mentees_count = device.objects.annotate(num=Count('Connections'))

# class Connection(models.Model):
# """ Model to represent Friendships """
#     to_user = models.ForeignKey(AUTH_USER_MODEL, models.CASCADE, related_name='friends')
#     from_user = models.ForeignKey(AUTH_USER_MODEL, models.CASCADE, related_name='_unused_friend_relation')

class MentorProfile(models.Model):
    # INTEGER_CHOICES= [tuple([x,x]) for x in range(1,7)]
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    capacity = models.BooleanField('MentorCapacity', default=False)

#     def current_load(): #define function that counts how many mentees a mentor has
#         count(MentorProfile.mentees)   #need a varaible that counts how many mentees currently assigned

#     def capacity_remain(): #define function that subtracts capacity from current load
#         capacity_remaining=(capacity-current_load)  #need a variable that says how much capacity is remaining

#     def at_capacity(request): #create boolean trigger that shows if mentor is at capacity or not
#         if capacity_remaining=0:
#             at_capacity=True
#         else:
#             at_capacity= False

#     questions = Question.objects.annotate(number_of_mentees=Count('answer')) 

    AREA_OF_EXPERTISE = [
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
        ('Entrepeneurship', 'Entrepeneurship'),
        ('--', '--')
    ]
    
    career_expertise1 = models.CharField(max_length=30, default='--', choices=AREA_OF_EXPERTISE, verbose_name='Career Expertise 1')
    career_expertise2 = models.CharField(max_length=30, default='--', choices=AREA_OF_EXPERTISE, verbose_name='Career Expertise 2')
    career_expertise3 = models.CharField(max_length=30, default='--', choices=AREA_OF_EXPERTISE, verbose_name='Career Expertise 3')
    career_expertise4 = models.CharField(max_length=30, default='--', choices=AREA_OF_EXPERTISE, verbose_name='Career Expertise 4')
    career_expertise5 = models.CharField(max_length=30, default='--', choices=AREA_OF_EXPERTISE, verbose_name='Career Expertise 5')
    career_expertise6 = models.CharField(max_length=30, default='--', choices=AREA_OF_EXPERTISE, verbose_name='Career Expertise 6')
    
    # friends = models.ManyToManyField('MenteeProfile')

    # mentor_capacity = models.CharField(max_length=3, default=1, choices=INTEGER_CHOICES, verbose_name='What is your maximum mentee threshold?')

    def __str__(self):
        return self.user.username

# class MentorMenteeTable(models.Model):
#     mentor = models.ForeignKey(MentorProfile)
#     mentee = models.ForeignKey(MenteeProfile)
#     is_current = models.BooleanField(default=True)

class MenteeProfile(models.Model):
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

    career_interest1 = models.CharField(max_length=30, default='MGMT', choices=CAREER_CHOICES, verbose_name='First Career Interest')
    career_interest2 = models.CharField(max_length=30, default='MGMT', choices=CAREER_CHOICES, verbose_name='Second Career Interest')
    career_interest3 = models.CharField(max_length=30, default='MGMT', choices=CAREER_CHOICES, verbose_name='Third Career Interest')
    has_match = models.BooleanField('Match', default=False)

    def __str__(self):
        return self.user.username

# class MentorMenteeMgmt(models.Model):
#     """
#         friends table
#     """
#     user = models.ForeignKey(User)
#     friend = models.ForeignKey(User, related_name="friends")