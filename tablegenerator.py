for x in range(2,21):
   f = open("tableof" + str(x)+".txt","w")
   l = []
   for i in range(1,11):
      val = x*i
      s = str(x) + "*"+ str(i) + "=" + str(val)
      l.append(s)
   f.write(str(l))
   f.close()