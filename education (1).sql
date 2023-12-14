CREATE TABLE ldms_education (
  id INT NOT NULL,
  institute_name VARCHAR(20) ,
  passing_year INT NOT NULL,
  primary key (id),
  foreign key (id) references ldms_user (id)
);
insert into ldms_education (id, institute_name, passing_year)
values(1, 'Stanford University',2022),
(2, 'MIT',2023),
(3, 'Carnegie University', 2018),
(4, 'UC',2019),
(5, 'UW', 2015),
(6, 'New York University', 2021),
(7, 'Harvard',2020),
(8, 'Duke University',2022),
(9, 'Cornell University',  2023),
(10, 'IIT Roorkee',  2017),
(11, 'UCLA',2018),
(12, 'IIT Bombay', 2019),
(13, 'IIT Kanpur', 2020),
(14, 'Yale',2021),
(15, 'MIT',2023);
select * from ldms_education;
