INSERT INTO RENTALS_PID_HID_S_HZ_HS
SELECT PID, HID, S, HZ, HS
FROM RENTALS;

INSERT INTO RENTALS_PID_PN
SELECT PID, PN
FROM RENTALS;

INSERT INTO RENTALS_HID_HS
SELECT PID, PN
FROM RENTALS;

INSERT INTO RENTALS_HS_HC
SELECT HS, HC
FROM RENTALS;

INSERT INTO COFFEES_CM_CN
SELECT CM, CN
FROM COFFEES;

INSERT INTO COFFEES_DID_DS_DN
SELECT DID, DS, DN
FROM COFFEES;

INSERT INTO COFFEES_DID_CID_HID
SELECT DID, CID, HID
FROM COFFEES;

INSERT INTO PROJECTS_MID_MN
SELECT MID, MN
FROM PROJECTS;

INSERT INTO PROJECTS_SID_SN
SELECT SID, SN
FROM PROJECTS;

INSERT INTO PROJECTS_PID_PN
SELECT PID, PN
FROM PROJECTS;

INSERT INTO PROJECTS_ID_MID
SELECT ID, MID
FROM PROJECTS;

INSERT INTO CUSTOMERS_CID_CN_CS_CNr_CC_EID
SELECT CID, CN, CS, CNr, CC, EID
FROM CUSTOMERS;

INSERT INTO CUSTOMERS_CC_CZ
SELECT CC, CZ
FROM CUSTOMERS;