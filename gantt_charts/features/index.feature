Feature: Rocking with lettuce and django

    Scenario: Branding works
        Given I go to "localhost:8000"
        The element with id of "header" contains "gAnttlr - Gantt charts"

    Scenario: Branding works on other pages
        Given I go to "localhost:8000/project/1"
        The element with id of "header" contains "gAnttlr - Gantt charts"

    @fails
    Scenario: Logged in users can logout
    	Given I go to "localhost:8000"
    	And I am logged in as "elspeth"
    	I find a link called "Logout ?" that goes to "/logout"

    Scenario: Logged out users can log in
    	Given I am logged out
    	And I go to "localhost:8000"
    	I find a link called "Sign in" that goes to "/login"
    