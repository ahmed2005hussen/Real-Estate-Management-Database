create database RealEstate;
use RealEstate ; 

create table Office (
officeID int auto_increment primary key , 
location varchar(100)
);

create table Employee(
empID int auto_increment primary key,
empName varchar(50)
);

create table Property(
propID int auto_increment primary key ,
address varchar(50), 
city varchar(50),
state varchar(50), 
zip varchar(50) , 

offID int not null ,

foreign key (offID) references Office(officeID)

);

create table Owner(
ownerID int auto_increment primary key, 
ownerName varchar(50)
);

create table Ownership(
ownerID int not null , 
propID int not null, 

primary key(ownerID , propID), 

foreign key (ownerID) references owner(ownerID), 
foreign key (propID) references Property(propID)
); 

create table WorksIn(
officeID int not null,
empID int not null , 
primary key(officeID , empID),
foreign key (officeID) references Office(officeID),
foreign key (empID) references Employee(empID)

);

create table Manage(
officeID int not null,
empID int not null , 
primary key(officeID , empID),
foreign key (officeID) references Office(officeID),
foreign key (empID) references Employee(empID)
);

insert into office(location)
values
("Giza"),
("Dokki"),
("Obera");

insert into Employee(empName)
values
("ahmed"),
("hussein"),
("mohammed"),
("saleh");


insert into Property(address,city , state , zip ,offID)
values
("Giza" , "A" , "cairo ", "B" , 1),
("Dooke" , "A" , "cairo ", "B" , 2);


insert into owner(ownerName)
values
("hh"),
("aa");



insert into Ownership(ownerID,propID)
values
(1,2),
(2,1);




insert into WorksIn(officeID , empID)
values 
(1 , 1),
(1,2),
(2,3),
(3,4);

insert into Manage(officeID , empID)
values 
(1 , 1),
(2,3),
(3,4);

