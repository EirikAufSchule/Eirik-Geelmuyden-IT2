import matplotlib.pyplot as plt

karakterer = [5, 3, 6, 3, 5, 1, 2, 2, 2, 4, 2, 2, 5, 5, 6, 3, 5, 3, 5, 4, 2, 6, 1, 4, 2, 3, 3, 3, 5, 5]

ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)

ax1.set_xlabel("$karakterer$")
ax1.set_ylabel("$frekvens$")
ax1.hist(karakterer, 6, color="red", ec = "lightblue")
ax2.pie(karakterer, labels = [f"Karakter {i}" for i in karakterer])
plt.show()
