_prompt = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0]



_test1 = [1,0,0,0,99] # passes
# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).

_test2 = [2,3,0,3,99] # passes
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).

_test3 = [2,4,4,5,99,0] # passes
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).

_test4 = [1,1,1,4,99,5,6,0,99] # passes
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.



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
#

print opcodeGen(_prompt, 0)
puts ''

puts "Test 1:"
print opcodeGen(_test1, 0)
puts ''
#
puts "Test 2:"
print opcodeGen(_test2, 0)
puts ''

puts "Test 3:"
print opcodeGen(_test3, 0)
puts ''

puts "Test 4:"
print opcodeGen(_test4, 0)
puts ''


=begin
https://adventofcode.com/2019/day/2

dsadasda

=end
