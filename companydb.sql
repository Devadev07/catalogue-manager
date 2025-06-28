-- STEP 1: Create and use the database
CREATE DATABASE IF NOT EXISTS companydb;
USE companydb;
-- DROP DATABASE IF EXISTS companydb;

-- STEP 2: Create 'catalogue' table
CREATE TABLE IF NOT EXISTS catalogue (
    catalogue_id INT PRIMARY KEY AUTO_INCREMENT,
    catalogue_name VARCHAR(30),
    start_date DATE,
    end_date DATE,
    is_deleted TINYINT(1) DEFAULT 0
) ENGINE=InnoDB;

-- STEP 3: Create 'category' table
CREATE TABLE IF NOT EXISTS category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(80),
    is_deleted TINYINT(1) DEFAULT 0
) ENGINE=InnoDB;

-- STEP 4: catalog_category_mapping
CREATE TABLE IF NOT EXISTS catalog_category_mapping (
    catalogue_id INT,
    category_id INT,
    FOREIGN KEY (catalogue_id) REFERENCES catalogue(catalogue_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- STEP 5: category_category_mapping (subcategory links)
CREATE TABLE IF NOT EXISTS category_category_mapping (
    category_id INT,
    subcategory_id INT,
    FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE CASCADE,
    FOREIGN KEY (subcategory_id) REFERENCES category(category_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- STEP 6: Create 'product' table
CREATE TABLE IF NOT EXISTS product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(50),
    product_quantity INT,
    is_deleted TINYINT(1) DEFAULT 0
) ENGINE=InnoDB;

-- STEP 7: product_category_mapping
CREATE TABLE IF NOT EXISTS product_category_mapping (
    product_id INT,
    category_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- STEP 8: sku table
CREATE TABLE IF NOT EXISTS sku (
    sku_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    sku_name VARCHAR(100),
    price DECIMAL(10,2),
    is_deleted TINYINT(1) DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- STEP 9: sku_attribute table
CREATE TABLE IF NOT EXISTS sku_attribute (
    sku_id INT,
    attribute_name VARCHAR(50),
    attribute_value VARCHAR(50),
    sku_name VARCHAR(100),
    FOREIGN KEY (sku_id) REFERENCES sku(sku_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- STEP 10: administrator table
CREATE TABLE IF NOT EXISTS administrator (
    administrator_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    username VARCHAR(50),
    password VARCHAR(100)
) ENGINE=InnoDB;

-- STEP 11: Sample data for catalogue
INSERT INTO catalogue (catalogue_name, start_date, end_date, is_deleted) VALUES
('Diwali Dhamaka', '2025-10-20', '2025-11-10', 0),
('Republic Day Sale', '2025-01-20', '2025-01-27', 0),
('Independence Day Mega Sale', '2025-08-10', '2025-08-15', 0),
('Onam Specials', '2025-08-25', '2025-09-10', 0),
('Eid Celebration Offers', '2025-04-01', '2025-04-15', 0),
('Navratri Fashion Fest', '2025-10-01', '2025-10-10', 0),
('Pongal & Sankranti Deals', '2025-01-12', '2025-01-17', 0),
('Raksha Bandhan Gifting Week', '2025-08-12', '2025-08-18', 0),
('Clearance Sale', '2025-08-01', '2025-08-15', 0),
('NewOld BigBigSale', '2025-06-01', '2025-06-30', 0);

-- STEP 12: Category values
INSERT INTO category (category_name, is_deleted) VALUES
('Electronics', 0),
('Stationery', 0),
('Clothing', 0),
('Kitchenware', 0),
('Books', 0);

-- STEP 13: Catalogue-Category mapping
INSERT INTO catalog_category_mapping (catalogue_id, category_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 2),
(4, 4);

-- STEP 14: Category hierarchy mapping
INSERT INTO category_category_mapping (category_id, subcategory_id) VALUES
(1, 5),
(2, 4),
(3, 1),
(4, 2),
(5, 3);

-- STEP 15: Product entries
INSERT INTO product (product_name, product_quantity, is_deleted) VALUES
('Bluetooth Speaker', 25, 0),
('Formal Shoes', 40, 0),
('Electric Kettle', 30, 0),
('Kurti Set', 60, 0),
('Wireless Mouse', 45, 0),
('Cricket Bat', 20, 0),
('School Backpack', 70, 0),
('Air Purifier', 10, 0),
('Smartwatch', 35, 0),
('Wall Clock', 50, 0);

-- STEP 16: Product-category mapping
INSERT INTO product_category_mapping (product_id, category_id) VALUES
(1, 1),
(2, 3),
(3, 4),
(4, 3),
(5, 1),
(6, 5),
(7, 2),
(8, 1),
(9, 1),
(10, 4);

-- STEP 17: SKU entries
INSERT INTO sku (product_id, sku_name, price, is_deleted) VALUES
(1, 'Bluetooth Speaker 10W', 1499.00, 0),
(2, 'Formal Shoes Size 9', 1999.00, 0),
(3, 'Electric Kettle 1.5L', 1299.00, 0),
(4, 'Kurti Set M Size', 999.00, 0),
(5, 'Wireless Mouse Silent', 499.00, 0);

-- STEP 18: SKU attributes
INSERT INTO sku_attribute (sku_id, attribute_name, attribute_value, sku_name) VALUES
(1, 'Output Power', '10W', 'Bluetooth Speaker 10W'),
(1, 'Connectivity', 'Bluetooth 5.0', 'Bluetooth Speaker 10W'),

(2, 'Size', '9', 'Formal Shoes Size 9'),
(2, 'Material', 'Leather', 'Formal Shoes Size 9'),

(3, 'Capacity', '1.5L', 'Electric Kettle 1.5L'),
(3, 'Wattage', '1500W', 'Electric Kettle 1.5L'),

(4, 'Size', 'M', 'Kurti Set M Size'),
(4, 'Fabric', 'Cotton', 'Kurti Set M Size'),

(5, 'Type', 'Silent Click', 'Wireless Mouse Silent'),
(5, 'Battery Life', '12 months', 'Wireless Mouse Silent');

-- STEP 19: Administrator users
INSERT INTO administrator (name, username, password) VALUES
('Devadev K A', 'devadev', 'dev123'),
('Sneha S', 'sneha_s', 'sneha@123'),
('Sona', 'sona_s', 'sona123'),
('Raju R', 'raju_r', 'raju123'),
('Tom Jerry', 'tom_j', 'jerry123');

-- STEP 20: Optional - cleanup duplicates (only run if needed)
SET SQL_SAFE_UPDATES = 0;

DELETE FROM catalogue
WHERE catalogue_id NOT IN (
    SELECT * FROM (
        SELECT MIN(catalogue_id)
        FROM catalogue
        GROUP BY catalogue_name, start_date, end_date
    ) AS temp
);

SET SQL_SAFE_UPDATES = 1;

-- STEP 21: View active catalogues
SELECT * FROM catalogue WHERE is_deleted = 0 ORDER BY catalogue_id DESC;
