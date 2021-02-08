user=dict()
user["fname "] = 'Askar'
user['lname'] = "Akshabaev"
print(user)
for key in user:
    print(key,user[key])

if "fname" in user:
    print('YES')
else:
    print("No")