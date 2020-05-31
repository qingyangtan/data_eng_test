CREATE TABLE customer(
	customer_id serial PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	phone_number VARCHAR (50)
);

CREATE TABLE salesperson(
	salesperson_id serial PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL
);

CREATE TABLE store(
	store_id serial PRIMARY KEY,
	location VARCHAR (255) NOT NULL
);

CREATE TABLE car_manufacture(
	manufacture_name VARCHAR (255) PRIMARY KEY,
	other_details VARCHAR (255)
);

CREATE TABLE car_model(
	serial_number VARCHAR (50) PRIMARY KEY,
	manufacture_name VARCHAR (255) REFERENCES car_manufacture (manufacture_name),
	model_name VARCHAR (50) NOT NULL,
	model_variant VARCHAR (50) NOT NULL,
	weight FLOAT NOT NULL,
	engine_cubic_capacity FLOAT NOT NULL,
	price FLOAT NOT NULL,
	car_condition VARCHAR (50) NOT NULL
);

CREATE TABLE sales(
	PRIMARY KEY (salesperson_id, car_id),
	salesperson_id INT REFERENCES salesperson (salesperson_id),
	car_id VARCHAR (50) REFERENCES car_model (serial_number),
	customer_id INT REFERENCES customer (customer_id),
	store_id INT REFERENCES store (store_id),
	transaction_datetime TIMESTAMP NOT NULL,
	transaction_price FLOAT NOT NULL
);