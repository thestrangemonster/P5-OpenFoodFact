
"""
CREATE DATABASE p5_openfoodfacts;
GRANT ALL PRIVILEGES ON DATABASE p5_openfoodfacts TO tom;
\connect p5_openfoodfacts
"""

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(40) NOT NULL
);
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    category_id  smallint NOT NULL,
    nutri_score VARCHAR(40) NOT NULL,
    product_name  VARCHAR(40) NOT NULL,
    stores_tags  VARCHAR(40) NOT NULL,
    url_  VARCHAR(200) NOT NULL
);
CREATE TABLE favorites (
    id SERIAL PRIMARY KEY,
    favorite_id smallint NOT NULL,
    product_name  VARCHAR(40) NOT NULL
);

ALTER TABLE products ADD CONSTRAINT fk_products_category_id FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE;
ALTER TABLE favorites ADD CONSTRAINT fk_favorites_favorite_id FOREIGN KEY (favorite_id) REFERENCES products (id) ON DELETE CASCADE;