select *from singers;
select *from genres;
select *from albums;
select *from tracks;
select *from singersgenres;

insert into singers (name)
values
('Michael Jackson'),
('Madonna'),
('Frank Sinatra'),
('Paul McCartney'),
('Sting'),
('Алла Пугачева'),
('Elton John');
delete from singers
where id >= 0;
alter sequence singers_id_seq restart;
delete from genres 
where id >= 0;
alter sequence genres_id_seq restart;
delete from albums  
where id >= 0;
alter sequence albums_id_seq restart;
delete from tracks  
where id >= 0;
alter sequence tracks_id_seq restart;

delete from singersgenres
where singers_id > 0;
alter sequence singersgenres_id_seq restart;