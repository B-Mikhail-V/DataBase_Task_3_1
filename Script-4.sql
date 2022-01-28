select *from singers;
select *from genres;
select *from albums;
select *from tracks;
select *from collections;
select *from collectionstracks;
select *from singersalbums;
select *from singersgenres;

update tracks
set title = 'The Lady in my Life'
where id = 3;

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
delete from collections  
where id >= 0;
alter sequence collections_id_seq restart;

delete from collectionstracks  
where tracks_id >= 0;
alter sequence collectionstracks_id_seq restart;

delete from singersalbums  
where singers_id > 0;
alter sequence singersalbums_id_seq restart;

delete from singersgenres
where singers_id > 0;
alter sequence singersgenres_id_seq restart;