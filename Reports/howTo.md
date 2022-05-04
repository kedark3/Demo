# How to Run Tests in Android Studio

Make sure you have an app/src/androidTest/java folder 
1. Run ALL test:
- right click on Test class file and select 'Run'

<img width="250" alt="AS1" src="https://user-images.githubusercontent.com/104631202/166688913-139edf09-f929-4eaf-a939-2c7a825453f2.png">

or
- open Test class file
- tap 'double play' icon on line public class ..Test { of your test case.
<img width="250" alt="AS2" src="https://user-images.githubusercontent.com/104631202/166692784-de783b39-63d9-4ebd-8650-99090bb8ebc3.png">

2. Run a Single test by tapping 'Play' icon in front of chosen test
<img width="250" alt="AS3" src="https://user-images.githubusercontent.com/104631202/166693031-24df6e0f-01c8-49b3-a440-f73c1cf19fef.png">

# How to retrieve the Automation Test Report

Make sure you swith to Run tab in toolbar
1. After All test run finished, tap 'Export Test Results' icon 
<img width="250" alt="AS4" src="https://user-images.githubusercontent.com/104631202/166693674-05305bb7-0db7-4a29-96e7-2c4e0dfc3dbc.png">
2. Chose format from provided
<img width="250" alt="AS5" src="https://user-images.githubusercontent.com/104631202/166693863-44f132b8-19b4-44f6-9154-25a9c8943ca5.png">
3. Tap 'OK'


# BB-Mobile-QA-assignment - Test plan <!-- omit in toc -->

- [IDENTIFICATION INFORMATION SECTION](#identification-information-section)
  - [PRODUCT](#product)
  - [PROJECT DESCRIPTION](#project-description)
  - [TEST PERSONNEL](#test-personnel)
  - [PROGRAMMERS](#programmers)
- [AUTOMATION TEST SECTION](#automation-test-section)
  - [AUTOMATION TEST STRATEGY](#automation-test-strategy)
  - [AUTOMATION TEST CASES](#automation-test-cases)
  - [AUTOMATION TEST EVIDENCE](#automation-test-evidence)
- [INTEGRATION TEST SECTION](#integration-test-section)
  - [INTEGRATION TEST STRATEGY AND EXTENT OF INTEGRATION TESTING](#integration-test-strategy-and-extent-of-integration-testing)
  - [INTEGRATION TEST CASES](#integration-test-cases)
- [USER ACCEPTANCE TEST SECTION (To be completed by the business office)](#user-acceptance-test-section-to-be-completed-by-the-business-office)
  - [USER ACCEPTANCE TEST STRATEGY](#user-acceptance-test-strategy)
  - [USER ACCEPTANCE TEST CASES](#user-acceptance-test-cases)
- [BUGS AND ISSUES REPORT](#bugs-and-issues-report)

## IDENTIFICATION INFORMATION SECTION

### PRODUCT

- **Product Name:** Mobile Assignment

### PROJECT DESCRIPTION

These test scenarios are introductory, being based on architectural requirements and an understanding of the Mobile Assignment project from BackBase.

### TEST PERSONNEL

- LEANDRO LESSA 

### PROGRAMMERS

- LEANDRO LESSA

## AUTOMATION TEST SECTION

### AUTOMATION TEST STRATEGY 

The application was evaluated and the following test cases were selected for the automation case. 

### AUTOMATION TEST CASES

| \#  | TEST ID | OBJECTIVE | 
| --- | --- | ---|
| 1   | SearchForACityWithCityName | This test searches for a city with an entire city name and selects the city |
| 2   | SearchForInvalidCity |  This test searches for a invalid city name  |
| 3   | SelectCityWithoutInformValueInSearchField | This test select a city without search |
| 4   | SearchWithOnlyInitialCharOfCities | This test searches for a the initial char of the City |
| 5   | SelectCityAndCheckGoogleMapsDisplays | Select a city and verify if google maps is displayed in the next screen  |

### AUTOMATION TEST EVIDENCE

![image info](./images/TestAutEvidences.png)

## INTEGRATION TEST SECTION

Combine individual software modules and test as a group.

### INTEGRATION TEST STRATEGY AND EXTENT OF INTEGRATION TESTING

Evaluate all integrations with locally developed shared libraries, with consumed services, and other touch points.

### INTEGRATION TEST CASES

| #   | OBJECTIVE | INPUT | EXPECTED RESULTS | TEST DELIVERABLES |
| --- | --------- | ----- | ---------------- | ----------------- |
| 1   |           |       |                  |                   |

## USER ACCEPTANCE TEST SECTION (To be completed by the business office)

Verify that the solution works for the user

### USER ACCEPTANCE TEST STRATEGY

{Explain how user acceptance testing will be accomplished}

### USER ACCEPTANCE TEST CASES

| #   | TEST ITEM | EXPECTED RESULTS | ACTUAL RESULTS | DATE |
| --- | --------- | ---------------- | -------------- | ---- |
| 1   |           |                  |                |      |

## BUGS AND ISSUES REPORT
