alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(string, shift):
  encoded = ""
  total_alphabets = len(alphabet)
  for char in string:
    index = alphabet.index(char)
    index = (index + shift) % total_alphabets
    index = int(index)
    encoded += alphabet[index]
  print("encoded message is " + encoded)

def decode(string, shift):
  decoded = ""
  total_alphabets = len(alphabet)
  for char in string:
    index = alphabet.index(char)
    index = (index - shift)
    if index < 0:
      index = total_alphabets + index
    decoded += alphabet[index]
  print("decoded message is " + decoded)
  

is_program_end = False
while not is_program_end:

  direction = input("Type 'encode' to encryp, type 'decode' to decrypt \n")
  text = input("Type your message: \n").lower()
  shift = int(input("Type the shift \n"))

  if direction == "encode":
    encode(text, shift)
  else:
    decode(text, shift)

  again = input("Do you want to continue. Type 'y' to continue").lower()
  
  if not again == 'y':
    is_program_end = True
