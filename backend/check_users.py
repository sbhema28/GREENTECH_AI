from config.db import db

print("=" * 40)
print("USERS IN DATABASE")
print("=" * 40)

users = db.users.find()

count = 0

for user in users:
    count += 1
    print(f"\nUser {count}:")
    print(f"ID: {user.get('_id')}")
    print(f"Name: {user.get('name')}")
    print(f"Email: {user.get('email')}")
    print(f"Password: {user.get('password')}")

if count == 0:
    print("No users found in database.")

print("\nTotal Users:", count)
