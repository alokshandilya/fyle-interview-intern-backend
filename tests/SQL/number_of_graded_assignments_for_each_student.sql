-- Write query to get number of graded assignments for each student:

SELECT students.id, COUNT(assignments.id) FROM students
LEFT JOIN assignments ON students.id = assignments.student_id AND assignments.state = 'GRADED'
GROUP BY students.id;
