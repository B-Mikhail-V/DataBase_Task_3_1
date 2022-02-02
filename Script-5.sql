/*количество исполнителей в каждом жанре*/
select COUNT(s.name) singers_qty, g.title genre from singers s
join singersgenres sg on s.id = sg.singers_id 
join genres g on sg.genres_id = g.id
group by g.title;

/*количество треков, вошедших в альбомы 2019-2020 годов*/
select COUNT(t.title) track_qty from tracks t
join albums a on t.albums_id = a.id
where a.recording_year between '2019' and '2020';

/*количество треков, вошедших в альбомы 1982-1989 годов*/
select COUNT(t.title) track_qty from tracks t
join albums a on t.albums_id = a.id
where a.recording_year between '1982' and '1989';


/*средн€€ продолжительность треков по каждому альбому*/
select avg(t.duration) avr_duration, a.title album_name  from tracks t
join albums a on t.albums_id = a.id
group by a.id;


/*все исполнители, которые не выпустили альбомы в 2021 году*/
select distinct s.name singer from singers s
join singersalbums sa on s.id = sa.singers_id 
join albums a on sa.albums_id = a.id
where a.recording_year != '2021';

/*названи€ сборников, в которых присутствует конкретный исполнитель*/
select c.title collection from collections c 
join collectionstracks ct on c.id = ct.collections_id 
join tracks t on ct.tracks_id  = t.id 
join albums a on t.albums_id = a.id 
join singersalbums sa on a.id = sa.albums_id 
join singers s on sa.singers_id = s.id
where s.name = 'Frank Sinatra'
group by c.id
order by c.id;

/*название альбомов, в которых присутствуют исполнители более 1 жанра*/
select a.title album from albums a 
join singersalbums sa on a.id = sa.albums_id 
join singers s on sa.singers_id = s.id
join singersgenres sg on s.id = sg.singers_id 
join genres g on sg.genres_id = g.id
group by a.id
having count(g.title) > 1;

/*наименование треков, которые не вход€т в сборники*/
select t.title track from tracks t
left join collectionstracks ct on t.id = ct.tracks_id
where ct.collections_id is null;

/*исполнител€(-ей), написавшего самый короткий по продолжительности трек*/
select s.name singer from singers s
join singersalbums sa on s.id = sa.singers_id 
join albums a on sa.albums_id = a.id
join tracks t on a.id = t.albums_id
where t.duration = (
select min(t.duration) from tracks t);


/*название альбомов, содержащих Ќј»ћ≈Ќ№Ў≈≈ количество треков*/
select a.title album from tracks t
join albums a on t.albums_id = a.id 
group by a.id 
having count(t.id) = (
select count(t.id) cc from tracks t
group by albums_id 
order by cc
limit 1
);

/*название альбомов, содержащих Ќј»ЅќЋ№Ў≈≈ количество треков*/
select a.title album from tracks t
join albums a on t.albums_id = a.id 
group by a.id 
having count(t.id) = (
select count(t.id) cc from tracks t
group by albums_id 
order by cc desc
limit 1
);
