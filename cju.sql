CREATE TABLE link_cju (
  id INT NOT NULL,
  cid VARCHAR(25) NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  email VARCHAR(50) NOT NULL,
  connections INT NOT NULL,
  cname VARCHAR(50) NOT NULL,
  cindustry VARCHAR(100) NOT NULL,
  clocation VARCHAR(100) NOT NULL,
  job_title VARCHAR(100) NOT NULL,
  salary INT NOT NULL,
  PRIMARY KEY (id)
);
INSERT INTO link_cju (
  id,
  cid,
  first_name,
  last_name,
  email,
  connections,
  cname,
  cindustry,
  clocation,
  job_title,
  salary
)

SELECT
  link_users.id,
  link_company.cid,
  link_users.first_name,
  link_users.last_name,
  link_users.email,
  link_users.connections,
  link_company.cname,
  link_company.cindustry,
  link_company.clocation,
  link_job.job_title,
  link_job.salary
FROM link_users
LEFT JOIN link_company ON link_users.c_id = link_company.cid
LEFT JOIN link_job ON link_company.cid = link_job.jid;
select * from link_cju;

drop table link_cju;