def jiazi(year):
   tiangan='甲乙丙丁戊己庚辛壬癸'
   dizhi='子丑寅卯辰巳午未申酉戌亥'
   jiazi=[tiangan[x%len(tiangan)]+dizhi[x%len(dizhi)] for x in range(60)]
   return(jiazi[(year%60)-4])