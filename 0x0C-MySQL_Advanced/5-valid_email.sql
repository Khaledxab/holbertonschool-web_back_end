-- Creates trigger to reset the attribute valid_email 

DELIMITER $$
CREATE TRIGGER valid_email BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    IF NEW.email NOT REGEXP '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' THEN
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email = 1;
    END IF;
END$$
DELIMITER ;
