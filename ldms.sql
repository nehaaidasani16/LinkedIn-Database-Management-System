

alter table ldms add foreign key (cid) REFERENCES ldms_company (cid);

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

insert into ldms (id, cid, name, email, connections, post_content, likes, institute_name, passing_year, skills, job_role, company_name, industry, salary )
values(17, 'C04','Koo Joon', 'bon-joon.koo@lge.com', 10000, 'I am excited to see what the future holds.', 2400, 'UofCalifornia', 2000, 'youth development, mentoring', 'Youth Program Coordinator', 'Clubs of America', 'Nonprofit', 70000),
(18, 'C09','Lee Jin', 'hae-jin.lee@naver.com', 5000, 'I am a Data Scientist at Amazon',6000, 'UofCalifornia', 1995, 'volunteer&event planning', 'After-School Program ', 'YMCA of the USA', 'Nonprofit', 80000),
(19, 'C07','Kim Soo', 'beom-soo@kakao.com', 3000, 'I am a Software Engineer at Microsoft', 4500, 'UofCalifornia', 1986, ' community development','Camp Counselor', 'American Red Cross', 'Nonprofit', 100000);


