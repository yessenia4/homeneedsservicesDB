-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 06, 2020 at 12:16 AM
-- Server version: 5.7.28
-- PHP Version: 7.2.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `HNS`
--

-- --------------------------------------------------------

--
-- Table structure for table `administrators`
--

CREATE TABLE `administrators` (
  `adminID` int(11) NOT NULL,
  `adminEmail` varchar(100) NOT NULL,
  `adminPassword` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `contractorApplications`
--

CREATE TABLE `contractorApplications` (
  `contractorID` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `ssn` int(9) NOT NULL,
  `address` varchar(150) NOT NULL,
  `aptNum` varchar(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zipcode` int(9) NOT NULL,
  `willingTravel` int(11) NOT NULL,
  `phone` int(11) NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `dateApp` date NOT NULL,
  `adminID` int(11) NOT NULL,
  `dateApproved` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `contractors`
--

CREATE TABLE `contractors` (
  `contractorID` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `ssn` int(9) NOT NULL,
  `scheduleID` int(11) NOT NULL,
  `address` varchar(150) NOT NULL,
  `aptNum` varchar(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zipCode` int(9) NOT NULL,
  `willingTravel` int(11) NOT NULL,
  `phone` int(11) NOT NULL,
  `dob` date NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `contractorsServiceRecords`
--

CREATE TABLE `contractorsServiceRecords` (
  `contractorID` int(11) NOT NULL,
  `serviceID` int(11) NOT NULL,
  `chargeService` decimal(10,2) NOT NULL,
  `yearsExperience` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `contractors_background`
--

CREATE TABLE `contractors_background` (
  `contractorID` int(11) NOT NULL,
  `approved` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `contractPayment`
--

CREATE TABLE `contractPayment` (
  `contractID` int(11) NOT NULL,
  `time` datetime NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `approved` tinyint(1) NOT NULL,
  `refund` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `contracts`
--

CREATE TABLE `contracts` (
  `contractID` int(11) NOT NULL,
  `serviceID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `description` varchar(500) NOT NULL,
  `dateService` date NOT NULL,
  `startTime` time NOT NULL,
  `serviceZipCode` int(9) NOT NULL,
  `serviceAddress` varchar(150) NOT NULL,
  `serviceAptNum` varchar(10) NOT NULL,
  `contractorID` int(11) NOT NULL,
  `paymentID` int(11) NOT NULL,
  `dateContract` datetime NOT NULL,
  `cancelContract` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `paymentInfo`
--

CREATE TABLE `paymentInfo` (
  `paymentID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `cardType` varchar(20) NOT NULL,
  `cardName` varchar(150) NOT NULL,
  `cardNumber` int(11) NOT NULL,
  `cvv` int(11) NOT NULL,
  `billingAddress` varchar(150) NOT NULL,
  `expDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `contractorID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `number_rating` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `comments` varchar(300) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `schedules`
--

CREATE TABLE `schedules` (
  `scheduleID` int(11) NOT NULL,
  `time_slot_ID` int(11) NOT NULL,
  `busy/available` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `serviceApplications`
--

CREATE TABLE `serviceApplications` (
  `serviceAppID` int(11) NOT NULL,
  `contractorID` int(11) NOT NULL,
  `serviceID` int(11) NOT NULL,
  `dateApp` date NOT NULL,
  `adminID` int(11) NOT NULL,
  `dateApproved` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `serviceCategories`
--

CREATE TABLE `serviceCategories` (
  `serviceID` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `subServiceID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `subServiceCategories`
--

CREATE TABLE `subServiceCategories` (
  `subServiceID` int(11) NOT NULL,
  `sub_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `time_slots`
--

CREATE TABLE `time_slots` (
  `time_slot_ID` int(11) NOT NULL,
  `day` date NOT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userID` int(11) NOT NULL,
  `firstName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `phone` int(11) NOT NULL,
  `address` varchar(150) NOT NULL,
  `aptNum` varchar(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zipCode` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administrators`
--
ALTER TABLE `administrators`
  ADD PRIMARY KEY (`adminID`);

--
-- Indexes for table `contractorApplications`
--
ALTER TABLE `contractorApplications`
  ADD PRIMARY KEY (`contractorID`),
  ADD UNIQUE KEY `ssn` (`ssn`),
  ADD KEY `adminConstraint3` (`adminID`);

--
-- Indexes for table `contractors`
--
ALTER TABLE `contractors`
  ADD PRIMARY KEY (`contractorID`),
  ADD UNIQUE KEY `scheduleID` (`scheduleID`),
  ADD UNIQUE KEY `ssn` (`ssn`);

--
-- Indexes for table `contractorsServiceRecords`
--
ALTER TABLE `contractorsServiceRecords`
  ADD PRIMARY KEY (`contractorID`,`serviceID`),
  ADD KEY `serviceConstraint` (`serviceID`);

--
-- Indexes for table `contractors_background`
--
ALTER TABLE `contractors_background`
  ADD PRIMARY KEY (`contractorID`);

--
-- Indexes for table `contractPayment`
--
ALTER TABLE `contractPayment`
  ADD PRIMARY KEY (`contractID`);

--
-- Indexes for table `contracts`
--
ALTER TABLE `contracts`
  ADD PRIMARY KEY (`contractID`),
  ADD KEY `userConstraint4` (`userID`),
  ADD KEY `contractorConstraint4` (`contractorID`),
  ADD KEY `serviceConstraint2` (`serviceID`),
  ADD KEY `paymentConstraint` (`paymentID`);

--
-- Indexes for table `paymentInfo`
--
ALTER TABLE `paymentInfo`
  ADD PRIMARY KEY (`paymentID`),
  ADD KEY `userConstraint` (`userID`);

--
-- Indexes for table `rating`
--
ALTER TABLE `rating`
  ADD PRIMARY KEY (`contractorID`,`userID`),
  ADD KEY `userConstraint2` (`userID`);

--
-- Indexes for table `schedules`
--
ALTER TABLE `schedules`
  ADD PRIMARY KEY (`scheduleID`,`time_slot_ID`),
  ADD KEY `timeConstraint` (`time_slot_ID`);

--
-- Indexes for table `serviceApplications`
--
ALTER TABLE `serviceApplications`
  ADD PRIMARY KEY (`serviceAppID`,`serviceID`),
  ADD KEY `contractorConstraint5` (`contractorID`),
  ADD KEY `serviceConstraint3` (`serviceID`),
  ADD KEY `adminConstraint` (`adminID`);

--
-- Indexes for table `serviceCategories`
--
ALTER TABLE `serviceCategories`
  ADD PRIMARY KEY (`serviceID`),
  ADD KEY `subServiceConstraint` (`subServiceID`);

--
-- Indexes for table `subServiceCategories`
--
ALTER TABLE `subServiceCategories`
  ADD PRIMARY KEY (`subServiceID`);

--
-- Indexes for table `time_slots`
--
ALTER TABLE `time_slots`
  ADD PRIMARY KEY (`time_slot_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `contractorApplications`
--
ALTER TABLE `contractorApplications`
  ADD CONSTRAINT `adminConstraint3` FOREIGN KEY (`adminID`) REFERENCES `administrators` (`adminID`);

--
-- Constraints for table `contractors`
--
ALTER TABLE `contractors`
  ADD CONSTRAINT `appContractorConstraint2` FOREIGN KEY (`contractorID`) REFERENCES `contractorApplications` (`contractorID`) ON DELETE CASCADE;

--
-- Constraints for table `contractorsServiceRecords`
--
ALTER TABLE `contractorsServiceRecords`
  ADD CONSTRAINT `contractorConstraint3` FOREIGN KEY (`contractorID`) REFERENCES `contractors` (`contractorID`) ON DELETE CASCADE,
  ADD CONSTRAINT `serviceConstraint` FOREIGN KEY (`serviceID`) REFERENCES `serviceCategories` (`serviceID`) ON DELETE CASCADE;

--
-- Constraints for table `contractors_background`
--
ALTER TABLE `contractors_background`
  ADD CONSTRAINT `contractorConstraint` FOREIGN KEY (`contractorID`) REFERENCES `contractors` (`contractorID`) ON DELETE CASCADE;

--
-- Constraints for table `contractPayment`
--
ALTER TABLE `contractPayment`
  ADD CONSTRAINT `contractConstraint` FOREIGN KEY (`contractID`) REFERENCES `contracts` (`contractID`) ON DELETE CASCADE;

--
-- Constraints for table `contracts`
--
ALTER TABLE `contracts`
  ADD CONSTRAINT `contractorConstraint4` FOREIGN KEY (`contractorID`) REFERENCES `contractors` (`contractorID`) ON DELETE CASCADE,
  ADD CONSTRAINT `paymentConstraint` FOREIGN KEY (`paymentID`) REFERENCES `paymentInfo` (`paymentID`),
  ADD CONSTRAINT `serviceConstraint2` FOREIGN KEY (`serviceID`) REFERENCES `serviceCategories` (`serviceID`) ON DELETE CASCADE,
  ADD CONSTRAINT `userConstraint4` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE CASCADE;

--
-- Constraints for table `paymentInfo`
--
ALTER TABLE `paymentInfo`
  ADD CONSTRAINT `userConstraint` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE NO ACTION;

--
-- Constraints for table `rating`
--
ALTER TABLE `rating`
  ADD CONSTRAINT `contractorConstraint2` FOREIGN KEY (`contractorID`) REFERENCES `contractors` (`contractorID`) ON DELETE CASCADE,
  ADD CONSTRAINT `userConstraint2` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE NO ACTION;

--
-- Constraints for table `schedules`
--
ALTER TABLE `schedules`
  ADD CONSTRAINT `scheduleConstraint` FOREIGN KEY (`scheduleID`) REFERENCES `contractors` (`scheduleID`) ON DELETE CASCADE,
  ADD CONSTRAINT `timeConstraint` FOREIGN KEY (`time_slot_ID`) REFERENCES `time_slots` (`time_slot_ID`) ON DELETE CASCADE;

--
-- Constraints for table `serviceApplications`
--
ALTER TABLE `serviceApplications`
  ADD CONSTRAINT `adminConstraint` FOREIGN KEY (`adminID`) REFERENCES `administrators` (`adminID`),
  ADD CONSTRAINT `contractorConstraint5` FOREIGN KEY (`contractorID`) REFERENCES `contractors` (`contractorID`) ON DELETE CASCADE,
  ADD CONSTRAINT `serviceConstraint3` FOREIGN KEY (`serviceID`) REFERENCES `serviceCategories` (`serviceID`) ON DELETE CASCADE;

--
-- Constraints for table `serviceCategories`
--
ALTER TABLE `serviceCategories`
  ADD CONSTRAINT `subServiceConstraint` FOREIGN KEY (`subServiceID`) REFERENCES `subServiceCategories` (`subServiceID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
