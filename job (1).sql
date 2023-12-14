CREATE TABLE ldms_job (
  cid VARCHAR(3) NOT NULL ,
  job_role VARCHAR(25) ,
  salary INT NOT NULL,
  primary key (cid),
  foreign key (cid) references ldms_company (cid)
); 
insert into ldms_job (cid, job_role, salary)
values ('C01', 'Software Engineer',  120000),
('C02', 'Data Scientist',  130000),
('C03', 'CEO',  110000),
('C04', 'CEO',  120000),
('C05', 'CEO',  100000),
('C06', 'HR',  110000),
('C07', 'HR',  80000),
('C08', 'CEO',  90000),
('C09', 'CEO',  100000),
('C10', 'CEO',  100000);

select * from ldms_job;
insert into ldms_job (cid, job_role, salary)
values 
('C11', 'Consultant', 120000),
('C12', 'Consultant', 130000),
('C13', 'Consultant', 110000),
('C14', 'Consultant', 120000),
('C15', 'Consultant',  130000),
('C16', 'Teacher',  60000),
('C17', 'Youth Coordinator', 50000),
('C18', 'Program Coordinator',  40000),
('C19', 'Camp Counselor', 30000),
('C20', 'Volunteer Coordinator', 20000);
