-- Drop Tables if Existing
DROP TABLE IF EXISTS heart_disease;

-- Craete tables and import data from the corresponding CSV files
CREATE TABLE heart_disease (
	id INT NOT NULL, 
	age INT NOT NULL,
	sex VARCHAR NOT NULL,
	dataset VARCHAR NOT NULL,
	cp VARCHAR NOT NULL,
	trestbps NUMERIC NOT NULL,
	chol NUMERIC NOT NULL,
	fbs BOOLEAN DEFAULT false,
	restecg VARCHAR NOT NULL,
	thalch NUMERIC NOT NULL,
	exang BOOLEAN DEFAULT false,
	oldpeak NUMERIC NOT NULL,
	slope VARCHAR NOT NULL,
	ca NUMERIC NOT NULL,
	thal VARCHAR NOT NULL,
	num NUMERIC NOT NULL	
);

SELECT *
FROM heart_disease;