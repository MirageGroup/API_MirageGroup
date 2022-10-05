-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 05-Out-2022 às 03:24
-- Versão do servidor: 10.4.24-MariaDB
-- versão do PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `api`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `laboratorio402`
--
DROP DATABASE IF EXISTS api;

CREATE DATABASE api;

USE api;

CREATE TABLE laboratorio402 (
  pc_id varchar(9) NOT NULL,
  pc_status varchar(20) NOT NULL,
  pc_problema varchar(20) DEFAULT NULL,
  pc_descricao varchar(50) NOT NULL,
  posx int(1) NOT NULL,
  posy int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `laboratorio402`
--

INSERT INTO laboratorio402 (pc_id, pc_status, pc_problema, pc_descricao, posx, posy) VALUES
('Professor', 'Funcionando', NULL, 'O computador está funcionando corretamente', 1, 1),
('001', 'Funcionando', NULL, 'O computador está funcionando corretamente', 2, 2),
('002', 'Funcionando', NULL, 'O computador está funcionando corretamente', 3, 2),
('003', 'Funcionando', NULL, 'O computador está funcionando corretamente', 4, 2),
('004', 'Funcionando', NULL, 'O computador está funcionando corretamente', 5, 2),
('005', 'Funcionando', NULL, 'O computador está funcionando corretamente', 6, 2),
('006', 'Funcionando', NULL, 'O computador está funcionando corretamente', 7, 2),
('007', 'Funcionando', NULL, 'O computador está funcionando corretamente', 8, 2),
('008', 'Funcionando', NULL, 'O computador está funcionando corretamente', 9, 2),
('009', 'Funcionando', NULL, 'O computador está funcionando corretamente', 2, 3),
('010', 'Funcionando', NULL, 'O computador está funcionando corretamente', 3, 3),
('011', 'Funcionando', NULL, 'O computador está funcionando corretamente', 4, 3),
('012', 'Funcionando', NULL, 'O computador está funcionando corretamente', 5, 3),
('013', 'Funcionando', NULL, 'O computador está funcionando corretamente', 6, 3),
('014', 'Funcionando', NULL, 'O computador está funcionando corretamente', 7, 3),
('015', 'Funcionando', NULL, 'O computador está funcionando corretamente', 8, 3),
('016', 'Funcionando', NULL, 'O computador está funcionando corretamente', 9, 3),
('017', 'Funcionando', NULL, 'O computador está funcionando corretamente', 2, 4),
('018', 'Funcionando', NULL, 'O computador está funcionando corretamente', 3, 4),
('019', 'Funcionando', NULL, 'O computador está funcionando corretamente', 4, 4),
('020', 'Funcionando', NULL, 'O computador está funcionando corretamente', 5, 4),
('021', 'Funcionando', NULL, 'O computador está funcionando corretamente', 6, 4),
('022', 'Funcionando', NULL, 'O computador está funcionando corretamente', 7, 4),
('023', 'Funcionando', NULL, 'O computador está funcionando corretamente', 8, 4),
('024', 'Funcionando', NULL, 'O computador está funcionando corretamente', 9, 4),
('025', 'Funcionando', NULL, 'O computador está funcionando corretamente', 2, 5),
('026', 'Funcionando', NULL, 'O computador está funcionando corretamente', 3, 5),
('027', 'Funcionando', NULL, 'O computador está funcionando corretamente', 4, 5),
('028', 'Funcionando', NULL, 'O computador está funcionando corretamente', 5, 5),
('029', 'Funcionando', NULL, 'O computador está funcionando corretamente', 6, 5),
('030', 'Funcionando', NULL, 'O computador está funcionando corretamente', 7, 5),
('031', 'Funcionando', NULL, 'O computador está funcionando corretamente', 8, 5),
('032', 'Funcionando', NULL, 'O computador está funcionando corretamente', 9, 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `_laboratorio402`
--

CREATE TABLE _laboratorio402 (
  pos int(2) NOT NULL,
  com_pc tinyint(1) NOT NULL,
  pc_id varchar(10) DEFAULT NULL,
  pc_problema varchar(30) DEFAULT NULL,
  pc_descricao varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `_laboratorio402`
--

INSERT INTO _laboratorio402 (pos, com_pc, pc_id, pc_problema, pc_descricao) VALUES
(1, 1, 'Professor', NULL, 'O computador funciona corretamente'),
(2, 0, NULL, NULL, NULL),
(3, 0, NULL, NULL, NULL),
(4, 0, NULL, NULL, NULL),
(5, 0, NULL, NULL, NULL),
(6, 0, NULL, NULL, NULL),
(7, 0, NULL, NULL, NULL),
(8, 0, NULL, NULL, NULL),
(9, 0, NULL, NULL, NULL),
(10, 0, NULL, NULL, NULL),
(11, 0, NULL, NULL, NULL),
(12, 0, NULL, NULL, NULL),
(13, 1, '01', NULL, 'O computador funciona corretamente'),
(14, 1, '02', NULL, 'O computador funciona corretamente'),
(15, 1, '03', NULL, 'O computador funciona corretamente'),
(16, 1, '04', NULL, 'O computador funciona corretamente'),
(17, 0, NULL, NULL, NULL),
(18, 1, '05', NULL, 'O computador funciona corretamente'),
(19, 1, '06', NULL, 'O computador funciona corretamente'),
(20, 1, '07', NULL, 'O computador funciona corretamente'),
(21, 1, '08', NULL, 'O computador funciona corretamente'),
(22, 0, NULL, NULL, NULL),
(23, 0, NULL, NULL, NULL),
(24, 1, '09', NULL, 'O computador funciona corretamente'),
(25, 1, '10', NULL, 'O computador funciona corretamente'),
(26, 1, '11', NULL, 'O computador funciona corretamente'),
(27, 1, '12', NULL, 'O computador funciona corretamente'),
(28, 0, NULL, NULL, NULL),
(29, 1, '13', NULL, 'O computador funciona corretamente'),
(30, 1, '14', NULL, 'O computador funciona corretamente'),
(31, 1, '15', NULL, 'O computador funciona corretamente'),
(32, 1, '16', NULL, 'O computador funciona corretamente'),
(33, 0, NULL, NULL, NULL),
(34, 0, NULL, NULL, NULL),
(35, 1, '17', NULL, 'O computador funciona corretamente'),
(36, 1, '18', NULL, 'O computador funciona corretamente'),
(37, 1, '19', NULL, 'O computador funciona corretamente'),
(38, 1, '20', NULL, 'O computador funciona corretamente'),
(39, 0, NULL, NULL, NULL),
(40, 1, '21', NULL, 'O computador funciona corretamente'),
(41, 1, '22', NULL, 'O computador funciona corretamente'),
(42, 1, '23', NULL, 'O computador funciona corretamente'),
(43, 1, '24', NULL, 'O computador funciona corretamente'),
(44, 0, NULL, NULL, NULL),
(45, 0, NULL, NULL, NULL),
(46, 1, '25', NULL, 'O computador funciona corretamente'),
(47, 1, '26', NULL, 'O computador funciona corretamente'),
(48, 1, '27', NULL, 'O computador funciona corretamente'),
(49, 1, '28', NULL, 'O computador funciona corretamente'),
(50, 0, NULL, NULL, NULL),
(51, 1, '29', NULL, 'O computador funciona corretamente'),
(52, 1, '30', NULL, 'O computador funciona corretamente'),
(53, 1, '31', NULL, 'O computador funciona corretamente'),
(54, 1, '32', NULL, 'O computador funciona corretamente'),
(55, 0, NULL, NULL, NULL),
(56, 0, NULL, NULL, NULL),
(57, 0, NULL, NULL, NULL),
(58, 0, NULL, NULL, NULL),
(59, 0, NULL, NULL, NULL),
(60, 0, NULL, NULL, NULL),
(61, 0, NULL, NULL, NULL),
(62, 0, NULL, NULL, NULL),
(63, 0, NULL, NULL, NULL),
(64, 0, NULL, NULL, NULL),
(65, 0, NULL, NULL, NULL),
(66, 0, NULL, NULL, NULL),
(67, 0, NULL, NULL, NULL),
(68, 0, NULL, NULL, NULL),
(69, 0, NULL, NULL, NULL),
(70, 0, NULL, NULL, NULL),
(71, 0, NULL, NULL, NULL),
(72, 0, NULL, NULL, NULL),
(73, 0, NULL, NULL, NULL),
(74, 0, NULL, NULL, NULL),
(75, 0, NULL, NULL, NULL),
(76, 0, NULL, NULL, NULL),
(77, 0, NULL, NULL, NULL),
(78, 0, NULL, NULL, NULL),
(79, 0, NULL, NULL, NULL),
(80, 0, NULL, NULL, NULL),
(81, 0, NULL, NULL, NULL),
(82, 0, NULL, NULL, NULL),
(83, 0, NULL, NULL, NULL),
(84, 0, NULL, NULL, NULL),
(85, 0, NULL, NULL, NULL),
(86, 0, NULL, NULL, NULL),
(87, 0, NULL, NULL, NULL),
(88, 0, NULL, NULL, NULL),
(89, 0, NULL, NULL, NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

SELECT * FROM _laboratorio402;