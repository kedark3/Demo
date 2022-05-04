
# Test Plan
## Mobile Assignment
### Test Plan Identifier: AAA-BBB-123

Author: Irene Zheludenko
Date: 04/05/2022
Version: 1.0

## Contents
- [Test plan identifier](#test-plan-identifier)
- [References](#references)
- [Test items](#test-items)
- [Planning risks and contingencies, software technical risk issues](#planning-risks-and-contingencies-software-technical-risk-issues)
- [Features to be tested](#features-to-be-tested)
- [Features not to be tested (for now)](#features-not-to-be-tested-for-now)
- [QA approach (strategy)](#qa-approach-strategy)
- [Types of Testing](#types-of-testing)
- [QA Team Composition and Responsibilities](#qa-team-composition-and-responsibilities)
- [Item PASS/FAIL criteria](item-PASS/FAIL-criteria)
- [Test deliverables](#test-deliverables)


## Test plan identifier
AAA-BBB-123

## References
In this section specified the list of references related to Mobile Assignment  project, which can be helpful during perform testing activities for this project.
| No  | Document  | Description      |
| --- | --------- | ---------------- |
| 1   | link      | Test cases       | 
| 2   | link      | Checklist for Smoke testing |
| 3   | link      | Requirements    |
| 4   | link      | etc.            |     


## Introduction
This is the Test Plan for the Mobile Assignment  project.
The purpose of this Test Plan is to define the overall QA approach that will be taken by the
QA Team during testing activities and services for Mobile Assignment  project.
This document helps to clarify the scope of test activities, environment needs, types of testing, roles and responsibilities, processes and practice to be used across successive project.
This document shall be completed and used by the QA team to guide how testing will be done and lead for this project. The test effort will be prioritized and executed based on the project priorities as defined in the Project Plan/Requirements Specification/Backlog or other
documentation. This is a living document that may be refined as the project progresses.
The Product Owner, Business analyst, Project Manager and QA Lead shall review and approve the final version of the Mobile Assignment  Test Plan document.

## Test items

Based on Agile methodology, first of all should be tested such items:
- Verification requirements and acceptance criteria for Features which planned to
implement in sprints/releases
- Testing of User Stories which implemented within the sprint
- Testing of Feature/bug fixes which was implemented within the sprint or several sprints
- Testing of highly prioritized critical business functionality
- Testing of scenarios and business process flows according to business requirement with integrated systems that are in scope
- Defects maintenance (submit, verify, close, reopen)
- Regression testing of already existing and implemented functionality after fixes

## Planning risks and contingencies, software technical risk issues

| List of risks  | Description  | Probably   | Impact | 
| -------------- | ------------ | -----------| -------|
| Product requirements| Changes/inaccuracies/poorness/absence  | medium | high   |
| Interaction with API| Troubles in delivery of a third party products| high | high | 
| Regression risks | Releasing of build with critical/blocker bug found after release | low | high | 


## Features to be tested
According to Backlog such items and functionality of Mobile Assignment  should be tested:


| Link to Jira  | Functional area  | Description Priority   |
| -------------- | ------------ | -----------|
| MA-09  | Search flow  | Integration with Google maps | high   |

## Features not to be tested (for now)

## QA approach (strategy)
After analysis the initial version of product and project overview we concluded that the following mix of testing strategies will be the most suitable for testing the product (it can be changed based on the project needs):

| Strategy  | Description  | Reasons to use  |
| -------------- | ------------ | -----------|
|  |  |  |

## Types of Testing
Functional Testing of the user stories should execute according to the acceptance criteria.
Functional and Regression Testing of the Epic (set of stories) should be started after all stories of corresponding Epic was successfully tested before and marked as “Done” (in Agile terminology).
For Testing purpose should execute such Type of Testing:

1. User Stories Review:
a. static analysis of business requirements, acceptance criterias
b. make suggestions what should be adde
2. Functional Testing:
a. functional testing of base functionality
b. functional testing of the stories, which implementing within the sprint by
development team according to acceptance criteria
c. functional testing of Improvements, which implementing within the sprint
3. Regression Testing:
a. stories testing after major corresponding defects was fixed
b. testing of already existing features, scenarios and business process flow of the
whole system that are critical from the business side
4. Smoke Testing - testing of critical flows from business side
5. Confirmation Testing - Defect re-testing
6. Usability Testing - checking usability issues, navigations and content
7. UX/UI - inspect user’s experience and UI when interacting with the product
8. Localization Testing ? - check localization for languages
9. Cross-Platform Testing ? - checks application with supported platforms/devices



## QA Team Composition and Responsibilities
Based on existing scope of work, planned activities and current backlog for Mobile Assignment release, we propose such team composition:

| Full Name  | Position / Role  | Responsibilities      |
| --- | --------- | ---------------- |
| Irene Zheludenko  | AQA (IOS)     | Test Plan creation, Tasks Estimation, Requirement review/testing,Test Case/Checklist creation, Manual tests execution, Defects maintenance       |


## Item PASS/FAIL criteria
Testing activities is completed in case of:
- All User stories are done according to acceptance criteria
- No any defects with “Critical” or “Major” priority
- All Planned Testing Activities are completed
- Functional testing of whole system with already integrated components according to requirements completed successfully
- All non-functional types(usability, UX/UI) of testing are done
- Regression testing of whole system with already integrated components according to requirements completed successfully


## Test deliverables
- Test Plan
- Test Cases
- Defects
- Smoke, regression checklists
- Test Reports





