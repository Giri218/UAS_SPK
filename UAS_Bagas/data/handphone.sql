-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Inang: 127.0.0.1
-- Waktu pembuatan: 30 Okt 2023 pada 07.03
-- Versi Server: 5.5.27
-- Versi PHP: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Basis data: `spk_wp`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `handphone`
--

CREATE TABLE IF NOT EXISTS `handphone` (
  `No.` int(50) NOT NULL AUTO_INCREMENT,
  `Merk` varchar(255) NOT NULL,
  `Harga` varchar(255) NOT NULL,
  `Kamera` varchar(255) NOT NULL,
  `Memori Internal` varchar(255) NOT NULL,
  `RAM` varchar(255) NOT NULL,
  `Baterai` varchar(255) NOT NULL,
  PRIMARY KEY (`No.`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=11 ;

--
-- Dumping data untuk tabel `handphone`
--

INSERT INTO `handphone` (`No.`, `Merk`, `Harga`, `Kamera`, `Memori Internal`, `RAM`, `Baterai`) VALUES
(1, 'Xiaomi 13T', '6499000', '50', '256', '12', '5000'),
(2, 'Vivo Y17s', '1799000', '50', '128', '6', '5000'),
(3, 'Vivo V29 5G', '6449000', '50', '256', '8', '4600'),
(4, 'Realme 11', '3599000', '108', '256', '8', '5000'),
(5, 'Infinix GT 10 Pro', '3330000', '108', '256', '8', '5000'),
(6, 'Realme C51', '1420000', '50', '64', '4', '5000'),
(7, 'Redmi 12', '1899000', '50', '128', '8', '5000'),
(8, 'Vivo Y27 4G', '1975000', '50', '128', '6', '5000'),
(9, 'Vivo Y27 5G', '2439000', '50', '128', '6', '5000'),
(10, 'Samsung Galaxy Z Flip 5', '14299000', '12', '256', '8', '3700');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
