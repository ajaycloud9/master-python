SELECT 
    p1.person_id,
    p1.first_name,
    p1.last_name,
    p1.date AS date1,
    p1.weight AS weight1,
    p2.date AS date2,
    p2.weight AS weight2,
    ROUND((p2.weight - p1.weight), 2) AS weight_difference
FROM 
    Person p1
JOIN 
    Person p2 
ON 
    p1.person_id = p2.person_id 
    AND p1.date = '2024-09-22'  -- First date
    AND p2.date = '2024-09-29'   -- Second date
ORDER BY 
    weight_difference ASC;  -- Sort by weight_difference in ascending order
