wynik_z_testu_klasyfikacyjnego = float(input('wynik_z_testu_klasyfikacyjnego'))
Ocena_z_swiadectwa = int(input('ocena z świadectwa'))

if wynik_z_testu_klasyfikacyjnego > 90 or Ocena_z_swiadectwa > 5:
    print('dostales się do grupy zaawansowanej')
elif wynik_z_testu_klasyfikacyjnego <= 90 or Ocena_z_swiadectwa < 5:
    print('grupa Podstawowa')
