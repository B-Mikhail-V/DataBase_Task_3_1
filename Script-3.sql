select * from singers;
delete from singers
where id >= 1;
alter sequence singers_id_seq restart;