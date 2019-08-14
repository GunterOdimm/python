from matplotlib import  pyplot

from sample import newborn
from sample import year

pyplot.figure()

pyplot.plot(newborn, label='baby count',linestyle='--',marker='.',color="#ff6600")

pyplot.savefig('line1.png')

pyplot.legend()

pyplot.savefig('line2.png')

pyplot.grid()

pyplot.savefig('line3.png')

pyplot.title("Newborn baby of year")
pyplot.xlabel('year')
pyplot.ylabel('newborn')
pyplot.savefig('line4.png')

pyplot.xticks([0,1,2,3,4],year)
pyplot.savefig('line5.png')

pyplot.close()

