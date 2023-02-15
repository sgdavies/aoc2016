inp =: freads '09.txt'
nowhitespace =: 3 : '(-. LF = y) # y'

decompress =: 3 : 0
 out =. ''
 in =. y
 parens =. in i. '()'
 while. (0{parens) < #in do.
  po =. 0{parens
  pc =. 1{parens
  out =. out, po{.in
  nums =. ". ;._2 ( (po+1)}. pc{. in ),'x'
  in =. (pc+1)}.in
  chars =. 0{nums
  repeats =. 1{nums
  out =. out, (chars*repeats) $ chars{.in
  in =. chars}.in
  parens =. in i. '()'
 end.
 out =. out,in
out
)

decompress_len =: 4 : 0  NB. x=expand_parens? y=input
 olen =. 0
 in =. y
 parens =. in i. '()'
 while. (0{parens) < #in do.
  po =. 0{parens
  pc =. 1{parens
  olen =. olen + po
  nums =. ". ;._2 ( (po+1)}. pc{. in ),'x'
  in =. (pc+1)}.in
  nchars =. 0{nums
  repeats =. 1{nums
  if. x do.
   chunklen =. 1 decompress_len nchars{.in
  else.
   chunklen =. nchars
  end.
  olen =. olen + (chunklen*repeats)
  in =. nchars}.in
  parens =. in i. '()'
 end.
 olen =. olen + #in
olen
)

ignore =: 0 : 0
echo decompress 'ADVENT'
echo decompress 'A(1x5)BC'
echo decompress '(3x3)XYZ'
echo decompress 'A(2x2)BCD(2x2)EFG'
echo decompress '(6x1)(1x3)A'
echo 0 decompress_len 'X(8x2)(3x3)ABCY'
echo 1 decompress_len 'X(8x2)(3x3)ABCY'
echo # decompress nowhitespace inp
)
echo 0 decompress_len nowhitespace inp
echo 1 decompress_len nowhitespace inp
exit 0
