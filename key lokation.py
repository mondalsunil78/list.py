key_location = "chair"
locations = ["garage", "living room", "chair", "closet"]
for i in locations:
    if i == key_location:
        print("key found in", i)
         break
    else:
        print("key is not found", i)
