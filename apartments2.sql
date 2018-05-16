USE apartments;

DROP TABLE IF EXISTS apts2;
CREATE TABLE apts2
(
  id             int unsigned NOT NULL auto_increment, # Unique ID for the record
  unit           varchar(255) NOT NULL,                # Apartment unit Name
  price        varchar(255) NOT NULL,                # Special
  name           varchar(255) NOT NULL,                # Apartment Complex Name
  moveIn        varchar(255) NOT NULL,                # Apartment address
  bedrooms       varchar(255) NOT NULL,                # Num bedrooms
  bath           varchar(255) NOT NULL,                # Num baths
  sqft           varchar(255) NOT NULL,                # Sqft of Apt

  PRIMARY KEY     (id)
);
