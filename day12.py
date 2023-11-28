#File I/O
print("\nWilson - Day 12 of 100DaysOfCode")
print("\n File I/O")

#writing on a empty txt file
with open('sampleio.txt','w') as file:
  file.write('hello my name is wilson and im doing my 100daysofcode')
with open('sampleio.txt', 'a') as file:
  file.write('\na is used for appending some content in my sampleio txt file')
with open('sampleio.txt','r') as file:
  txt = file.read()
  print(txt)
