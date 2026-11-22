from config.db import db

records = db.consumption.find()

print("=" * 40)
print("CONSUMPTION DATA")
print("=" * 40)

count = 0

for record in records:
    count += 1

    print(f"\nRecord {count}")
    print(f"Temperature: {record.get('temperature')}")
    print(f"Building Size: {record.get('buildingSize')}")
    print(f"Units Consumed: {record.get('unitsConsumed')}")
    print(f"Renewable Usage: {record.get('renewableUsage')}")

print("\nTotal Records:", count)