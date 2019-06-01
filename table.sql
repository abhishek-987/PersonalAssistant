CREATE DATABASE function_database;

CREATE TABLE functions_table(
	
		id int(10) not null PRIMARY KEY AUTO_INCREMENT,
    	function_name varchar(50) not null,
    	function_operation varchar(100) not null
);

INSERT into functions_table(function_name, function_operation) VALUES(

	'date', 'x.strftime("%d")'

);