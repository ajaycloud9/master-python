select * from employee;

SELECT COUNT(emp_id) 
FROM employee
WHERE sex = 'F' AND birth_day > '1971-01-01';

SELECT SUM(salary)
FROM employee;

-- How many males and females are their in the company ?

SELECT COUNT(sex), sex
FROM employee
GROUP BY sex;

-- Find the total sales of each salesman

SELECT SUM(total_sales), emp_id
FROM works_with
GROUP BY emp_id;

-- Find any clients who are an LLC
-- % = any characters, _ = One Character
SELECT * 
FROM client
Where client_name LIKE '%LLC';

-- Find any client who is born in Oct

SELECT * 
FROM employee
Where birth_day LIKE '____-10%';

-- Find the list of all the clients and branch supplier names

SELECT client_name
FROM client
UNION 
SELECT supplier_name
FROM branch_supplier;

-- Find a list of all the money spent or earned by the company

SELECT salary
FROM employee
UNION
SELECT total_sales
FROM works_with;


-- Find all the branches and the names of their manager

SELECT employee.emp_id, employee.first_name, employee.last_name, branch.branch_name
FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id;

-- 4 types of join (Left join, Inner Join)
-- Left join (We include everything from the left)
-- Right Join (We include everything from the right (Rest all the elements coming from left is NULL))
-- FULL OUTER JOIN (Left and Right join combined)

SELECT employee.emp_id, employee.first_name, employee.last_name, works_with.total_sales
FROM employee
JOIN works_with
ON employee.emp_id = works_with.emp_id;

-- Find names of all employees who have sold over
-- 30,000 to as single client

SELECT employee.first_name, employee.last_name
FROM employee
WHERE employee.emp_id IN (
    SELECT works_with.emp_id
    FROM works_with
    WHERE works_with.total_sales > 30000
);


-- Find all the clients who are handled by the branch
-- that Micheal scott manages, Assume you know Michale's ID

SELECT client.client_name
FROM client
WHERE client.branch_id = (
    SELECT branch.branch_id
    FROM branch
    WHERE branch.mgr_id = 102
    LIMIT 1 
);

-- In the cases like above sql goes from inwards to outwards as it sees there is a syntax attached to this

-- Trigger will happen

CREATE TABLE trigger_test (
    message VARCHAR(100)
);


-- Run this in mysql command line

DELIMITER $$
CREATE 
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES('Add new employee');
    END$$
DELIMITER ;

-- An example where we are adding the new in first name

DELIMITER $$
CREATE 
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES(NEW.first_name);
    END$$
DELIMITER ;

-- AN example for trigger having if and else condition

DELIMITER $$
CREATE 
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES(NEW.first_name);
    END$$
DELIMITER ;


INSERT INTO employee
VALUES(110,'VIJAY','SINGH', '1993-12-23','M',160000,107,3);