# ISS_Activity_2

changes:-

1. Added colons (`:`) where needed, because Python needs them after functions and loops.
2. Fixed a mistake by changing `==` to `=`, so it actually assigns a value instead of comparing it.
3. Changed `***` to `**`**, because `**` is the correct way to do powers in Python.
5. Made sure the right value gets passed to the function in the loop.


in code:-
1.Added colon
def is_narc(n):
for num in range(start, end + 1):
2.Fixed assignment (changed == to =)
num_str = str(n)
3.Changed operator *** to **
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
4.Fixed function call to pass the correct argument:
if is_narc(n=num)


