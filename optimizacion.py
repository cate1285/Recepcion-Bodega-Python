def conteo(x):
  letras=[]
  lista=[]
  count=0
  a=1
  r=1
  for i in range(len(x)):
    if a < len(x):
      if x[count]!= x[a] :
        letras.append(x[count])
        lista.append(r)
        count=a
        a+=1
        r=1
      else:
        a+=1
        r+=1
    elif a== len(x):
      lista.append(r)
      letras.append(x[count])
  print(' '.join(map(str,letras)))
  print(' '.join(map(str,lista)))

x=input().upper().split()
conteo(x)
