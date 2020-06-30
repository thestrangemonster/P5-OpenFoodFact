
"""
CREATE DATABASE p5_openfoodfacts;
GRANT ALL PRIVILEGES ON DATABASE p5_openfoodfacts TO tom;
\connect p5_openfoodfacts
"""
DROP TABLE IF EXISTS favorites; 
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;



CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(40) NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    nutri_score VARCHAR(40) NOT NULL,
    product_name  VARCHAR(40) NOT NULL,
    stores_tags  VARCHAR(40) NOT NULL,
    url_  VARCHAR(200) NOT NULL
);


CREATE TABLE link
(
    category_id smallint NOT NULL,
    product_id smallint NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    UNIQUE (category_id, product_id)
);

CREATE TABLE favorites (
    id SERIAL PRIMARY KEY,
    product_name  VARCHAR(40) NOT NULL
);
