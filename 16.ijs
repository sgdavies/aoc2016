dragon =: 4 : 0
 limit =. x
 d =. ('1' = y) { 0 1
 while. limit > #d do.
  d =. d, 0, -. |. d
 end.
limit {. d
)

checksum =: 3 : 0
 c =. y
 while. 0 = 2 | #c do.
  c =. -. 1 = +/"1 [_2[\ c
 end.
c { '01'
)

echo checksum 272 dragon '10001001100000001'
echo checksum 35651584 dragon '10001001100000001'
exit 0
