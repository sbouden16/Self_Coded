Feature: sign in to gmail e-mail account
As a user I want to log in
and check my mails

Scenario Outline: Log in with correct data
Given user is on gmail portal
When user fills the username <username> and password <password> form and submits it
Then user can access his mails

Examples:
|username |password |
|sboudentest16@gmail.com |Asdfghjkl1234567890 |
