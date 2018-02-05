This data set contains 10000054 ratings and 95580 tags applied to 10681 movies by 71567 users of the online movie recommender service MovieLens.

Ratings Data File Structure
	All ratings are contained in the file ratings.dat. Each line of this file represents one rating of one movie by one user, and has the following format:

	UserID::MovieID::Rating::Timestamp

	The lines within this file are ordered first by UserID, then, within user, by MovieID.

	Ratings are made on a 5-star scale, with half-star increments.

	Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.

	
Tags Data File Structure
	All tags are contained in the file tags.dat. Each line of this file represents one tag applied to one movie by one user, and has the following format:

	UserID::MovieID::Tag::Timestamp

	The lines within this file are ordered first by UserID, then, within user, by MovieID.

	Tags are user generated metadata about movies. Each tag is typically a single word, or short phrase. The meaning, value and purpose of a particular tag is determined by each user.

	Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.	
		

Movies Data File Structure
	Movie information is contained in the file movies.dat. Each line of this file represents one movie, and has the following format:

	MovieID::Title::Genres

	MovieID is the real MovieLens id.

	Movie titles, by policy, should be entered identically to those found in IMDB, including year of release. However, they are entered manually, so errors and inconsistencies may exist.

	Genres are a pipe-separated list, and are selected from the following:		
		Action
		Adventure
		Animation
		Children's
		Comedy
		Crime
		Documentary
		Drama
		Fantasy
		Film-Noir
		Horror
		Musical
		Mystery
		Romance
		Sci-Fi
		Thriller
		War
		Western
		