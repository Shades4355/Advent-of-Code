=begin
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

examples:
For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
=end

_masses = [144358,
92044,
53617,
71695,
134329,
149370,
57980,
71899,
58281,
67662,
81199,
123700,
140080,
63608,
71520,
51020,
125731,
58038,
64709,
120935,
65512,
142680,
135615,
64251,
131894,
92421,
135197,
118339,
111812,
133283,
100622,
67295,
125093,
56381,
76811,
82373,
147433,
96033,
114523,
134209,
111383,
130114,
56037,
144439,
135345,
78408,
98586,
118732,
84373,
62412,
146946,
96024,
101322,
91590,
59401,
113838,
98867,
76950,
130379,
120006,
66525,
64876,
83451,
114127,
98963,
81096,
110360,
123755,
77552,
76400,
146026,
70976,
53906,
149079,
121966,
63970,
67562,
62162,
67534,
118706,
138329,
81170,
101462,
130641,
73241,
86687,
67198,
141550,
117396,
98423,
51743,
88076,
114089,
118106,
96609,
145837,
61959,
118543,
63914,
54664
]


#############
# functions #
#############



#########
# Start #
#########
total = 0

for i in _masses do
  subtotal = (((i/3).floor)-2)
  total += subtotal

  while subtotal > 0
    subtotal = (((subtotal/3).floor)-2)

    if subtotal <= 0
      subtotal = 0
    end

    print "Subtotal: "
    puts subtotal

    total += subtotal
  end

end
puts ''
print total
