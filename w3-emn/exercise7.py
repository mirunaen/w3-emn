#Copy of variables
a="Sun"
b=a
print(b)
#Python does not create another object. It simply creates a new symbolic name or reference, b, which points to the same object that a points to.
a=400
print(b)
#To see this more clearly we could type id(a) and id(b) in the two cases to see that in the first case we assign a and b to the same object and then once a is assigned to 400,a and b point to different objects with different identities.
