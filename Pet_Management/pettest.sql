CREATE database Pettest;
USE Pettest;

CREATE TABLE PET(
PET_ID INT PRIMARY KEY,
NAME VARCHAR(20),
TYPE VARCHAR(20),
BREED VARCHAR(20),
AGE INT,
GENDER VARCHAR(1),
STATUS VARCHAR(20));

CREATE TABLE MEDICAL_RECORDS(
PET_ID INT,
VACCINATION_ID INT,
VACCINATION_STATUS VARCHAR(20),
NEXT_DUE_DATE DATE,
DISEASE_HISTORY VARCHAR(20),
CURRENT_DISEASES VARCHAR(20),
PRIMARY KEY(PET_ID,VACCINATION_ID),
FOREIGN KEY (PET_ID) REFERENCES PET(PET_ID) ON DELETE CASCADE);

CREATE TABLE ADOPTER(
ADOPTER_ID INT,
PET_ID INT PRIMARY KEY,
ADOPTER_NAME VARCHAR(20),
AMOUNT INT,
CONTACT BIGINT(10),
FOREIGN KEY (PET_ID) REFERENCES PET(PET_ID)  ON DELETE CASCADE);


CREATE TABLE EMPLOYEE(
EMPLOYEE_ID INT PRIMARY KEY,
NAME VARCHAR(20),
GENDER VARCHAR(1),
SALARY INT,
PHONE BIGINT(10));

CREATE TABLE FEEDBACK(
FEEDBACK_ID INT,
ADOPTER_ID INT,
PET_NAME VARCHAR(20),
DATE DATE,
RATING INT,
REVIEW VARCHAR(50));

INSERT INTO 
PET(PET_ID,NAME,TYPE,BREED,AGE,GENDER,STATUS)
VALUES(001,"BOND","DOG","ROTTWEILER",5,"M","TBA"),
	  (002,"SUZIE","CAT","PERSIAN",12,"F","ADOPTED"),
	  (003,"GOLDY","FISH","GOLDFISH",2,"M","TBA"),
	  (004,"FLASH","RABBIT","FLEMISH",7,"M","ADOPTED"),
	  (005,"MS.SLOW","TURTLE","MUSK",50,"F","ADOPTED"),
	  (006,"ROCK Jr","TURTLE","PAINTED",77,"M","TBA"),
	  (007,"BROWNIE","DOG","CANE CORSO",7,"F","ADOPTED"),
	  (008,"RICK","BIRD","MACAW",16,"M","TBA"),
	  (009,"LUCY","CAT","BRITISH",3,"F","TBA"),
	  (010,"NEMO","FISH","CLOWNFISH",4,"M","ADOPTED"),
	  (011,"JOHN","DOG","GOLDEN RETREIVER",10,"M","ADOPTED"),
	  (012,"COOPER","DOG","GERMAN SHEPARD",6,"M","ADOPTED"),
	  (013,"ALICE","CAT","SIAMESE",8,"F","TBA"),
	  (014,"SIMBA","CAT","BALINESE",2,"M","ADOPTED"),
	  (015,"ZIGGY","DOG","PUG",5,"M","ADOPTED");
                       
-- SELECT * FROM PET;


INSERT INTO 
MEDICAL_RECORDS(PET_ID,VACCINATION_ID,VACCINATION_STATUS,NEXT_DUE_DATE,DISEASE_HISTORY,CURRENT_DISEASES)
VALUES(001,010,"VACCINATED","2024-06-12","NONE","NONE"),
	  (002,011,"PENDING","2024-06-10","TICKS","NONE"),
      (003,012,"VACCINATED","2024-08-20","NONE","NONE"),
      (004,013,"VACCINATED","2024-07-11","NONE","NONE"),
      (005,014,"PENDING","2024-03-05","NONE","NONE"),
      (006,015,"PENDING","2024-02-29","NONE","NONE"),
      (007,016,"VACCINATED","2024-12-12","DIABETES","DIABETES"),
      (008,017,"VACCINATED","2024-10-17","BIRD MITES","NONE"),
      (009,018,"PENDING","2024-05-18","ROUNDWORMS","NONE"),
      (010,019,"VACCINATED","2024-12-24","NONE","NONE"),
      (011,020,"VACCINATED","2024-04-22","NONE","NONE"),
      (012,021,"PENDING","2024-07-27","DIABETES","DIABETES"),
      (013,022,"VACCINATED","2024-09-13","OBESITY","OBESITY"),
      (014,023,"PENDING","2024-03-14","NONE","NONE"),
      (015,024,"VACCINATED","2024-08-28","NONE","NONE");

-- SELECT * FROM MEDICAL_RECORDS;
	

INSERT INTO
ADOPTER(ADOPTER_ID,PET_ID,ADOPTER_NAME,AMOUNT,CONTACT)
VALUES (1001,001,"JAMES BOND",10000,4567892748),
	   (1002,002,"SRINIDHI",20000,3457654560),
       (1003,003,"CHALRES",5000,5637284927),
       (1004,004,"MAX",20000,4858294726),
       (1005,005,"CARLOS",45000,5837576829),
       (1006,006,"KUMAR",75000,4869482849),
       (1007,007,"ALEX",35000,0967476848),
       (1008,008,"MICHEAL",5000,8523819476),
       (1009,009,"SCOTT",12000,2847693759),
       (1010,010,"LEWIS",500,2058386946),
       (1011,011,"SEJAL",17000,7485328639),
       (1001,012,"JAMES BOND",19000,4567892748),
       (1007,013,"ALEX",30000,0967476848),
       (1010,014,"LEWIS",10500,2058386946),
       (1012,015,"RIA",25000,8574857351);

-- SELECT * FROM ADOPTER;

INSERT INTO
EMPLOYEE(EMPLOYEE_ID,NAME,GENDER,SALARY,PHONE)
VALUES(101,"ALIA","F",5000,4723846290),
      (102,"RANVEER","F",3000,5869483758),
      (103,"ALAN","F",3000,85738392758),
      (201,"AHAAN","F",5000,4536274859),
      (202,"RIHANNA","F",3000,4657328495),
      (203,"ALICIA","F",3000,8564738475);

-- SELECT * FROM EMPLOYEE;