Feature: User login successfully with valid account

  @id-1
  Scenario: User login successfully with valid account
    Given Navigate to login page with URL "http://192.168.202.48:9000/login"
    When Input valid username "Duy Nguyen"
    And When Input valid password "Duy Nguyen"
    And Click login button
    Then Login successfully and navigate to homepage with user name "Duy"
