ipsubnet = input('ip girin(x.x.x.x/subnet):')
correct = True


if len(ipsubnet.split('/')) != 2:
  print('yallah!')
  correct = False
elif int(ipsubnet.split('/')[1]) < 0 or int(ipsubnet.split('/')[1]) > 32:
  print('yallah!')
  correct = False
elif len(ipsubnet.split('/')[0].split('.')) != 4:
  print('yallah!')
  correct = False


if correct:
  subnet = ipsubnet.split('/')[1]
  ip = ipsubnet.split('/')[0].split('.')
  for i in ip:
    try:
      i = int(i)
    except:
      correct = False
      print('ip icinde sadece rakam kullaniniz')


if correct:
  for i in ip:
    if i <0 or i > 255:
      correct = False


if correct:
  pass
