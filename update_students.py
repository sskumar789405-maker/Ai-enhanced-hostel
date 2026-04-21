import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_pg_system.settings')
django.setup()

from django.contrib.auth.models import User
from management.models import StudentProfile

# New student names
new_names = ['Jagdish', 'Gudu', 'Somnath', 'Soumya']

# Update existing students
students = StudentProfile.objects.all()
for i, student in enumerate(students):
    if i < len(new_names):
        student.user.first_name = new_names[i]
        student.user.save()
        print(f"Updated {student.user.username} to {new_names[i]}")

print("\n✅ All students updated successfully!")
print("\nUpdated Students:")
for student in StudentProfile.objects.all():
    print(f"  - {student.user.first_name} (@{student.user.username})")
