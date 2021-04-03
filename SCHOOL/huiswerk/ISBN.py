ISBN = input()
X='10'
dot=-1
begin=10
end=1
total=0

if len(ISBN) != 10:
    print('INPUT ERROR')
    exit()

for i in ISBN:
    if i not in ['0','1','2','3','4','5','6','7','8','9','X','.'] :
        print('INPUT ERROR')
        exit()

if len(ISBN)==10 and '.' in ISBN:
  while begin>end:
    Copy=ISBN[0]+ISBN[1]+ISBN[2]+ISBN[3]+ISBN[4]+ISBN[5]+ISBN[6]+ISBN[7]+ISBN[8]
    x=Copy.replace('.', str(begin))
    x=[int(x) for x in str(x)]
    check=ISBN[9]
    if check=='X':
      check=10
    elif check=='.':
      check=begin
    else: check=int(check)
    ControlNumber=x[0]*10+x[1]*9+x[2]*8+x[3]*7+x[4]*6+x[5]*5+x[6]*4+x[7]*3+x[8]*2
    z=ControlNumber//11
    y=z*11
    A=ControlNumber-y
    Digit=11-A
    if Digit==check:
      total=str(begin)
    begin=begin-1
  if total=='10':
    print('X')
  else: 
    print(str(total))

elif len(ISBN)==10 and '.' not in ISBN:
    Copy=ISBN[0]+ISBN[1]+ISBN[2]+ISBN[3]+ISBN[4]+ISBN[5]+ISBN[6]+ISBN[7]+ISBN[8]
    x=[int(x) for x in str(Copy)]
    if ISBN[9]=='X':
      check=10
    else: check=int(ISBN[9])
    ControlNumber=x[0]*10+x[1]*9+x[2]*8+x[3]*7+x[4]*6+x[5]*5+x[6]*4+x[7]*3+x[8]*2
    z=ControlNumber//11
    y=z*11
    A=ControlNumber-y
    D=11-A
    Digit=int(D)
    if Digit==11 and check==0:
      print('VALID')
    elif Digit==check:
      print('VALID')
    else:
      print('INVALID')