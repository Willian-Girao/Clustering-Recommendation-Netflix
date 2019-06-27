
def returnLineType(data):
	if (":" in data):
		return 0 # Line containing movie id.
	else:		
		return 1 # Line containing userId, rating, date.

#grab last 4 characters of the file name:
def last_4chars(x):
    return x.split('_')[0]

# Returns movie id
def getMovieId(file_name):
	return file_name.split('_')[0].replace('.txt', '')