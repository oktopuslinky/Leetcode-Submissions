# Write your MySQL query statement below
SELECT project_id, ROUND(AVG(experience_years),2) as average_years
FROM (Employee NATURAL JOIN Project as j)
GROUP BY project_id