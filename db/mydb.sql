-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 14, 2019 at 12:15 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `name`, `address`) VALUES
(1, 'John', 'Highway 21');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_name` varchar(15) NOT NULL,
  `product_id` int(5) NOT NULL,
  `description` varchar(90) NOT NULL,
  `imglink` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_name`, `product_id`, `description`, `imglink`) VALUES
('Iphone', 5, 'THis Is Iphone 11', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR88t1fMR2bpSyAzmYI-yx2t-NLrU3TuyUS_n0hvdrkVV3Cgze9'),
('Macbook Pro', 6, 'This is a macbook Pro', 'https://cnet4.cbsistatic.com/img/F9suzz0c1Q7ghhQoienu2TajkIw=/868x488/2016/10/27/6cd01ecb-40cd-4615-b5f5-82993fbf9419/apple-macbook-pro-13-inch-2016-1765-026.jpg'),
('MiBand', 7, 'This Is  a mi band', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTsJlhB3eg2QzskfNa_DLGWzkuJqVWYSN_vFb5r70sCpOkFkFo'),
('galaxy s10', 9, 'This Is galaxy s10', 'https://images-na.ssl-images-amazon.com/images/I/619h1rSUcKL._SX569_.jpg'),
('Cannon 4000D', 10, 'This Is Canon 4000D cam', 'https://images-na.ssl-images-amazon.com/images/I/41RV3IWWADL._SX425_.jpg'),
('Wireless Keybor', 11, 'This is a Wireless Keybord', 'https://target.scene7.com/is/image/Target/GUEST_25cb8b97-a9ce-4dad-a0b7-1d7142461fc1?wid=488&hei=488&fmt=pjpeg'),
('Apple Airpods', 12, 'This is Airpods', 'https://images-na.ssl-images-amazon.com/images/I/41qIPi7taiL._SX385_.jpg'),
('VR Box', 13, 'Enjoy With This Amazing VR Box', 'https://rukminim1.flixcart.com/image/832/832/j5lchow0/smart-glass/u/k/4/12-nexus-original-imaevs9sg9egpjzh.jpeg?q=70');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `role` varchar(10) DEFAULT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `address`, `role`, `password`) VALUES
(19, 'admin', 'admin@admin.com', 'admincity', 'admin', 'admin'),
(21, 'Khaled Ahmed', 'khaled.basha144@gmail.com', 'Cairo', 'user', '123456789'),
(22, 'Khaled Abd ElFatah', 'khaledabdelfatah200@gmail.com', 'Mansoura', 'user', '123456789'),
(23, 'user', 'user@user.com', 'User City', 'user', '123456789');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
