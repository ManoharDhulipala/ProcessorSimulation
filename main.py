import sys

regList = [65536, 0, 0, 0, 0, 0, 0, 0, 0]

opCodeDict = {
  '100000': 'add', 
  '100010': 'sub', 
  '001000': 'addi',
  '100011': 'lw',
  '101011': 'sw',
  '000100': 'beq',
  '000101': 'bne'
}

registerDict = {
  '00000': 'reg0',
  '00001': 'reg1',
  '00010': 'reg2',
  '00011': 'reg3',
  '00100': 'reg4',
  '00101': 'reg5',
  '00110': 'reg6',
  '00111': 'reg7'
}

reglistLoc = {
  'reg0': 1,
  'reg1': 2,
  'reg2': 3,
  'reg3': 4,
  'reg4': 5,
  'reg5': 6,
  'reg6': 7,
  'reg7': 8
}


controlDict = {
  'addi': '010100001',
  'add': '100100010',
  'sub': '100100010',
  'lw' : '000000000',
  'sw' : '000000000',
  'beq' : '000000000',
  'bne' : '000000000'
}


def binaryToDecimal(n):

  num = n
  dec_value = 0
  base = 1
  temp = num

  while (temp):

    last_digit = temp % 10
    temp = int(temp / 10)
    dec_value += last_digit * base
    base = base * 2

  return dec_value

def parse(input):

  opCode = input[0:6]
  rs = registerDict[input[6:11]]
  rt = registerDict[input[11:16]]
  if opCode == '000000':

    funct = opCodeDict[input[26:32]]
    rd = registerDict[input[16:21]]
    parseList = [funct, rd, rs, rt]

  else:

    instruct = opCodeDict[opCode]
    imm = input[16:32]
    imm.lstrip('0')
    imm = int(imm)
    imm = binaryToDecimal(imm)
    imm = str(imm)

    parseList = [instruct, rt, rs, imm]

  return parseList


def calculate(input):

  regList[0] = regList[0] + 4
  if input[0] == 'addi':
    
    element1 = reglistLoc[input[2]]
    element = reglistLoc[input[1]]
    #print("element1", element1)
    val1 = regList[element1]
    #print("val1", val1)
    val2 = int(input[3])
    #print("val2", val2)
    regVal = val1 + val2
    regList[element] = regVal

  elif input[0] == 'add' or input[0] == 'sub':

    destLoc = reglistLoc[input[1]]
    dest = reglistLoc[input[1]]
    val1 = reglistLoc[input[2]]
    val2 = reglistLoc[input[3]]

    dest = regList[dest]
    val1 = regList[val1]
    val2 = regList[val2]

    if input[0] == 'add':
      dest = val1 + val2

    else:
      dest = val1 - val2
      
    regList[destLoc] = dest

  elif input[0] == 'beq' or input[0] == 'bne':
    val1 = reglistLoc[input[1]]
    val2 = reglistLoc[input[2]]
    loc = int(input[3])

    val1 = regList[val1]
    val2 = regList[val2]
    check = val1-val2

    if check == 0 and input[0] == 'beq':
      regList[0] = loc

    elif check !=0 and input[0] == 'bne':
      regList[0] = loc
    

  else:
    print(input[0])



def printList(list):
  string = ''
  for i in list:
    string = string + str(i) + '|'
  string = string[:-1]

  return string


def joe():

  inFile = sys.argv[1]
  inputlist = []
  opCodeList = []
  regComm = []

  with open(inFile) as NumFile:
    [inputlist.append(line.strip("\n")) for line in NumFile.readlines()]

  size = len(inputlist)

  #print(size)
  if (size < 100):
    with open('registers.txt', 'w') as f:

      f.write(printList(regList))
      f.write('\n')

      for i in inputlist:

        #i = int(i)
        opCodeList.append(parse(i))
        print(parse(i))
        calculate(parse(i))
        f.write(printList(regList))
        f.write('\n')

    #print(opCodeList)

    #print(type(opCodeList[0][0]))

    with open('control.txt', 'w') as f:
      for i in opCodeList:

        f.write(controlDict[i[0]])
        f.write('\n')
  else:

    with open('registers.txt', 'w') as f:
      f.write("Too many inputs")

    with open('control.txt', 'w') as f:
      f.write("Too many inputs")

if __name__ == '__main__':
  inFile = sys.argv[1]
  inputlist = []
  opCodeList = []
  regComm = []

  with open(inFile) as NumFile:
    [inputlist.append(line.strip("\n")) for line in NumFile.readlines()]

  size = len(inputlist)

  #print(size)
  if (size < 100):
    with open('registers.txt', 'w') as f:

      f.write(printList(regList))
      f.write('\n')

  print(printList(regList))
  for i in inputlist:
    print(parse((i)))
    calculate(parse(i))
    print(printList(regList))

