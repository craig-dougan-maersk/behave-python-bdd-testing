Feature: Showing off behave (tutorial01)

Scenario Outline: Run a simple test
    Given we have some tests to run
    When we have no reason not to test
    Then The website "<url>" is up and reporting a "<status_code>" code.

    Examples: Not-Owned Sites
    | url                       | status_code |
    | http://google.co.uk       | 301         |
    | https://stackoverflow.com | 200         |
