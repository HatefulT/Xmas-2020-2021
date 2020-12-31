import random as r                                          #            o
def merry(n):                                               #           o-
  return "-"*n                                              #          ---o
def xmas(n, m):                                             #          ---o
  a = merry(n)                                              #         --o-o-
  r1 = int(r.random()*n//4+1)                               #        -o------
  for i in range(r1):                                       #        ----o---
    j = int(r.random()*n)                                   #       -o--------
    a = a[:j] + "o" + a[j+1:]                               #      ----o---oo--
  return a                                                  #     -----o-----o--
def space(n):                                               #      -----o---o--
  return " "*n                                              #     --o-----------
                                                            #    ----o----o---o--
for i in range(4):                                          #   -------o----oo----
  for j in range(i//2 + 3):                                 #       Merry xmas!
    print( space(5+(3-i)*2 - j) + xmas( 2*(2*i+j), j) )     #   From Moscow, Russia
                                                            #    Good luck in 2021!
print(space(6) + "Merry xmas!")                             #
