solve =: 3 : 0
 elfs =. i. y
 while. 1<#elfs do.
  elfs =. 1 |. elfs
  elfs =. }. elfs
 end.
elfs+1  NB. 0-indexed
)

NB. 'solve' works but it's too slow for large numbers
NB. Is there a pattern? 
NB. ,solve"0 [1+i.50
NB. 1 1 3 1 3 5 7 1 3 5 7 9 11 13 15 1 3 5 7 9 11 13
NB. 15 17 19 21 23 25 27 29 31 1 3 5 7 9 11 13 15 17
NB. 19 21 23 25 27 29 31 33 35 37
NB. odd numbers: 1, 2, 4, 8, 16, ... of each
NB. So to solve for x: rmeove the largest 2^n -1 from x you can,
NB. and then pick the (remainder)th odd number
quicksolve =: 3 : 0
 b =. 2 #.inv y  NB. binary expansion of y
 NB. ..th odd number | of y - | 0b111..111 (#b -1 ones)
 _1 + 2* y - 2 #. (_1 + #b) $ 1
)

echo quicksolve 3014387

NB. Part two
solve_two =: 3 : 0
 elfs =. i. y
 while. 1<#elfs do.
  steal =. <. (#elfs)%2
  elfs =. (steal{.elfs),((steal+1)}.elfs)
  elfs =. 1 |. elfs  NB. next elf to the front
 end.
elfs+1
)

NB. solved the rest interactively
NB. is there another pattern?
NB. ,solve_two"0 [1+i.100
NB. 1  1 3  1 2 3 5 7 9  1 2 3...27 29 ... 81 etc
NB. so 1, then 1...3^n followed by the next 3^n odd numbers
NB. By experimentation, 3014387<{:+/\ 1,2*3^ i.14
NB. x:3014387 - {:+/\ 1,2*3^ i.13
NB. 1420064
NB. this is less than 4782969 (i.e. {:+/\ 1,2*3^ i.14  )
NB. so 1420064 is the answer (it's the 1420064th counting number
NB. and we haven't reached the set of odd numbers).
