def make_equal(s) :
  _space = False
  s_fin = ''
  s = s.strip(" ")
  
  for idx, i in enumerate(s) :
    if i == ' ':
      if not _space and (s[idx-1].isalpha() or s[idx-1].isdigit()):
        s_fin += i
        _space = True
        
      else :
        continue
        
    else :
      if i.isalpha() :
        s_fin += i.lower()
        _space = False 
        continue
      elif i.isdigit() :
        s_fin += str(i)
        _space = False 
        continue

      if _space :
        s_fin = s_fin.rstrip(" ")
        
      if i in '{[(' :
        s_fin += '('
      elif i in '}])' :
        s_fin += ')'
      elif i in ';,' :
        s_fin += ','
      else :
        s_fin += i

      _space = False  

  return s_fin

k = int(input())
 
for i in range(k) :
  s1 = input()
  s2 = input()
  
  s1_fin = make_equal(s1)
  s2_fin = make_equal(s2)
    
  if s1_fin == s2_fin :
    print(f"Data Set {i+1}: equal")
  else:
    print(f"Data Set {i+1}: not equal")

  print()