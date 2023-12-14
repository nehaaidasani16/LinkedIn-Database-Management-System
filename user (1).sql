CREATE table ldms_user(
  id INT NOT NULL ,
  cid VARCHAR(3) NOT NULL,
  name VARCHAR(20) ,
  email VARCHAR(25) ,
  connections INT ,
  primary key (id),
  foreign key (cid) references ldms_company (cid)
);
insert into ldms_user(id,cid,name, email, connections )
 values(1,'C01', 'JohnDoe', 'john.doe@example.com',  500),
(2,'C02', 'JaneDoe', 'jane.doe@example.com',  1000),
(3,'C03', 'MarkZuck', 'mark.z@facebook.com',30000),
(4,'C04', 'JeffBezos', 'jeff.bezos@amazon.com', 50000),
(5,'C05', 'TimCook', 'tim.cook@apple.com', 20000),
(6,'C06','SachinGaj', 'sachin@flipkart.com', 10000),
(7,'C07', 'AmitDuth', 'amit.duth@amazon.in', 5000),
(8,'C08', 'VijaySham', 'vijay.sham@paytm.com', 3000),
(9,'C09', 'BooRaveendran', 'boo.ra@byjus.com', 2000),
(10,'C10', 'RiteshAaga', 'ritesh@oyorooms.com', 1000),
(11,'C06','SonuSood', 'soso@flipkart.com', 10000),
(12,'C07', 'AmanDatt', 'aman.dath@amazon.in', 5000),
(13,'C08', 'VimanBish', 'vimanb@paytm.com', 3000),
(14,'C09', 'RahulRoy', 'rahul@byjus.com', 2000),
(15,'C10', 'AkhilJosh', 'akjo@oyorooms.com', 1000);
select * from ldms_user;

