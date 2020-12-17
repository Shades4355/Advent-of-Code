# input = open('2019/advent3pt1_data.txt', "r").read().split(',')
input = open('2019/advent3pt1_data_test.txt', "r").read().split(',') # 159

location = [0,0] # up/down, right/left
visited = Array([])
crossed = []
least = Float::INFINITY

input.each do |full_direction|
  direction = full_direction[0]
  distance = full_direction[1..].to_i
  puts(direction, distance)
  puts("pre-" + "(" + location.join(", ") + ")")
  if direction == "U"
    location[0] += distance
  elsif direction == "D"
    location[0] -= distance
  elsif direction == "R"
    location[1] += distance
  elsif direction == "L"
    location[1] -= distance
  end
  puts("post-" +  "(" + location.join(", ") + ")")

  if visited.include?([location])
    crossed << location
    puts("True")
    print("visited: ")
    print(visited)
    puts()
  else
    visited << location
    puts("False")
    print("visited: ")
    print(visited)
    puts()
  end

  crossed.each do |crossed_paths|
    manhattan_distance = crossed_paths[0].abs + crossed_paths[1].abs
    if manhattan_distance < least
      least = manhattan_distance
    end
    puts("least: " + least.to_s)
  end
  puts("~" * 20)
end




puts least


# too high: 5011
