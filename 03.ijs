n =. ". ;._2 freads '03.txt'
ok =: 3 : '(>./y) < (+/y)-(>./y)'  NB. longest side is less than sum of other 2
echo +/ ok"1 n
echo +/+/ ok"1 |:"2 ]_3[\n  NB. take 3 rows at a time and transpose each block
exit 0
