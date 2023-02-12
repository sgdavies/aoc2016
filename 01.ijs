inp =: 'L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5'

l =. }:"1 ;._2 inp ,', '  NB. split on spaces and trim trailing ,

NB. First part: if L pick i elseif R pick -i, and take running product to get current direction
NB. Then * numbers and take running sum to get answer (as a complex number)
v =. +/\ (*/\('R' = {."1 l) { 0j1 0j_1) * (". }."1 l)

echo +/ |"1 +. {:v  NB. sum the magnitudes of the real/imag components of final spot

NB. First location you *stop* at twice is
NB. +/ |"1 +. {. (I. 1<+/"1 =v) { ~.v
NB. (first point that appears more than once in =v)

NB. But we need to include crossing points.
dirs =. */\('R'={."1 l){0j1 0j_1
counts =. ".}."1 l
all_intersections =. +/\ counts # dirs
echo +/ |"1 +. {. (I. 1<+/"1 =all_intersections) { ~.all_intersections

exit 0
