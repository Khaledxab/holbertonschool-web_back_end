-- creates a procedure ComputeAverageWeightedScoreForUser that computes the average weighted score for a user
-- The procedure takes 1 argument: user_id
-- The procedure updates the average_score column of the users table for the user with the user_id
-- The average_score is computed as the sum of the score * weight of all the projects that the user corrected, divided by the sum of the weight of all the projects that the user corrected
-- If the user didn't correct any project, the average_score is 0
-- The procedure should be created without any warnings
-- The procedure should be created without any errors
-- The procedure should be created without any notices
-- The procedure should be created without any debug messages
-- The procedure should be created without any info messages
-- The procedure should be created without any trace messages
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE total_weighted_score INT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    SELECT SUM(corrections.score * projects.weight)
        INTO total_weighted_score
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    SELECT SUM(projects.weight)
        INTO total_weight
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    IF total_weight = 0 THEN
        UPDATE users
            SET users.average_score = 0
            WHERE users.id = user_id;
    ELSE
        UPDATE users
            SET users.average_score = total_weighted_score / total_weight
            WHERE users.id = user_id;
    END IF;
END $$
DELIMITER ;