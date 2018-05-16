USE apartments;

DROP TABLE IF EXISTS apts;
CREATE TABLE apts
(
  id             int unsigned NOT NULL auto_increment, # Unique ID for the record
  name           varchar(255) NOT NULL,                # Apartment Complex Name
  address        varchar(255) NOT NULL,                # Apartment address
  bedrooms       varchar(255) NOT NULL,                # Num bedrooms
  bath           varchar(255) NOT NULL,                # Num baths
  sqft           varchar(255) NOT NULL,                # Sqft of Apt

  PRIMARY KEY     (id)
);
