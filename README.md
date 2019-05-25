# Logs Analysis Project

# Project Description 

	this is Log Analysis project for the Udacity Full Stack Nanodegree that consists of answering three questions based on the data in the given database for 
	a fictional news website,using Python (psycopg2) module to connect to PostgreSQL database and the schema contains three tables: authors, articles, and log.
	 
## Questions

	1. What are the most popular three articles of all time?
	2. Who are the most popular article authors of all time?
	3. On which days did more than 1% of requests lead to errors?
	
# Answers

	Answer 1: 
		* "Candidate is jerk, alleges rival" - 338647 views
		* "Bears love berries, alleges bear" - 253801 views
		* "Bad things gone, say good people" - 170098 views

	Answer 2

		* Ursula La Multa - 507594 views
		* Rudolf von Treppenwitz - 423457 views
		* Anonymous Contributor - 170098 views
		* Markoff Chaney - 84557 views

	Answer 3
		* July 17, 2016 - 2.2% errors

## How to Run the Project

	* Download and Install postgresSQL
	* Download the schema and data for the news database for the below link:
		https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
	* UnZip the file newsdata.zip (newsdata.sql)
	* Create databse news and Import newsdata.sql into database (postgresSQL) using psql -d news -f newsdata.sql.
	* Run or Excute file using Command python '.\Logs Analysis Project.py'.
	* Check the results for the output file output.txt.




