CREATE TABLE ldms_experience (
  id INT NOT NULL,
  skills varchar(30),
  primary key (id),
  foreign key (id) references ldms_user (id)
); 
insert into ldms_experience (id, skills)
values (1, 'Python, Java, JavaScript' ),
(2, 'Python, SQL, R'),
(3, 'Python, AWS, Azure'),
(4, 'C++, C#, Python'),
(5, 'Java, Objective-C, Swift'),
(6, 'Banking'),
(7, 'Financial analysis'),
(8, 'Mergers and acquisitions'),
(9, 'Corporate finance'),
(10, 'Commercial banking'),
(11, 'Java, Swift'),
(12, 'Financial ,investment '),
(13, 'Credit analysis'),
(14, 'Venture capital'),
(15, 'Treasury management');
select * from ldms_experience;

