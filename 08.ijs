inp =: <;._2 freads '08.txt'

transform =: 4 : 0  NB. x=display, y=instructions
 xr =. 0{$x
 xc =. 1{$x
 display =. x
 for_ins. y do.
  words =. ;:>ins
  if. 'rect' -: >0{words do.
   cr =. ".;._2 (>1{words),'x'
   c =. 0{cr
   r =. 1{cr
   mask =. xr $!.0 (r $ ((1, xc) $!.0 (c$1)))
   display =. mask +. display
  else.
   c =. ". >4{words
   by =. - ". >6{words  NB. - to shift right instead of left
   if. 'column' -: >1{words do.
    display =. |: display
   end.
   display =. (c{.display),(by|.c{display),((c+1)}.display)
   if. 'column' -: >1{words do.
    display =. |: display
   end.
  end.
  NB. echo display { '.#'
 end.
display
)

NB.i=: <;._2 'rect 3x2',LF,'rotate column x=1 by 1',LF,'rotate row y=0 by 4',LF,'rotate column x=1 by 1',LF
NB.echo +/+/ (3 7 $ 0) transform i
out =. (6 50 $ 0) transform inp
echo +/+/ out
echo out { ' #'

exit 0
