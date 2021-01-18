import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()
max_x = die_1.num_sides + die_2.num_sides
die_values = [die_1.roll()+die_2.roll() for x in range(50_000)]

height = [die_values.count(x) for x in range(1,max_x)]

fig, ax = plt.subplots()
ax.bar(list(range(1,max_x)), height)

ax.set_title('Sum of two rolled D6 die', fontsize = 24)
ax.set_xlabel('Sum', fontsize = 14)
ax.set_ylabel('Frequency', fontsize = 14)

ax.tick_params(axis='both', which='major', labelsize = 14)

plt.show()

