-- Rentals

DROP TABLE
  IF EXISTS RENTALS_PID_HID_S_HZ_HS;
DROP TABLE
  IF EXISTS RENTALS_PID_PN;
DROP TABLE
  IF EXISTS RENTALS_HID_HS;
DROP TABLE
  IF EXISTS RENTALS_HS_HC;

CREATE TABLE RENTALS_PID_HID_S_HZ_HS
(
  PID INTEGER           NOT NULL,
  HID INTEGER           NOT NULL,
  S   INTEGER           NOT NULL,
  HZ  CHARACTER VARYING NOT NULL,
  HS  INTEGER           NOT NULL,
  PRIMARY KEY (PID, HID)
);
CREATE TABLE RENTALS_PID_PN
(
  PID INTEGER           NOT NULL,
  PN  CHARACTER VARYING NOT NULL,
  PRIMARY KEY (PID)
);
CREATE TABLE RENTALS_HID_HS
(
  HID INTEGER NOT NULL,
  HS  INTEGER NOT NULL,
  PRIMARY KEY (HID)
);
CREATE TABLE RENTALS_HS_HC
(
  HS INTEGER           NOT NULL,
  HC CHARACTER VARYING NOT NULL,
  PRIMARY KEY (HS)
);

--Coffees

DROP TABLE
  IF EXISTS COFFEES_CID_CM_CN;
DROP TABLE
  IF EXISTS COFFEES_DID_DS_DN;
DROP TABLE
  IF EXISTS COFFEES_DID_CID_HID;

CREATE TABLE COFFEES_CID_CM_CN
(
  CID INTEGER           NOT NULL,
  CN  CHARACTER VARYING NOT NULL,
  CM  CHARACTER VARYING NOT NULL,
  PRIMARY KEY (CID)
);
CREATE TABLE COFFEES_DID_DS_DN
(
  DID INTEGER           NOT NULL,
  DN  CHARACTER VARYING NOT NULL,
  DS  CHARACTER VARYING NOT NULL,
  PRIMARY KEY (DID)
);
CREATE TABLE COFFEES_DID_CID_HID
(
  DID INTEGER NOT NULL,
  HID INTEGER NOT NULL,
  CID INTEGER NOT NULL,
  PRIMARY KEY (DID, CID)
);

-- PROJECTS

DROP TABLE
  IF EXISTS PROJECTS_MID_MN;
DROP TABLE
  IF EXISTS PROJECTS_SID_SN;
DROP TABLE
  IF EXISTS PROJECTS_PID_PN;
DROP TABLE
  IF EXISTS PROJECTS_ID_MID;

CREATE TABLE PROJECTS_MID_MN
(
  MID INTEGER           NOT NULL,
  MN  CHARACTER VARYING NOT NULL,
  PRIMARY KEY (MID)
);

CREATE TABLE PROJECTS_SID_SN
(
  SID INTEGER NOT NULL,
  PRIMARY KEY (SID)
);

CREATE TABLE PROJECTS_PID_PN
(
  PID INTEGER           NOT NULL,
  PN  CHARACTER VARYING NOT NULL,
  PRIMARY KEY (PID)
);

CREATE TABLE PROJECTS_ID_MID
(
  ID  INTEGER NOT NULL,
  MID INTEGER NOT NULL,
  PRIMARY KEY (ID)
);

-- Customers

DROP TABLE
  IF EXISTS CUSTOMERS_CID_CN_CS_CNr_CC_EID;
DROP TABLE
  IF EXISTS CUSTOMERS_CC_CZ;

CREATE TABLE CUSTOMERS_CID_CN_CS_CNr_CC_EID
(
  CID INTEGER           NOT NULL,
  CN  CHARACTER VARYING NOT NULL,
  CS  CHARACTER VARYING NOT NULL,
  CNr INTEGER           NOT NULL,
  CC  INTEGER           NOT NULL,
  EID INTEGER           NOT NULL,
  PRIMARY KEY (CID)
);

CREATE TABLE CUSTOMERS_CC_CZ
(
  CC INTEGER           NOT NULL,
  CZ CHARACTER VARYING NOT NULL,
  PRIMARY KEY (CC)
);