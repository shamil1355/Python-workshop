import matplotlib.pyplot as plt
data={'c':20,'c++':15,'java':30,'python':35}
courses=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,6))
plt.bar(courses,values,color='yellow',width=0.4)
plt.xlabel("Courses Offered")
plt.ylabel("No of Students Enrolled")
plt.title("Students Enrolled In Diffrent Courses")
plt.show()

