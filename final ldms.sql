CREATE TABLE ldms (
  id INT NOT NULL,
  cid VARCHAR(3) NOT NULL,
  name VARCHAR(20) ,
  email VARCHAR(25) ,
  connections INT ,
  post_content VARCHAR(45) ,
  likes INT ,
  institute_name VARCHAR(20) ,
  passing_year INT NOT NULL,
  skills varchar(30) ,
  job_role VARCHAR(25) ,
  company_name VARCHAR(20) ,
  industry VARCHAR(20),
  salary INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (cid) REFERENCES ldms_company (cid)
);

INSERT INTO ldms (
  id,
  cid,
  name,
  email,
  connections,
  post_content,
  likes,
  institute_name,
  passing_year ,
  skills  ,
  job_role ,
  company_name ,
  industry,
  salary 
)
SELECT
  ldms_user.id,
  ldms_user.cid,
  ldms_user.name,
  ldms_user.email,
  ldms_user.connections,
  ldms_post.post_content,
  ldms_post.likes,
  ldms_education.institute_name,
  ldms_education.passing_year ,
  ldms_experience.skills  ,
  ldms_job.job_role ,
  ldms_company.company_name ,
  ldms_company.industry,
  ldms_job.salary 
FROM ldms_user
LEFT JOIN ldms_post ON ldms_user.id = ldms_post.id
LEFT JOIN ldms_education ON ldms_user.id = ldms_education.id
LEFT JOIN ldms_experience ON ldms_user.id = ldms_experience.id
LEFT JOIN ldms_job ON ldms_user.cid = ldms_job.cid
LEFT JOIN ldms_company ON ldms_user.cid = ldms_company.cid
WHERE ldms_user.id IS NOT NULL;
select * from ldms;


