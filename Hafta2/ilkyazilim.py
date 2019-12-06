isim = input('bir isim girin:')
print(isim)
print(type(isim))

#############################versiyon1 == kullanildi
'''
if('fatma' == isim):
    #islemler
    print('fatma hanim hosgeldiniz!')
elif ('umit' == isim):
    print('hosgeldin umit!')
else:
    print('hosgeldin digeri!')
'''

#####################################versiyon2 in kullanildi
if('fatma' in isim):
    #islemler
    print('fatma hanim hosgeldiniz!')
elif ('umit' in isim):
    print('hosgeldin umit!')
else:
    print('hosgeldin digeri!')