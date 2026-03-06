Feature: Movie seat booking

Scenario: User books a seat
    Given a movie "Interstellar" exists
    And seat "A1" is available
    When the user books seat "A1"
    Then the seat should be marked as booked