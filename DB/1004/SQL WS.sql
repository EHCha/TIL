-- 1)
CREATE TABLE countries (
  id INTERGER PRIMARY KEY,
  room_num TEXT,
  check_in TEXT,
  check_out TEXT,
  grade TEXT,
  price INTEGER
);

-- 2)
INSERT INTO countries (id, room_num, check_in, check_out, grade, price) 
VALUES
  (1, 'B203', '2019-12-31', '2020-01-03', 'suite', 900),
  (2, '1102', '2020-01-04', '2020-01-08', 'suite', 850),
  (3, '303', '2020-01-01', '2020-01-03', 'deluxe', 500),
  (4, '807', '2020-01-04', '2020-01-07', 'superior', 300);

-- 3)
ALTER TABLE countries RENAME TO hotels;

-- 4)
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

-- 5)
SELECT grade, COUNT(*) AS number_of_grade FROM hotels GROUP BY grade ORDER BY number_of_grade DESC;

-- 6)
SELECT * FROM hotels WHERE room_num LIKE '%B%' OR grade = 'deluxe';

-- 7)
SELECT room_num, check_in, check_out, grade, price FROM hotels WHERE room_num NOT LIKE '%B%' and check_in = '2020-01-04' ORDER BY price ASC;

