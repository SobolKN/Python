check = True

# Функция для зашифровки и расшифровки текста
def encryption_decryption(inpt_str, mode):
  sign = 1 if mode == 1 else -1
  inpt_str_list = list(inpt_str)
  new_inpt_str = ''
  for symbol in inpt_str_list:
    new_inpt_str += chr(ord(symbol) + 5 * sign)
  return new_inpt_str

while check:
  print('Для шифровки текста введите: 1\nДля расшифровки введите: 2\nДля выхода из программы: 3')
  mode = int(input())
  if mode == 1 or mode == 2:
    print('Введите текст:')
    inpt_str = input()
    result = encryption_decryption(inpt_str, mode)
    print(result)
  elif mode == 3:
    print('exit ptogram...')
    check = False
