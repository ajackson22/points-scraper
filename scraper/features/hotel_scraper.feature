Feature: Hotel Scraper

  Scenario Outline: Scrap points for all hotels for brand
    Given my desired hotel brand is "<brand>"
    When I search for all hotels in city "Austin, TX"
    Then I scrap all costs for hotels in area in "cash"
    And I scrap all costs for hotels in area in "points"
    And I calculate valuation for hotel points
    And I list the hotels
    And I show the best award redemption

    Examples:
      | brand    |
      | IHG      |
#      | Hilton   |
#      | Marriott |
#      | Radisson |