
def returnLineType(data):
	if (":" in data):
		return 0 # Line containing movie id.
	else:		
		return 1 # Line containing userId, rating, date.