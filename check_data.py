import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_pg_system.settings')
django.setup()

from management.models import Room, StudentProfile, Fee, Complaint, Announcement, Maintenance
from django.contrib.auth.models import User

print("=== DATABASE CONTENTS ===")
print(f"Users: {User.objects.count()}")
print(f"Rooms: {Room.objects.count()}")
print(f"Students: {StudentProfile.objects.count()}")
print(f"Fees: {Fee.objects.count()}")
print(f"Complaints: {Complaint.objects.count()}")
print(f"Announcements: {Announcement.objects.count()}")
print(f"Maintenance: {Maintenance.objects.count()}")

print("\n=== SAMPLE DATA ===")
for user in User.objects.all()[:2]:
    print(f"User: {user.username}")

for room in Room.objects.all()[:2]:
    print(f"Room: {room.number} ({room.room_type})")

for student in StudentProfile.objects.all()[:2]:
    print(f"Student: {student.user.username} - Room: {student.room}")
