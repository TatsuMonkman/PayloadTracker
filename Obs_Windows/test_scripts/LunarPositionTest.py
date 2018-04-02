import ephem

m1 = ephem.Moon('2018/3/20 5:13:00')

print(ephem.constellation(m1))

print('%s %s %.10f %s %s' % (m1.name, m1.elong, m1.size, m1.a_ra, m1.a_dec))

m2 = ephem.Moon('2018/3/20 5:13:30')

print(ephem.constellation(m2))

print('%s %s %.10f %s %s' % (m2.name, m2.elong, m2.size, m2.a_ra, m2.a_dec))
