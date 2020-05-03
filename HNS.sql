-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 03, 2020 at 11:44 PM
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

--
-- Dumping data for table `administrators`
--

INSERT INTO `administrators` (`adminID`, `adminEmail`, `adminPassword`) VALUES
(1, 'yessenia.yess98@hotmail.com', 'admin1');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add administrators', 7, 'add_administrators'),
(26, 'Can change administrators', 7, 'change_administrators'),
(27, 'Can delete administrators', 7, 'delete_administrators'),
(28, 'Can view administrators', 7, 'view_administrators'),
(29, 'Can add paymentinfo', 8, 'add_paymentinfo'),
(30, 'Can change paymentinfo', 8, 'change_paymentinfo'),
(31, 'Can delete paymentinfo', 8, 'delete_paymentinfo'),
(32, 'Can view paymentinfo', 8, 'view_paymentinfo'),
(33, 'Can add serviceapplications', 9, 'add_serviceapplications'),
(34, 'Can change serviceapplications', 9, 'change_serviceapplications'),
(35, 'Can delete serviceapplications', 9, 'delete_serviceapplications'),
(36, 'Can view serviceapplications', 9, 'view_serviceapplications'),
(37, 'Can add servicecategories', 10, 'add_servicecategories'),
(38, 'Can change servicecategories', 10, 'change_servicecategories'),
(39, 'Can delete servicecategories', 10, 'delete_servicecategories'),
(40, 'Can view servicecategories', 10, 'view_servicecategories'),
(41, 'Can add services', 11, 'add_services'),
(42, 'Can change services', 11, 'change_services'),
(43, 'Can delete services', 11, 'delete_services'),
(44, 'Can view services', 11, 'view_services'),
(45, 'Can add time slots', 12, 'add_timeslots'),
(46, 'Can change time slots', 12, 'change_timeslots'),
(47, 'Can delete time slots', 12, 'delete_timeslots'),
(48, 'Can view time slots', 12, 'view_timeslots'),
(49, 'Can add users', 13, 'add_users'),
(50, 'Can change users', 13, 'change_users'),
(51, 'Can delete users', 13, 'delete_users'),
(52, 'Can view users', 13, 'view_users'),
(53, 'Can add contracts', 14, 'add_contracts'),
(54, 'Can change contracts', 14, 'change_contracts'),
(55, 'Can delete contracts', 14, 'delete_contracts'),
(56, 'Can view contracts', 14, 'view_contracts'),
(57, 'Can add contractpayment', 15, 'add_contractpayment'),
(58, 'Can change contractpayment', 15, 'change_contractpayment'),
(59, 'Can delete contractpayment', 15, 'delete_contractpayment'),
(60, 'Can view contractpayment', 15, 'view_contractpayment'),
(61, 'Can add contractors background', 16, 'add_contractorsbackground'),
(62, 'Can change contractors background', 16, 'change_contractorsbackground'),
(63, 'Can delete contractors background', 16, 'delete_contractorsbackground'),
(64, 'Can view contractors background', 16, 'view_contractorsbackground'),
(65, 'Can add rating', 17, 'add_rating'),
(66, 'Can change rating', 17, 'change_rating'),
(67, 'Can delete rating', 17, 'delete_rating'),
(68, 'Can view rating', 17, 'view_rating'),
(69, 'Can add schedules', 18, 'add_schedules'),
(70, 'Can change schedules', 18, 'change_schedules'),
(71, 'Can delete schedules', 18, 'delete_schedules'),
(72, 'Can view schedules', 18, 'view_schedules'),
(73, 'Can add contractorsservicerecords', 19, 'add_contractorsservicerecords'),
(74, 'Can change contractorsservicerecords', 19, 'change_contractorsservicerecords'),
(75, 'Can delete contractorsservicerecords', 19, 'delete_contractorsservicerecords'),
(76, 'Can view contractorsservicerecords', 19, 'view_contractorsservicerecords'),
(77, 'Can add contractorapplications', 20, 'add_contractorapplications'),
(78, 'Can change contractorapplications', 20, 'change_contractorapplications'),
(79, 'Can delete contractorapplications', 20, 'delete_contractorapplications'),
(80, 'Can view contractorapplications', 20, 'view_contractorapplications'),
(81, 'Can add contractors', 21, 'add_contractors'),
(82, 'Can change contractors', 21, 'change_contractors'),
(83, 'Can delete contractors', 21, 'delete_contractors'),
(84, 'Can view contractors', 21, 'view_contractors');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `contractorApplications`
--

