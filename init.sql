CREATE DATABASE IF NOT EXISTS `flask`;
USE `flask`;
CREATE TABLE IF NOT EXISTS `user` (
                    `id` int NOT NULL AUTO_INCREMENT,
                    `name` varchar(20) NOT NULL,
                    `lastname` varchar(20) NOT NULL,
                    `role` varchar(20) NOT NULL,
                    PRIMARY KEY (`id`)
                    );