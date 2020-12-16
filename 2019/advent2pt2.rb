
=begin
fails
=end

_prompt = [
  1,12,2,3,
  1,1,2,3,
  1,3,4,3,
  1,5,0,3,
  2,13,1,19,
  1,9,19,23,
  2,23,13,27,
  1,27,9,31,
  2,31,6,35,
  1,5,35,39,
  1,10,39,43,
  2,43,6,47,
  1,10,47,51,
  2,6,51,55,
  1,5,55,59,
  1,59,9,63,
  1,13,63,67,
  2,6,67,71,
  1,5,71,75,
  2,6,75,79,
  2,79,6,83,
  1,13,83,87,
  1,9,87,91,
  1,9,91,95,
  1,5,95,99,
  1,5,99,103,
  2,13,103,107,
  1,6,107,111,
  1,9,111,115,
  2,6,115,119,
  1,13,119,123,
  1,123,6,127,
  1,127,5,131,
  2,10,131,135,
  2,135,10,139,
  1,13,139,143,
  1,10,143,147,
  1,2,147,151,
  1,6,151,0,
  99,
  2,14,0,0]


prompt_freeze = _prompt.freeze



=begin from pt 1

def opcodeGen(array, position)
  x = position
  if array[x] == 1
    opcode = array[x..(x+3)]

    array[opcode[3]] = array[opcode[1]] + array[opcode[2]]
    x += 4 # step forward 4
    opcodeGen(array, x) # repeat
  elsif  array[x] == 2
    opcode = array[x..(x+3)]
    array[opcode[3]] = array[opcode[1]] * array[opcode[2]]
    x += 4
    opcodeGen(array, x) # repeat
  elsif array[x] == 99
    return array
  else
    return array
  end

end

=end

'''
https://adventofcode.com/2019/day/2#part2

"determine what pair of inputs produces the output 19690720."

"Each time you try a pair of inputs, make sure you first reset the computer\'s memory to the values in the program (your puzzle input) - in other words, don\'t reuse memory from a previous attempt."

(use .dup & .freeze?)

[0] = pointer
[1] = noun (wx) (between 0..99)
[2] = verb (yz) (between 0..99)
[3] = output

noun + verb == wxyz (between 0000..9999)

"Find the input noun and verb that cause the program to produce the output 19690720."

"What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)"
'''

def opcodeGen(array, position)
  x = position
  if array[x] == 1
    opcode = array[x..(x+3)]

    y = array[opcode[1]] + array[opcode[2]]
    x += 4 # step forward 4
    return x, y
  elsif  array[x] == 2
    opcode = array[x..(x+3)]
    y = array[opcode[1]] * array[opcode[2]]
    x += 4
    return x, y
  elsif array[x] == 99
    y = 99
    x += 1
    return x, y
  else
    y =  "Oh shiiiiit.....It broke...."

  end

end

#########
# start #
#########


x = 0
y = 0
until y == 19690720 do
  x, y = opcodeGen(prompt_freeze, x)
  puts "X: #{x}"
  puts "Y: #{y}"
  if y ==  "Oh shiiiiit.....It broke...."
    puts y
    break
  end
end