CREATE TABLE `contractorApplications` (
  `contractorID` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `ssn` int(11) NOT NULL,
  `address` varchar(150) NOT NULL,
  `aptNum` varchar(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zipcode` int(9) NOT NULL,
  `willingTravel` int(11) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `dateApp` date NOT NULL,
  `adminID` int(11) DEFAULT NULL,
  `dateApproved` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contractorApplications`
--

INSERT INTO `contractorApplications` (`contractorID`, `name`, `ssn`, `address`, `aptNum`, `city`, `state`, `zipcode`, `willingTravel`, `phone`, `dob`, `email`, `password`, `dateApp`, `adminID`, `dateApproved`) VALUES
(1, 'Clark Kent', 123456789, '517 Market St', '3D', 'Metropolis', 'IL', 62960, 50, '9563814675', '1938-04-18', 'clark.kent@dailyplanet.com', 'superman', '2020-05-02', 1, '2020-05-02'),
(2, 'Joe Doe', 234567891, '1201 W University Dr', '', 'Edinburg', 'TX', 78539, 70, '9566657120', '1996-05-29', 'john.doe@fakeEmail.com', 'contractor2', '2020-05-03', 1, '2020-05-03'),
(3, 'Kassie Wayne', 345678912, '1 W University Blvd', '', 'Brownsville', 'TX', 78520, 50, '9562030500', '2000-07-25', 'kassie.wayner@wayneContractor.com', 'wayne1', '2020-05-01', NULL, NULL);

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
  `phone` varchar(15) NOT NULL,
  `dob` date NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contractors`
--

INSERT INTO `contractors` (`contractorID`, `name`, `ssn`, `scheduleID`, `address`, `aptNum`, `city`, `state`, `zipCode`, `willingTravel`, `phone`, `dob`, `password`, `email`) VALUES
(1, 'Clark Kent', 123456789, 1, '517 Market St', '3D', 'Metropolis', 'IL', 62960, 100, '9563814675', '1938-04-18', 'superman', 'clark.kent@dailyplanet.com'),
(2, 'Joe Doe', 234567891, 2, '1201 W University Dr', '', 'Edinburg', 'TX', 78539, 70, '9566657120', '1996-05-29', 'contractor2', 'john.doe@fakeEmail.com');

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

--
-- Dumping data for table `contractorsServiceRecords`
--

INSERT INTO `contractorsServiceRecords` (`contractorID`, `serviceID`, `chargeService`, `yearsExperience`) VALUES
(1, 8, '7.25', 2),
(2, 8, '8.36', 2);

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
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'hns', 'administrators'),
(20, 'hns', 'contractorapplications'),
(21, 'hns', 'contractors'),
(16, 'hns', 'contractorsbackground'),
(19, 'hns', 'contractorsservicerecords'),
(15, 'hns', 'contractpayment'),
(14, 'hns', 'contracts'),
(8, 'hns', 'paymentinfo'),
(17, 'hns', 'rating'),
(18, 'hns', 'schedules'),
(9, 'hns', 'serviceapplications'),
(10, 'hns', 'servicecategories'),
(11, 'hns', 'services'),
(12, 'hns', 'timeslots'),
(13, 'hns', 'users'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-04-16 05:24:45.181485'),
(2, 'auth', '0001_initial', '2020-04-16 05:24:45.511229'),
(3, 'admin', '0001_initial', '2020-04-16 05:24:45.592850'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-04-16 05:24:45.603605'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-04-16 05:24:45.623449'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-04-16 05:24:45.680642'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-04-16 05:24:45.690990'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-04-16 05:24:45.704296'),
(9, 'auth', '0004_alter_user_username_opts', '2020-04-16 05:24:45.714162'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-04-16 05:24:45.744669'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-04-16 05:24:45.747783'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-04-16 05:24:45.757930'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-04-16 05:24:45.773343'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-04-16 05:24:45.787343'),
(15, 'sessions', '0001_initial', '2020-04-16 05:24:45.812572'),
(16, 'hns', '0001_initial', '2020-04-16 05:40:21.618413'),
(17, 'hns', '0002_auto_20200420_2302', '2020-04-20 23:02:23.955942'),
(18, 'hns', '0003_auto_20200424_1924', '2020-04-24 19:24:12.261746'),
(19, 'auth', '0010_alter_group_name_max_length', '2020-04-24 20:48:38.753366'),
(20, 'auth', '0011_update_proxy_permissions', '2020-04-24 20:48:38.775905'),
(21, 'hns', '0005_auto_20200424_2109', '2020-04-25 22:09:33.040443'),
(22, 'hns', '0006_auto_20200424_2121', '2020-04-25 22:09:33.073376'),
(23, 'hns', '0007_users_last_login', '2020-04-25 22:09:33.101232'),
(24, 'hns', '0008_auto_20200425_2045', '2020-04-25 22:09:33.107701'),
(25, 'hns', '0009_auto_20200425_2049', '2020-04-25 22:09:33.113864'),
(26, 'hns', '0010_users_is_active', '2020-04-25 22:09:33.146971'),
(27, 'hns', '0011_auto_20200425_2140', '2020-04-25 22:09:33.153594'),
(28, 'hns', '0013_auto_20200426_0412', '2020-05-02 05:03:21.352566'),
(29, 'hns', '0015_auto_20200428_0149', '2020-05-02 22:53:41.854471'),
(30, 'hns', '0016_auto_20200502_0448', '2020-05-02 22:53:41.865239'),
(31, 'hns', '0017_auto_20200502_0456', '2020-05-02 22:53:41.872853'),
(32, 'hns', '0019_auto_20200502_2244', '2020-05-02 22:55:01.973792');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('10bmudpmpekfukzvqbcd75ghssp9eq1b', 'MmJiM2FkMzMyOWRkODYyNTE3MzI1MzIwYzU0MTg2NmQ4MGExZTUzMDp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2JlY29tZUNvbnRyYWN0b3IvIn0=', '2020-05-14 03:13:31.788571'),
('2hleillbd4r7mklt2srbni23oesgrnfv', 'NjNhZGNmNjEwNTZiM2M5MjhiN2RkOTAyMmEyMDkxMzhlNTlkNTUxMDp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyIsImNyZWF0ZV91c2VyX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2xvZ2luLyJ9', '2020-05-15 00:45:25.125110'),
('486ea5ctgh48kucodx6sktqbv8kvs04w', 'MmJiM2FkMzMyOWRkODYyNTE3MzI1MzIwYzU0MTg2NmQ4MGExZTUzMDp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2JlY29tZUNvbnRyYWN0b3IvIn0=', '2020-05-13 22:54:59.706498'),
('4vot1skgbhaqgivdhlao4h8njf7tkwcb', 'ODY4YzY2NDc4OGUwYTdjYzk5OTNiNGIzYzAyMDQ0NzY1MWE0ODA0Njp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2xvZ2luLyIsImFkbWluX2lkIjoxfQ==', '2020-05-15 23:13:22.814197'),
('56h995bt7mx33twpwxvp35rtsugadiaz', 'OWMyOTE0ZDZkODIzNGViZmZkYzFlNGYyZGIyNGQ0NDYzNTk2YjZiODp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyJ9', '2020-05-16 21:18:06.696485'),
('8z90z1dj5fpa46pf28k5stpchimeskzn', 'OWMyOTE0ZDZkODIzNGViZmZkYzFlNGYyZGIyNGQ0NDYzNTk2YjZiODp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyJ9', '2020-05-13 19:54:05.945774'),
('c99os6n47cpsh3phy0s7u51kc504ld4f', 'OWMyOTE0ZDZkODIzNGViZmZkYzFlNGYyZGIyNGQ0NDYzNTk2YjZiODp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyJ9', '2020-05-13 21:11:09.456924'),
('ca7l5hoqd5klt7ydmtatza2gufjxmzto', 'NmRmZjdlNjllMWE4YTI1ZTgzMGM1MWY5ZmFmMGIxNmYyZjVhMzdmNzp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2JlY29tZUNvbnRyYWN0b3IvIiwiY29udHJhY3Rvcl9pZCI6MX0=', '2020-05-17 08:21:37.669622'),
('dykzodpq49710zgo8xr0b21olplwxzsi', 'NTI1YmU3OGY2ZTMyYjRjYzQyYmI1ZWRkNTZhNjk3ZDY4YzI4MWQ0MTp7ImNyZWF0ZV91c2VyX2Zyb20iOiIvIiwibG9naW5fZnJvbSI6Imh0dHA6Ly9lYzItMTgtMjE4LTQxLTE0LnVzLWVhc3QtMi5jb21wdXRlLmFtYXpvbmF3cy5jb20vIiwidXNlcl9pZCI6Mn0=', '2020-05-15 22:41:39.615942'),
('eobfi6z44q7ulo3vr4zkwvx2zrwt2epg', 'N2ZkYjhhZDYwZWY3N2MwN2Q0YzVlNzRlZjE3YWI3MDdhOGU0MjM2NTp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyIsImNvbnRyYWN0b3JfaWQiOjF9', '2020-05-17 08:20:39.205186'),
('eu0m50yd9q00xcvhr3txd40f0jdzp84a', 'NTU4ZWViNmE4ZmI1MTQzYmJiNTFjMTM2NGRhNTdmYjgwODlkODZjMzp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyIsImFkbWluX2lkIjoxfQ==', '2020-05-16 00:31:24.070347'),
('gpw7elqxxlvc9qnagrnskm1e4gly2bnv', 'NDRjYWQ4YTJlMTVlYzczYjY5YzhjMjE0Mzg4NWY1OWIxMTc1Mzg5YTp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyIsImNyZWF0ZV91c2VyX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2NyZWF0ZV9hY2NvdW50LyIsInVzZXJfaWQiOjJ9', '2020-05-15 04:51:02.883586'),
('ikgnqavyfjkcry6q3h9t1u5avehxajv9', 'N2ZkYjhhZDYwZWY3N2MwN2Q0YzVlNzRlZjE3YWI3MDdhOGU0MjM2NTp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyIsImNvbnRyYWN0b3JfaWQiOjF9', '2020-05-16 21:29:41.634505'),
('kia3ywn8mxwjtmpztl4uhuxpu76rqwn7', 'OWMyOTE0ZDZkODIzNGViZmZkYzFlNGYyZGIyNGQ0NDYzNTk2YjZiODp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyJ9', '2020-05-14 03:01:30.290354'),
('mn72jdtuz3dlubga7vfjfzdrdz21t8jr', 'OWMyOTE0ZDZkODIzNGViZmZkYzFlNGYyZGIyNGQ0NDYzNTk2YjZiODp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyJ9', '2020-05-14 03:02:51.439411'),
('p6y1a1qpg5djvu10oxmmo1jmk146qm7p', 'ODY4YzY2NDc4OGUwYTdjYzk5OTNiNGIzYzAyMDQ0NzY1MWE0ODA0Njp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2xvZ2luLyIsImFkbWluX2lkIjoxfQ==', '2020-05-15 23:48:06.147180'),
('p7bkipckh7mran7zqt6zizidvgblabd5', 'OTFjYjZhMmY5NDg0MmRhOTJiZDZlNGUwNDgwN2MwOTk5YmVhN2E4OTp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2Jvb2tpbmcvYm9va2luZ19pbmZvcm1hdGlvbi81In0=', '2020-05-16 22:17:46.423489'),
('ru2pvud7mjygrg7sdasgwo0cc78m6c65', 'ODY4YzY2NDc4OGUwYTdjYzk5OTNiNGIzYzAyMDQ0NzY1MWE0ODA0Njp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2xvZ2luLyIsImFkbWluX2lkIjoxfQ==', '2020-05-17 22:31:17.238356'),
('s99j5cnvzmd2xez0715rnmbjl5ztftgf', 'ODI5MTk0MzIzOWU3N2ZiYjAwMmViN2Q5N2VkYTFjYjE3ZGM2ZDdhZTp7ImNvbnRyYWN0b3JfaWQiOjF9', '2020-05-16 05:37:45.209877'),
('tbdwarf3fy512cwfgle00zyhd22cu8y0', 'ODY4YzY2NDc4OGUwYTdjYzk5OTNiNGIzYzAyMDQ0NzY1MWE0ODA0Njp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2xvZ2luLyIsImFkbWluX2lkIjoxfQ==', '2020-05-15 19:54:39.006934'),
('tsm5vcfbpezc4otcanxdt8rn7c6gkot4', 'MzM1ZTAwYTVkNjJiZDZkYjUzNWU0OGIyY2ZjMGFlNjVmYWFkNzM2MDp7InVzZXJfaWQiOjF9', '2020-05-13 15:46:24.467224'),
('u3wtjwn0ja92sxcaudj3vbpdnnjyvdnx', 'OTUxOTQxNjU4ZmE3YWEwZjIwZjc4YmYxM2Y1NzU3YzE3OWU2OGZlNzp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2Jvb2tpbmcvYm9va2luZ19pbmZvcm1hdGlvbi8xIiwidXNlcl9pZCI6MX0=', '2020-05-17 18:01:32.713224'),
('unkmy10d27d6cmjcdlu1vq0eq98734z8', 'OWMyOTE0ZDZkODIzNGViZmZkYzFlNGYyZGIyNGQ0NDYzNTk2YjZiODp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyJ9', '2020-05-14 02:08:30.401531'),
('w41j7dzll3dqmezbykkrt3r4x6bnxqfy', 'OWMyOTE0ZDZkODIzNGViZmZkYzFlNGYyZGIyNGQ0NDYzNTk2YjZiODp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyJ9', '2020-05-16 05:45:21.924696'),
('yjd2eh6k6flybys20c4ubk3wow2091lz', 'MzM1ZTAwYTVkNjJiZDZkYjUzNWU0OGIyY2ZjMGFlNjVmYWFkNzM2MDp7InVzZXJfaWQiOjF9', '2020-05-13 02:18:35.044696'),
('yw8g6iuo9620qu1hixw65f8b23biuygq', 'N2ZkYjhhZDYwZWY3N2MwN2Q0YzVlNzRlZjE3YWI3MDdhOGU0MjM2NTp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tLyIsImNvbnRyYWN0b3JfaWQiOjF9', '2020-05-16 04:57:33.172611'),
('zo09uio7cyq68q1pkn0v6m5yrj5o7m07', 'MWYyNTk1ZDBjODQwMzUzMmU5N2UxMzEyNWVhODhlNGRkMWVjN2ExZDp7ImxvZ2luX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL3NlcnZpY2VzLyIsImNyZWF0ZV91c2VyX2Zyb20iOiJodHRwOi8vZWMyLTE4LTIxOC00MS0xNC51cy1lYXN0LTIuY29tcHV0ZS5hbWF6b25hd3MuY29tL2NyZWF0ZV9hY2NvdW50LyIsInVzZXJfaWQiOjF9', '2020-05-15 00:55:41.796445');

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
  `adminID` int(11) DEFAULT NULL,
  `dateApproved` date DEFAULT NULL,
  `chargeService` decimal(10,2) NOT NULL,
  `yearsExperience` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `serviceApplications`
--

INSERT INTO `serviceApplications` (`serviceAppID`, `contractorID`, `serviceID`, `dateApp`, `adminID`, `dateApproved`, `chargeService`, `yearsExperience`) VALUES
(1, 1, 8, '2020-05-03', 1, '2020-05-03', '7.25', 2),
(2, 2, 8, '2020-05-03', 1, '2020-05-03', '8.36', 2),
(3, 2, 6, '2020-05-03', NULL, NULL, '10.25', 5);

-- --------------------------------------------------------

--
-- Table structure for table `serviceCategories`
--

CREATE TABLE `serviceCategories` (
  `categoryServiceID` int(11) NOT NULL,
  `sub_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `serviceCategories`
--

INSERT INTO `serviceCategories` (`categoryServiceID`, `sub_name`) VALUES
(1, 'Cleaning'),
(2, 'Assembly'),
(3, 'TV & Electronics');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `serviceID` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `categoryServiceID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`serviceID`, `title`, `categoryServiceID`) VALUES
(1, 'Office Cleaning', 1),
(2, 'Room Cleaning', 1),
(3, 'Kitchen Cleaning', 1),
(4, 'TV Wall Mounting Installation', 3),
(5, 'Home Theater AV Setup', 3),
(6, 'Smart Lock Installation', 3),
(7, 'Exercise Equipment Assembly', 2),
(8, 'Outdoor Furniture Assembly', 2);

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
  `phone` varchar(15) NOT NULL,
  `address` varchar(150) NOT NULL,
  `aptNum` varchar(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zipCode` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userID`, `firstName`, `lastName`, `email`, `password`, `dob`, `phone`, `address`, `aptNum`, `city`, `state`, `zipCode`) VALUES
(1, 'Yessenia', 'Rodriguez', 'yessenia.yess98@hotmail.com', 'hello', '1998-07-13', '9564661730', '554 Rey Salomon St.', '', 'Brownsville', 'TX', 78521),
(2, 'Clark', 'Kent', 'clark.kent@dailyplanet.com', 'superman', '1938-04-18', '9563814675', '517 Market St', '3D', 'Metropolis', 'IL', 62960);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administrators`
--
ALTER TABLE `administrators`
  ADD PRIMARY KEY (`adminID`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

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
  ADD UNIQUE KEY `ssn` (`ssn`),
  ADD UNIQUE KEY `contractors_email_93d0bb8e_uniq` (`email`);

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
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

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
  ADD PRIMARY KEY (`categoryServiceID`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`serviceID`),
  ADD KEY `subServiceConstraint` (`categoryServiceID`);

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
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `contractorApplications`
--
ALTER TABLE `contractorApplications`
  ADD CONSTRAINT `adminConstraint3` FOREIGN KEY (`adminID`) REFERENCES `administrators` (`adminID`);

--
-- Constraints for table `contractors`
--
ALTER TABLE `contractors`
  ADD CONSTRAINT `contractors_contractorID_9b4db693_fk_contracto` FOREIGN KEY (`contractorID`) REFERENCES `contractorApplications` (`contractorID`);

--
-- Constraints for table `contractorsServiceRecords`
--
ALTER TABLE `contractorsServiceRecords`
  ADD CONSTRAINT `contractorConstraint3` FOREIGN KEY (`contractorID`) REFERENCES `contractors` (`contractorID`) ON DELETE CASCADE,
  ADD CONSTRAINT `serviceConstraint` FOREIGN KEY (`serviceID`) REFERENCES `services` (`serviceID`) ON DELETE CASCADE;

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
  ADD CONSTRAINT `serviceConstraint2` FOREIGN KEY (`serviceID`) REFERENCES `services` (`serviceID`) ON DELETE CASCADE,
  ADD CONSTRAINT `userConstraint4` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE CASCADE;

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `paymentInfo`
--
ALTER TABLE `paymentInfo`
  ADD CONSTRAINT `userConstraint` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE NO ACTION;

--
-- Constraints for table `rating`
--
ALTER TABLE `rating`
  ADD CONSTRAINT `rating_contractorID_6d2d3d2c_fk_contractors_contractorID` FOREIGN KEY (`contractorID`) REFERENCES `contractors` (`contractorID`),
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
  ADD CONSTRAINT `serviceConstraint3` FOREIGN KEY (`serviceID`) REFERENCES `services` (`serviceID`) ON DELETE CASCADE;

--
-- Constraints for table `services`
--
ALTER TABLE `services`
  ADD CONSTRAINT `subServiceConstraint` FOREIGN KEY (`categoryServiceID`) REFERENCES `serviceCategories` (`categoryServiceID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
