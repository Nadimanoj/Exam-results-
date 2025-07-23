# Exam Result - Predefined Student List

# List of students: (Name, Marks)
students = [
    ("manoj", 78),
    ("eshwar", 34),
    ("lokesh", 60),
    ("murali", 45),
    ("shiva", 28)
]

# Pass mark
pass_mark = 40

# Processing results
results = []
for name, marks in students:
    status = "Pass" if marks >= pass_mark else "Fail"
    results.append((name, marks, status))

# Displaying results
print("Exam Results")
print(f"{'Name':<10}{'Marks':<10}{'Status'}")
print("-" * 30)
for name, marks, status in results:
    print(f"{name:<10}{marks:<10}{status}")

total = len(results)
passed = sum(1 for _, _, status in results if status == "Pass")
failed = total - passed

print("\nSummary")
print(f"Total Students: {total}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")