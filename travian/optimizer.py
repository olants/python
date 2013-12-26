def start_data():
	start_data_variables = [0,0,0,0]
	cur_data_variables = [0,0,0,0]
	print "Current resources:"
	start_data_variables[0] = input("wood: ")
	start_data_variables[1] = input("clue: ")
	start_data_variables[2] = input("iron: ")
	start_data_variables[3] = input("crop: ")
	
	print "Thraed:"
	cur_data_variables[0] = input("wood: ")
	cur_data_variables[1] = input("clue: ")
	cur_data_variables[2] = input("iron: ")
	cur_data_variables[3] = input("crop: ")
	
	print """Current resources: 
		wood: %d
		clue: %d
		iron: %d
		crop: %d """ % (start_data_variables[0], start_data_variables[1], start_data_variables[2], start_data_variables[3] )
	
	iron_mine_level5 = [780,620,235,465,2,11]

	time2build_iron_mine_level5 = [ float((start_data_variables[0] - iron_mine_level5[0])) / cur_data_variables[0], 
			float((start_data_variables[1] - iron_mine_level5[1])) / cur_data_variables[1],
			float((start_data_variables[2] - iron_mine_level5[2])) / cur_data_variables[2],
			float((start_data_variables[3] - iron_mine_level5[3])) / cur_data_variables[3]
			]
	print """Time to build iron mine level 5:
		wood: %r
		clue: %r
		iron: %r
		crop: %r  """ % (time2build_iron_mine_level5[0], time2build_iron_mine_level5[1], time2build_iron_mine_level5[2], time2build_iron_mine_level5[3])
	i = 0
	while ( i < len(cur_data_variables) ) :
		print cur_data_variables[i] + iron_mine_level5[5]
		i = i + 1



start_data()
