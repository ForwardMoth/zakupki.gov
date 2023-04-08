CREATE TABLE IF NOT EXISTS Customers
(
    id serial,
    fullname character varying(2000) DEFAULT 'Отсутствует' NOT NULL,
    shortname character varying(200) DEFAULT 'Отсутствует' NOT NULL,
    inn numeric(12) NOT NULL,
    kpp numeric(9) NOT NULL,
    ogrn numeric(13) NOT NULL,
    legal_address character varying(2000),
    postal_address character varying(2000),
    bitmask character varying(7) NOT NULL,
    PRIMARY KEY (id), 
    UNIQUE(fullname, inn, ogrn) 
);

CREATE TABLE IF NOT EXISTS Placers
(
    id serial,
    fullname character varying(2000) DEFAULT 'Отсутствует' NOT NULL,
    shortname character varying(200) DEFAULT 'Отсутствует' NOT NULL,
    inn numeric(12) NOT NULL,
    kpp numeric(9) NOT NULL,
    ogrn numeric(13) NOT NULL,
    legal_address character varying(2000),
    postal_address character varying(2000),
    bitmask character varying(7) NOT NULL,
    PRIMARY KEY (id), 
    UNIQUE(fullname, inn, ogrn) 
);


CREATE TABLE IF NOT EXISTS maindata
(
    id serial,
    customer_id integer NOT NULL,
    placer_id integer NOT NULL,
    region character varying(64) NOT NULL,
    notice_number numeric(11) DEFAULT 0 NOT NULL,
    name character varying(2000) DEFAULT 'Без названия',
    guid character varying(36) DEFAULT '-' NOT NULL,
    create_datetime timestamp DEFAULT '2001-01-01 00:00:00',
    publication_datetime timestamp DEFAULT '2001-01-01 00:00:00',
    modification_datetime timestamp DEFAULT '2001-01-01 00:00:00',
    version numeric(3) DEFAULT 0,
    status char DEFAULT 'U',
    bitmask character varying(8) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS lots
(
    id serial,
    maindata_id integer NOT NULL,
    guid character varying(36) DEFAULT '-' NOT NULL,
    subject character varying(2000) DEFAULT 'Отсутствует',
    order_number numeric(8) DEFAULT 0,
    initital_price numeric(17, 2) DEFAULT -0.01,
    currency character varying(3) DEFAULT '-',
    bitmask character varying(5) NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS maindata
    ADD FOREIGN KEY (customer_id)
    REFERENCES Customers (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS maindata
    ADD FOREIGN KEY (placer_id)
    REFERENCES Placers (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS lots
    ADD FOREIGN KEY (maindata_id)
    REFERENCES maindata (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


