CREATE TABLE ldms_post (
  id INT NOT NULL,
  post_content VARCHAR(45) ,
  likes INT ,
  primary key (id),
  foreign key (id) references ldms_user (id)
);
insert into ldms_post (id, post_content, likes)
values(1, "I'm excited to start a new chapter !", 500),
(2, "I'm grateful for the opportunity to work .",300),
(3, "I'm passionate about using technology .", 2000),
(4, "I'm always looking for new ways to learn.", 100),
(5, "I'm grateful for the support .", 50),
(6, "I'm excited to see the future .", 200),
(7, "I'm excited to share my new blog post ", 4000),
(8, "I'm looking forward for conference .", 2500),
(9, "I'm grateful for the opportunity .", 70),
(10, "I'm passionate about diversity", 100),
(11, "I'm excited to attend.", 700),
(12, "I'm excited to share my success journey ", 400),
(13, "I'm looking forward to this event.", 250),
(14, "I'm grateful for increment .", 700),
(15, "I'm excited about this new life", 10);
select * from ldms_post;
