-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT name FROM people

SELECT full_name FROM airports JOIN flights ON airports.id = origin_airport_id;

SELECT * FROM airports JOIN flights ON airports.id = origin_airport_id WHERE full_name = "Fiftyville Regional Airport" AND day>=28;--theif must be on one of these flights

SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street" AND day=28 AND month=7;--gives description of crime: took place at 10:15 am, at humphrey street bakery, interviews conducted same day with 3 witnesses who were present, each interview mentions the bakery.

SELECT name, transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';--gives transcript of all 3 interviews of witnesses
--New Info: took earliest flight out of fiftyville on the 29th
--          The accomplice bought the ticket for that flight
--          Theif made a call for less than a minute just after 10:15 am
--          Between 10:15 and 10:25 AM the theif drove away from the parking lot

SELECT * FROM airports JOIN flights ON airports.id = origin_airport_id WHERE full_name = "Fiftyville Regional Airport" AND day = 29 ORDER BY hour LIMIT 1;--Theif was on this flight, destination airport was 4

SELECT full_name FROM airports WHERE id = "36";--destination of theif was LaGuardia Airport(New York City)

SELECT * FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration<60;--one of these calls is the theif to the accomplice

SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute>=15 AND minute<26;--one of these license plates is the theif's car

SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";--theif was one of these withdrawls

SELECT DISTINCT name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year=2021 AND month=7 AND day=28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";--names of all the people who used atm in timeframe

SELECT name FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE year=2021 AND month=7 AND day=28 AND hour=10 AND minute>=15 AND minute<26;
--names of all the people who left 10 minutes after crime

SELECT name FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id WHERE flight_id=36;
--names of all the people on the theif's flight

SELECT DISTINCT name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year=2021 AND month=7 AND day=28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw" AND name IN
(SELECT name FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE year=2021 AND month=7 AND day=28 AND hour=10 AND minute>=15 AND minute<26)
AND name IN (SELECT name FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id WHERE flight_id=36);
--people who fit all criteria other than call
--Bruce and Luca

SELECT name FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller WHERE year = 2021 AND month = 7 AND day = 28 AND duration<60;
--names of people who made call after crime for less than 60 sec

SELECT DISTINCT name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year=2021 AND month=7 AND day=28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw" AND name IN
(SELECT name FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE year=2021 AND month=7 AND day=28 AND hour=10 AND minute>=15 AND minute<26)
AND name IN (SELECT name FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id WHERE flight_id=36)
AND name IN (SELECT name FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller WHERE year = 2021 AND month = 7 AND day = 28 AND duration<60);
--name of theif who fits all criteria (Bruce)

SELECT phone_calls.id FROM phone_calls JOIN people ON people.phone_number = phone_calls.caller WHERE people.name = "Bruce" AND year=2021 AND month=7 AND day=28 AND duration<60;
--id number of phone call from theif to accomplice after crime(233)

SELECT name FROm people JOIN phone_calls ON people.phone_number = phone_calls.receiver WHERE phone_calls.id = 233;
--name of accomplice based on phone call(Robin)










