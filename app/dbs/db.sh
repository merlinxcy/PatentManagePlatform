create database web;
use web;


/*
普通用户注册信息表
*/
create table person_register(
  id int primary key,
  name varchar(10),
  phone varchar(13),
  location varchar(10),
  card_type varchar(5),
  card_num varchar(20),
  address varchar(50),
  password varchar(30),
  mail_address varchar(50),
  register_status int
);
/*
企业用户注册信息表
*/
create table company_register(
  id int primary key,
  name varchar(10),
  country varchar(10),
  card_type(10),
  card_num(20),
  company_address varchar(50),
  code_num varchar(10),
  location varchar(10),
  address varchar(50)
  password varchar(50),
  mail varchar(20),
  person_phone varchar(20),
  person_name varchar(10),
  person_address varchar(50),
  register_status int
);
/*
普通用户登录信息表
*/
create table person_login(
  id int primary key,
  name varchar(10),
  phone varchar(13),
  location varchar(10),
  card_type varchar(5),
  card_num varchar(20),
  address varchar(50),
  password varchar(30),
  mail_address varchar(50),
  account_status int
);
/*
企业用户登录信息表
*/
create table company_login(
  id int primary key,
  name varchar(10),
  country varchar(10),
  card_type(10),
  card_num(20),
  company_address varchar(50),
  code_num varchar(10),
  location varchar(10),
  address varchar(50)
  password varchar(50),
  mail varchar(20),
  person_phone varchar(20),
  person_name varchar(10),
  person_address varchar(50),
  account_status int
);
/*
普通用户专利申请信息表
id int primary key ;唯一id
patent_name varchar(50) ;专利名
patent_class varchar(10) ; 专利类别
patent_person_name varchar(10);
patent_person_phone varchar(20);
patent_person_idcard varchar(30);
patent_person_address varchar(100);
patent_append_time varchar(10);
patent_priority int;
patent_description varchar(200);
patent_documentfile_location varchar(50);
*/
create table patent_apply(
  id int primary key,
  patent_name varchar(50),
  patent_class varchar(10),
  patent_person_name varchar(10),
  patent_person_phone varchar(20),
  patent_person_idcard varchar(30),
  patent_person_address varchar(100),
  patent_append_time varchar(10),
  patent_priority int,
  patent_description varchar(200),
  patent_documentfile_location varchar(50)
);


