import matplotlib
import matplotlib.pyplot as plt
# #
x = (54, 55, 67, 34)
y = (2002, 2003, 2005, 2010)

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 8))
res = ax.plot(x, y)
line = res[0]
line.set_c('red')
line.set_linestyle('-')
title = ax.set_title('Pricing') #tytuł u góry
title.set_position ((.2, .7))
yax = ax.get_yaxis()
yax.set_ticks([2002, 2005, 2020])
plt.ylim(2002, 2005)
ax.text(ax.get_xlim()[0], 2003, 'dane', clip_on=True, family='Serif', size=20)
print(plt.style.available)

# # # # ax.bar(x, y)
# # # # ax.scatter(x, y, marker='*', alpha=.5)
# # # _ = ax.pie([10, 4], labels=['x', 'y'])
# # # _ = ax.legend()
plt.show()
# #
# #
# # fig, axs = plt.subplots(2, 2, figsize=(10, 10))
# # axs[0, 0].plot(x, y)
# # axs[1, 0].bar(x, y)
# # axs[0, 1].scatter(x, y, marker='o', alpha=.5)
# # axs[1, 1].pie([10, 5], labels=['10', '5'])
# # plt.show()

import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('_mpl-gallery')
#
# # Make data
# np.random.seed(19680801)
# n = 100
# rng = np.random.default_rng()
# xs = rng.uniform(23, 32, n)
# ys = rng.uniform(0, 100, n)
# zs = rng.uniform(-50, -25, n)
#
# # Plot
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.scatter(xs, ys, zs)
#
# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])
#
# plt.show()
