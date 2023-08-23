INSERT INTO `Api_Logo` VALUES (null, 'Logo 1');
INSERT INTO `Api_Logo` VALUES (null, 'Logo 2');
INSERT INTO `Api_Logo` VALUES (null, 'Logo 3');
INSERT INTO `Api_Logo` VALUES (null, 'Logo 4');
INSERT INTO `Api_Logo` VALUES (null, 'Logo 5');

DELETE FROM django_session WHERE session_key='tayitllxgw2s3vzzhtfbzbkfvvktuipc'

UPDATE auth_user 
SET is_active=1
WHERE id=1

UPDATE auth_user 
SET is_staff=0
WHERE id=1
