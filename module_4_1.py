from fake_math import divide as fm_div
from true_math import divide as tm_div

result1 = fm_div(69, 3)
result2 = fm_div(3, 0)
result3 = tm_div(49, 7)
result4 = tm_div(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)