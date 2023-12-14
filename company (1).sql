CREATE TABLE ldms_company (
  cid VARCHAR(3) NOT NULL,
  company_name VARCHAR(20) ,
  industry VARCHAR(20) ,
  primary key (cid)
); 
insert into ldms_company (cid, company_name, industry)
values('C01', 'Google', 'Technology'),
('C02', 'Meta', 'Technology'),
('C03', 'Microsoft', 'Technology'),
('C04', 'Apple', 'Technology'),
('C05', 'Amazon', 'Technology'),
('C06', 'Goldman Sachs', 'Financial Services'),
('C07', 'JPMorgan Chase', 'Financial Services'),
('C08', 'Morgan Stanley', 'Financial Services'),
('C09', 'Citigroup', 'Financial Services'),
('C10', 'Bank of America', 'Financial Services');
select * from ldms_company;

insert into ldms_company (cid, company_name, industry)
values
('C11', 'Bain & Company', 'Consulting'),
('C12', 'McKinsey & Company', 'Consulting'),
('C13', 'BCG', 'Consulting'),
('C14', 'A.T. Kearney', 'Consulting'),
('C15', 'Deloitte', 'Consulting'),
('C16', 'New Public Schools', 'Education'),
('C17', 'Clubs of America', 'Nonprofit'),
('C18', 'YMCA of the USA', 'Nonprofit'),
('C19', 'American Red Cross', 'Nonprofit'),
('C20', 'Humanity Program', 'Nonprofit');
