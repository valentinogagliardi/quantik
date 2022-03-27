Feature: Player can move pieces on the board

  Scenario: player cannot move when the same piece from another player is in the same area
    Given the following board with players de4c16 and ffffff
      |  |  |  |              |
      |  |  |  |              |
      |  |  |  | Cube:#de4c16 |
      |  |  |  |              |
    When player ffffff moves Cube to row 1, column 3
    Then player ffffff sees Cannot move Cube ffffff there!