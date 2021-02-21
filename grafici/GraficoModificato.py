import matplotlib.pyplot as plt

data = {'samsung': 25, 'apple': 14, 'huawei': 7, 'xiaomi': 4}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(11, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('marche di cellulari più vendute')
