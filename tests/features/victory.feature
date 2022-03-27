Feature: Player can win

  Player can win by putting pieces of different shapes in a row, in a column, or in an area

  Scenario: player wins in an area
    Given the following board with players de4c16 and ffffff
      | Sphere:#de4c16   | Pyramid:#ffffff |              | Cylinder:#de4c16 |
      | Cylinder:#ffffff |                 |              |                  |
      |                  |                 | Cube:#de4c16 |                  |
      |                  |                 |              |                  |
    When player ffffff moves Cube to row 1, column 1
    Then player ffffff sees you won!

  Scenario: player wins in a row
    Given the following board with players de4c16 and 222
      | Sphere:#de4c16 | Pyramid:#222 |              | Cylinder:#de4c16 |
      | Cylinder:#222  |              |              |                  |
      |                |              | Cube:#de4c16 |                  |
      |                |              |              |                  |
    When player 222 moves Cube to row 0, column 2
    Then player 222 sees you won!

  Scenario: player wins in a column
    Given the following board with players BDF7B7 and 3943B7
      | Cube:#BDF7B7     |                |  | Cylinder:#BDF7B7 |
      | Cylinder:#3943B7 |                |  |                  |
      | Pyramid:#BDF7B7  | Sphere:#3943B7 |  |                  |
      |                  |                |  |                  |
    When player 3943B7 moves Sphere to row 3, column 0
    Then player 3943B7 sees you won!
