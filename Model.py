/////// choices 

class Student(models.Model):
YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
////////////////  OR /////////////
class MyModel(models.Model):
    class Month(models.TextChoices):
        JAN = "1", "JANUARY"
        FEB = "2", "FEBRUARY"
        MAR = "3", "MAR"
        # (...)

    month = models.CharField(
        max_length=2,
        choices=Month.choices,
        default=Month.JAN
    )
