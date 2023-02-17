next =: 3 : ' 6 3 4 1 e.~ #. |: (3 1 $ _1 0 1) |.!.0 y'
step =: 3 : 0
 count =. {.y
 row =. }.y
 nr =. next row
 (count + +/ -. nr), nr
)
solve =: 4 : 0
 i =. ('^'=y) { 0 1
 {. step^:(x-1) (+/ -. i),i
)

echo 10 solve '.^^.^.^^^^'
input =. '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'
echo 40 solve input
echo 400000 solve input

exit 0
