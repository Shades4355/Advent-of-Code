# input = open('2019/advent3pt1_data.txt', "r").read().split("\n")
input = open('2019/advent3pt1_data_test.txt', "r").read().split("\n") # 6


visited = Array([])
crossed = Array([])
least = Float::INFINITY


input.each do |wire|
  location = [0,0] # up/down, right/left
  parsed_wire = wire.strip().split(",")

  parsed_wire.each do |full_direction|
    direction = full_direction[0]
    distance = full_direction[1..].to_i

    (1..distance).each do
      if direction == "U"
        location[0] += 1
      elsif direction == "D"
        location[0] -= 1
      elsif direction == "R"
        location[1] += 1
      elsif direction == "L"
        location[1] -= 1
      end

      if visited.include?(location)
        crossed << location.dup
      else
        visited << location.dup
      end
    end
  end

  crossed.each do |crossed_paths|
    manhattan_distance = crossed_paths[0].abs + crossed_paths[1].abs
    if manhattan_distance < least
      least = manhattan_distance
    end
  end
end




puts least

# too high: 5011
