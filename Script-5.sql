select COUNT(name), g.title from singers s
join singersgenres sg on s.id = sg.singers_id 
join genres g on sg.genres_id = g.id
group by g.title;

select COUNT(t.title) from tracks t
join albums a on t.albums_id = a.id
where a.recording_year between '2019' and '2020';

select COUNT(t.title) from tracks t
join albums a on t.albums_id = a.id
where a.recording_year between '1982' and '1989';


select avg(duration), a.title  from tracks t
join albums a on t.albums_id = a.id
group by a.title;


select name, a.recording_year from singers s
join singersalbums sa on s.id = sa.singers_id 
join albums a on sa.albums_id = a.id
where a.recording_year != '2019';

select c.title from collections c 
join collectionstracks ct on c.id = ct.collections_id 
join tracks t on ct.tracks_id  = t.id 
join albums a on t.albums_id = a.id 
join singersalbums sa on a.id = sa.albums_id 
join singers s on sa.singers_id = s.id
where s.name = 'Frank Sinatra'
group by c.title
order by c.title;

select a.title, count(g.title)  from albums a 
join singersalbums sa on a.id = sa.albums_id 
join singers s on sa.singers_id = s.id
join singersgenres sg on s.id = sg.singers_id 
join genres g on sg.genres_id = g.id
group by a.title;

select s.name, count(g.title) from singers s
join singersgenres sg on s.id = sg.singers_id  
join genres g on sg.genres_id = g.id
group by s.name;

