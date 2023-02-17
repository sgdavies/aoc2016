NB. Array of numbers N x 2
input =: ". ;._2"1 ([;._2 freads '20.txt'),"1 '-'

DBG =: 0  NB. can override in interactive mode
debug =: 3 : 'if. DBG do. echo y end.'

add =: 4 : 0  NB. x=splits_array, y = lo,hi to be added
 if. #x do.
   lo =. 0{y
   hi =. 1{y
   ip =. (lo < 0{"1 x) i. 1  NB. insert point
   debug 'lo, hi, (#x), ip'
   debug lo, hi, (#x), ip
   if. ip > 0 do.
     plo =. 0{(ip-1){x  NB. previous low
     phi =. 1{(ip-1){x
     if. lo <: phi+1 do.
       NB. overlap with previous entry
       if. hi > phi do.
         a =. ((ip-1){.x), (plo,hi), ip}.x
	 ip =. ip-1
       else.
         a =. x  NB. y fully contained in previous range
       end.
     else.
       NB. We don't overlap with previous row
       a =. (ip{.x),y,(ip}.x)
     end.
   else.
     NB. ip is 0
     a =. y,x
   end.

   debug 'ip, (#a), hi'
   debug ip, (#a), hi
   debug a
   if. (ip< 1 -~ #a) do.  NB. Not the last entry
     if. (hi+1 >: 0{(ip+1){a) do.
       NB. We now overlap with the next row
       new_y =. (ip+1){a
       new_a =. ((ip+1){.a),(ip+2)}.a
       a =. new_a add new_y
     end.
   end.
 else.
   NB. No previous entries
   a =. 1 2 $ y
 end.
a
)

solve =: 3 : 0  NB. pass array of number pairs
 s =. ''
 for_pair. y do.
   s =. s add pair
 end.
s
)

s =: solve input
echo 1+1{0{s

check_ends =: 3 : 0
assert. 0 = 0{0{y
assert. 4294967295 = 1{_1{y
)
check_ends s

NB. Sum the gaps between hi/lo of subsequent rows
NB. As it turns out all the gaps are size 1 so this could just be a count
echo +/ 1 -~ -~/"1 [ _2[\ }.}:,s

exit 0
